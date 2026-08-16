# Progressive image loading
The progressive loader in napari is experimental. It provides viewport aware, progressive chunk-wise
loading for very large multiscale images in napari. It uses the already existing multiscale layers in 
napari

The progressive loader ensures that an entire image pyramid level is not fully materialized before
displaying it. For this, it does the following:
1. It determines which resolution and spatial region are currently useful.
2. Ensures that something renderable is available immediately, e.g. (part of the) lowest resolution of the pyramid
3. Fetches missing chunks of current resolution level based on a priority order (distance from center chunk).
4. Progressively replaces the coarse, low resolution fallbak data with higher-resolution data.
5. Updates the displayed texture while limiting work that could interrupt interaction.

As a result, the napari viewer can work with datasets substantially larger than CPU or GPU memory
while still keeping navigation responsive.

## Core concepts
In order to understand the progressive loader we will first explain some of the concepts needed to 
understand it.

### Multiscale data and `VirtualData`
The source data is a multiscale pyramid ordered from highest to lowest resolution.

Rather than passing the source arrays directly to napari, each pyramid level is wrapped by
`VirtualData`. These arrays still look like arrays to napari, with the full shape of their 
corresponding resolution level, but internally they keep only a bounded resident interval 
in CPU memory (RAM).

The purpose of `VirtualData` is to separate the actual logical size of an image from the amount 
of data that must actually be materialized at any given time.

```{mermaid}
flowchart TD
    A["Chunked source"]
    B["VirtualData / multiscale<br/>pyramid"]
    C["Resident interval<br/>in RAM"]
    D["vispy texture"]
    E["Canvas"]

    A --> B
    B -->|"fetch missing chunks"| C
    C -->|"slice / patch"| D
    D --> E
```
Napari's rendering is not replaced. Rather the progressive loader adds coordination between
the different components of the existing rendering pipeline. We will now go more in detail.

### Resident interval
Only the region needed for the current view is kept resident at a fine-resolution level. The interval 
follows the viewport as the user pans, zooms, or changes dimensions. For displayed dimensions, it is 
derived from the layer's corner_pixels; non-displayed dimensions are restricted to the current 
dimension step. So for 2D data it would conceptually look like this:

```{mermaid}
flowchart TB
    subgraph P["Full pyramid level"]
        direction TB
        R["Resident interval<br/>currently held in<br/>CPU memory"]
    end
```
This resident interval is also bounded by memory and GPU texture limits. Moving the viewport moves the 
resident interval instead of the camera on a fully materialized resolution level.

### Resident coarsest level
This level is the lowest resolution level of the pyramid and it is treated specially. When it fits
within `resident_max_bytes`, it is kept fully in RAM. This to provide:
- immediate low-resolution context
- data for layer thumbnails
- a backdrop source for finer levels

It gives the user something to immediately show, while higher resolution chunks are still being fetched.

### Backdrop data
When zooming and panning, a fine-resolution interval does not have to start empty. 
hen the new interval overlaps the previous one, such as during a pan, already loaded 
target-resolution data in the overlapping region is retained. Only the newly exposed or 
otherwise unloaded regions need temporary coverage.
For those unloaded regions, the loader uses already available data from another pyramid 
level as a backdrop. It prefers the closest-resolution level whose resident data covers 
the requested region. If no closer level provides sufficient coverage, the resident coarsest 
level can serve as the fallback. Backdrop data is upsampled to the target resolution before 
being written into the target resident interval.
The backdrop therefore provides temporary image content. It does not mark those regions as 
loaded at the target level. They still need to be replaced by actual target-resolution chunks.
When `coarse_first=True`, the backdrop can be progressively improved before the target level is 
fetched. Missing chunks from intermediate pyramid levels are fetched from coarse to fine. As 
those chunks arrive, their data is upsampled and folded into regions of the target interval 
that do not yet contain loaded target chunks. Intermediate levels are not rendered directly.
Finally, missing target-level chunks are fetched and written into the target level's resident 
interval in `VirtualData`, which is held in RAM. These chunks replace any backdrop or 
intermediate-resolution data in the corresponding regions. Once all required target-level 
chunks for the requested view have been loaded, those regions of the resident interval 
contain actual target-rresolution data.

