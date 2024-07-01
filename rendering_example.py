import napari

viewer = napari.Viewer()
viewer.open_sample('napari', 'cells3d')

from napari.utils import nbscreenshot

nbscreenshot(viewer, alt_text="3D cell nuclei and membranes rendered as 2D slices in the napari viewer")

viewer.dims.range

viewer.layers[0].data.shape

viewer.dims.point

viewer.dims.point = (0, 0, 0)

nbscreenshot(viewer, alt_text="3D cell nuclei and membranes rendered as 2D slices in the napari viewer")

print(f'{viewer.dims.margin_left=}')
print(f'{viewer.dims.margin_right=}')
print(f'{viewer.dims.thickness=}')

viewer.dims.point = (29, 0, 0)
viewer.dims.thickness = (16, 0, 0)
print(f'{viewer.dims.margin_left=}')
print(f'{viewer.dims.margin_right=}')

viewer.layers[1].projection_mode = 'mean'

nbscreenshot(viewer, alt_text="3D cell nuclei and membranes rendered as 2D slices in the napari viewer")

import numpy as np

mean_data = np.mean(viewer.layers[1].data, axis=0)
viewer.add_image(mean_data, colormap=viewer.layers[1].colormap)
world_dims = np.asarray(viewer.dims.order)
layer1_dims = viewer.layers[1]._world_to_layer_dims(
  world_dims=world_dims, ndim_world=3)
layer2_dims = viewer.layers[2]._world_to_layer_dims(
  world_dims=world_dims, ndim_world=3)
print(f'{layer1_dims=}')
print(f'{layer2_dims=}')

point = viewer.dims.point
layer1_point = viewer.layers[1].world_to_data(point)
layer2_point = viewer.layers[2].world_to_data(point)
print(f'{layer1_point=}')
print(f'{layer2_point=}')

viewer.close()