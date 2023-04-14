# Using Dask and napari to view and process a high-resolution human brain imaging dataset

We used napari to view and process a high-resolution human brain imaging dataset, and in the following tutorial we will break down how it all builds up!

The dataset was obtained from [Dr. Brian Edlow's Lab](https://www.comarecoverylab.org/) for NeuroImaging of Coma and Consciousness, which is dedicated to promoting recovery of consciousness in people with severe brain injuries.
This dataset is a 100 micron resolution magnetic resonance imaging (MRI) scan of an ex vivo human brain specimen. The brain specimen was donated by a [58-year-old woman](https://www.youtube.com/watch?v=Q-9jzBkoNuI) who had no history of neurological disease and died of non-neurological causes.
This dataset was originally described in [Edlow, B.L., Mareyam, A., Horn, A. _et al._ 7 Tesla MRI of the ex vivo human brain at 100 micron resolution. Sci Data 6, 244 (2019)](https://doi.org/10.1038/s41597-019-0254-8).

#### Getting the data

You can download the dataset from [here](https://datadryad.org/stash/dataset/doi:10.5061/dryad.119f80q). A `.zip` file will be downloaded, and after extracting the compressed dataset the `.tiff` images can be found in the `SYNTHESIZED_TIFF_Images_Raw/Synthesized_FLASH25_100um_TIFF_Axial_Images/` directory. The dataset is 3.69 GB unzipped.

An important concept to bear in mind when going through this tutorial is [Lazy Loading](https://en.wikipedia.org/wiki/Lazy_evaluation), i.e., only loading images to memory when the position slider on napari maps to that particular image, which is very useful when using large datasets.

#### So how can we lazily load an image using dask?

While we could use plain `dask` through `delayed`, as we have shown in the [](dask.md) tutorial, we will [make our lives easier](make-your-life-easier-with-dask-image) and use `dask-image`.

Using [dask_image.imread](https://image.dask.org/en/latest/dask_image.imread.html#module-dask_image.imread), loading the entire dataset to view in napari is straightforward.

``` python
import napari
from dask_image.imread import imread

if __name__ == '__main__':
    # Load images
    images = imread(
        'SYNTHESIZED_TIFF_Images_Raw/Synthesized_FLASH25_100um_TIFF_Axial_Images/Synthesized_FLASH25_Axial_*.tiff'
        )

    with napari.gui_qt():
        napari.view_image(images) 
```

__And here's the final output!__

![Alt text](https://media.giphy.com/media/LO3gPbCs5AxApjAehW/giphy.gif)