The flow for populating and progressively refining a resident interval is therefore like this:
```{mermaid}
flowchart TD
    A["View changes<br/>pan or zoom"] --> B["Establish target<br/>resident interval"]

    B --> C["Carry over already loaded<br/>target-level data"]

    C --> D["Identify unresolved regions"]

    D --> E["Fill unresolved regions<br/>from available backdrop data"]

    E --> F["Upsample backdrop data<br/>to target resolution"]

    F --> G["Resident interval has<br/>useful image coverage"]

    G --> H{"coarse_first?"}

    H -- Yes --> I["Fetch missing chunks from<br/>intermediate pyramid levels<br/>coarse → fine"]

    I --> J["Upsample intermediate data into<br/>regions without target-level chunks"]

    J --> K["Progressively sharper<br/>temporary coverage"]

    K --> L["Fetch missing<br/>target-level chunks"]

    H -- No --> L

    L --> M["Write target chunks into<br/>VirtualData in CPU memory"]

    M --> N["Replace backdrop or intermediate<br/>data in corresponding regions"]

    N --> O{"Missing target<br/>chunks remain?"}

    O -- Yes --> L
    O -- No --> P["Requested view is fully resolved<br/>at the target resolution"]
```
The key take away here is that backdrop data, intermediate data and target-level data can coexist
within the same resident interval while loading is in progress. The resident coarsest level, backdrop
and intermediate data provide immediate visual coverage, while the set of loaded target chunks 
determines which regions have actually been resolved at the requested resolution. With `coarse_first=True`, 
intermediate levels progressively sharpen unresolved regions and with `coarse_first=False`, 
the loader proceeds directly from the initial backdrop to target-level chunks.

## How progressive loading works in the experimental implementation
In the previous section we described some of the nomenclature, how data is represented and how it 
is progressively refined. Here, we will describe how the loader decides what to load as the user
interacts with the viewer. 
`ProgressiveLoader` responds to changes in the viewer and layer that can affect what data is needed.
Examples of this are camera movement, dimension changes, display mode, layer visibility and changes
to the selected resolution level.
When there is such an event, the loader does not always immediately start a new fetch. Events such 
as camera interactions often generate many events in quick succession. Therefore, the loader waits 
for the view to settle before determining the next region to load. While the user is actively interacting,
expensive streaming and rendering work can also be temporarily suspended to keep navigation responsive.

Once the view is settled, the loader determines a couple of things:
1. Which pyramid level should be used.
2. Which region of that level is needed for the view.
3. What part of the region is already resident or currently being fetched.

If the required data is not fully resident / in RAM, a new data fetch is started.
We present this here schematically:

```{mermaid}
flowchart TD
    A["Viewer or layer<br/>state changes"] --> B["Interaction detected"]

    B --> C["Temporarily limit<br/>streaming and rendering work"]

    C --> D["Wait for view<br/>to settle"]

    D --> E["Determine target<br/>pyramid level"]

    E --> F["Determine required<br/>resident interval"]

    F --> G{"Required region<br/>already fully covered?"}

    G -- Yes --> H["No new fetch<br/>pass required"]

    G -- No --> I["Start new<br/>fetch pass"]

    I --> J["Populate and progressively<br/>refine resident interval"]
```
We will now describe these 3 steps in more detail

### 1. Selecting the resolution level
The way the resolution level is determined varies between 2D and 3D data in napari.
This because loading 3D data at a given resolution level could prove to be too
expensive. We will describe the selection of the resolution level in both 2D and 3D.

### Selection the resolution level for 2D data
For 2D data, napari's existing multiscale API selects the resolution level. The 
progressive loader uses the elvel selected by this API rather than introducing
a separate mechanism for selecting the target resolution.
As such, `locked_data_level` (TODO: explain this) is respected. Once the level is known,
the loader determines the region required for the current view from the layer's 
`corner-pixels`.

### 1. Selecting the resolutoin level for 3D data
For 3D data, the resolution level can either be selected automatically by the progressive loader 
or controlled through napari's normal level selection. This has different trade offs.

With a setting `auto_level_3d=True`, the progressive loader automatically selects the resolution
level based on the camera zoom (TODO check whether this is napari selected). It then aims to select 
the coarsest level of which the voxels project to no more than `max_pixel_size_3d` screen pixels 
(the unit here is pixels per voxel). Lower values cause finer, more expensive levels to be selected 
sooner while zooming in. For example, with `max_pixel_size_3d=2.0`, a finer level is preferred once a 
voxel would occupy more than two screen pixels.
The visually appropriate level must also be practical to load and render. If the desired level would 
exceed constraints such as the resident-interval memory budget or the maximum number of chunks 
allowed for a 3D fetch pass, the loader selects a coarser level instead.
When auto_level_3d=False, the progressive loader does not automatically change the pyramid level in 
response to camera zoom. Level selection is left to napari or to the user. The loader still performs 
progressive loading for whichever level is currently selected: it determines the required resident 
interval, provides backdrop coverage, and fetches the missing chunks for that level.
If the user explicitly selects a resolution level while automatic 3D level selection is enabled, 
that selection takes precedence and automatic level changes are suspended. Returning the resolution 
selector to Auto gives level selection back to the progressive loader.

