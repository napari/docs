### The amazing new Grid mode! 🗺️

The visualization of Grid mode has been redone from the ground up! This new Grid mode [(#7870)](https://github.com/napari/napari/pull/7870) now puts each layer into its own view (a VisPy Viewbox) with cameras linked together. Now, you can pan and zoom one view, and all other views in the grid will follow along. Layers are no longer awkwardly transformed into the same world space and displayed in a grid, only to make comparing the details of each a challenge.

Grid based exploration is now fluid, fast, and intuitive, especially when working with large images and 3D+ data! The mouse can even be used over one View, while updating the data, such as a label or shape annotation, in the selected layer of a different view. The usual napari overlays can now also be added to each grid, instead of just the canvas (eg. `viewer.scale_bar.gridded = True`).

Grid mode spacing now works proportionally to the layer extents (i.e. [0,1), as in 0.6.0) or as a pixel value [1,1500) and will automatically adjust if needed.

![grid mode](https://github.com/user-attachments/assets/fbcb216c-666b-43a6-bf25-aad82d5e9d92)

To coincide with this new Grid mode, we have chosen to reverse the ordering of layers in the grid [(#8053)](https://github.com/napari/napari/pull/8053). The first layer added to the viewer will now be at the top left of the grid, and the last layer added will be at the bottom right; new layers will be added to the bottom right of the grid. If you prefer the previous behavior, you can set the Grid Stride to `-1` in the Preferences dialog.

![Stride preference](https://github.com/user-attachments/assets/528aebca-d623-4f9a-97f4-691329d2a2a7)

### The Features Table Widget is now a napari builtin! 📊

The features table from [napari-properties-viewer](https://github.com/kevinyamauchi/napari-properties-viewer) is now a builtin widget in napari [(#7877)](https://github.com/napari/napari/pull/7877) *and* greatly improved! This widget allows you to view and edit the properties of Points, Shapes, and Labels layers in a table widget.

The widget can be opened from the `Layers` menu -> `Visualize` -> `Features table widget (napari builtins)` or from the command palette.  You can also save the properties table to a CSV file. Check out the [Features table widget](https://napari.org/dev/gallery/features_table_widget.html) example to learn more.

![Features table widget in napari](https://github.com/user-attachments/assets/2c218f05-6510-4192-b5c8-fb6d135e4863)

### Community developments! 📅

We are excited to share our new [active roadmap](https://napari.org/stable/roadmaps/active_roadmap.html) which is a living document that will be updated as we continue to develop napari. This document is intended to help the community understand the priorities of the napari team and to help us all work together to make napari better.

We are also now including all napari related events in the [community calendar](https://napari.org/stable/community/meeting_schedule.html) and as an [image.sc post](https://forum.image.sc/t/napari-community-meetings-and-events/113689), including conferences, tutorials, sprints, virtual seminars, and more. If you have an event you would like to add, please reach out to us!

### Some great features for contributors! 🛠️

1. **Contributing documentation is now a much smoother experience!** By default, new documentation will build in around 3 minutes, instead of the previous 20 minutes. This speed is thanks to new, slimmer `make` commands (`slimfast` by default) that can also be triggered in PRs with a bot (eg. `@napari-bot make docs`). Read our updated [docs contribution guide](https://napari.org/dev/developers/contributing/documentation/index.html) and reach out for help.
2. **The organization of the napari repo has been updated by moving into a `src/` directory [(#7952)](https://github.com/napari/napari/pull/7952).** This is modern best practice in Python projects (and what has long been standard in our [napari-plugin-template](https://github.com/napari/napari-plugin-template)) to avoid issues with relative imports and *should* now always result in importing the napari version installed in the current environment. For developers, especially of pull requests prior to this release, you may have many merge conflicts to resolve. Please ping the napari team if you would like help resolving these conflicts.
3. **There is now public API to access widgets docked in the viewer [(#7965)](https://github.com/napari/napari/pull/7965).** Check out the new documentation on the napari website to learn more about using this API to [communicate between widgets](https://napari.org/dev/plugins/advanced_topics/widget_communication.html). If you previously used `viewer.window._dock_widgets`, you should now use `viewer.window.dock_widgets`.