The whole mechanism of 3D resolution level selection can therefore be summarized schematically as:
```{mermaid}
flowchart TD
    A["3D view"] --> B{"auto_level_3d?"}

    B -- No --> C["Use level selected by<br/>napari or the user"]

    B -- Yes --> D{"User explicitly<br/>selected a level?"}

    D -- Yes --> C

    D -- No --> E["Determine coarsest level that<br/>satisfies max_pixel_size_3d"]

    E --> F{"Level fits memory and<br/>chunk-count constraints?"}

    F -- Yes --> G["Use selected level"]

    F -- No --> H["Try a coarser level"]

    H --> F

    C --> I["Progressively load<br/>selected level"]
    G --> I
```
With this design, 2 concerns are separated: automatic level selection determines which resolution 
to use, while progressive loading determines how the selected level is populated and displayed.

### 2. Determining the region to load
ONce a resolution level has been selected, the loader determines which part of that elvel is relevant
to the current view. 
For displayed dimensions, this region is based on the layer's `corner_pixels`. For dimensions that are 
not currently displayed, only the current dimension step needs to be represented (TODO: check with Kyle
if he sees value here for different mode, e.g. with tracking data).
The requested region is then converted into the resident interval used by `VirtualData`.

The resident interval can be larger than the exact rendered viewport. Specifically, the GPU texture
contains the crop described by `corner_pixels`, while the resident interval on the CPU follows underlying
chunk boundaries and can therefore extend beyond the rendered region as shown below:

```{mermaid}
flowchart TB
    subgraph R["Resident interval in RAM"]
        direction TB

        V["Rendered viewport<br/>represented by GPU texture"]
    end
```

### 3. Fetching chunks
After the resident interval and backdrop have been established, the loader determines which chunks 
still need to be loaded. 
The source arrays are chunked, meaning that the data is divided in predefined blocks, rather than 
arbitrary pixel slices. Only chunks intersercting the requested region are considered with chunks
already recorded as loaded excluded from the fetch queue. 
As stated before, the resident interval follows the underlying data source chunk boundaries, 
while the viewport contains a crop of it. While this may cause the resident interval to contain
data outside the visible viewport, it avoids repeatedly partially fetching chunks as the view moves.
Thus, an overview of fetching chunks looks like this:

```{mermaid}
flowchart TD
    A["Visible viewport"] --> B["Determine intersecting<br/>source chunks"]

    B --> C["Chunk-aligned<br/>resident region"]

    C --> D["Exclude chunks that<br/>are already loaded"]

    D --> E["Prioritize remaining<br/>missing chunks"]

    E --> F["Fetch chunks"]
```
We will now discuss chunk priority and fetch workers.

#### Chunk priority
Missing chunks are not fetched with storage order in mind, rather they are prioritized based on
their relevance to the current view.

In 2D, chunks are prioritized based on their distance to the center of the resident interval. Distance is 
not calculated for all chunks of the underlying data source. Instead, only distance is only calculated for
chunks intersecting with the resident interval.

For 3D, the camera is also taken into account. Chunks are primarily fetched based on their depth
along the view direction, with those closest to the viewer loading first. The distance from the camera
center line provides a second, but lower weighted, prioritization for fetching chunks. This ensures
chunks on the camera center line will be prioritized when multiple chunks are present at equal depth.

For both 2D and 3D data, the aim is not to resolve every chunk intersecting with the resident interval simultaneously,
but to spend the available loading capacity first on those chunks likely to visually matter the most.

#### Fetch workers
Fetching chunks happens on background worker threads, rather than on the main thread. The number of concurrent workers 
is controlled by fetch_workers. By default, the implementation uses up to four workers while deliberately leaving 
CPU capacity (2 cores by default) available for the GUI.

In summary, a fetch thus happens in a way shown in this diagram:
```{mermaid}
flowchart TD
    A["Target resident interval"] --> B["Find intersecting chunks"]

    B --> C["Remove already<br/>loaded chunks"]

    C --> D["Prioritize missing chunks"]

    D --> E{"coarse_first?"}

    E -- Yes --> F["Fetch intermediate-level<br/>chunk stages first"]

    F --> G["Fill unresolved target regions with<br/> intermediate-level data"]

    G --> H["Fetch target-level chunks"]

    E -- No --> H

    H --> I["Write fetched chunks into<br/>target VirtualData in RAM"]

    I --> J["Update displayed data"]

    J --> K{"More target chunks<br/>to fetch?"}

    K -- Yes --> H
    K -- No --> L["Fetch pass complete"]
```

### Keeping interaction responsive
