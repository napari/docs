# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "napari[all] @ git+https://github.com/napari/napari.git@main",
#   "scipy",
#   "pooch",
# ]
# ///

"""Generate the napari OpenGraph social-preview image.

Renders the tribolium embryo (Lund embryo) in 3D with a watershed
segmentation overlay and saves the 1200x630 PNG referenced by
``sphinxext-opengraph`` in ``docs/conf.py``.

Usage:
    uv run docs/_scripts/opengraph_preview.py
"""

from pathlib import Path

import napari
import pooch
import scipy.ndimage as ndimage
from skimage import filters, measure, morphology, segmentation
from skimage.io import imread

SCRIPT_DIR = Path(__file__).resolve().parent
DATA_URL = 'https://github.com/clEsperanto/clesperanto_example_data/raw/main/Lund-100MB.tif'
DATA_CACHE_DIR = SCRIPT_DIR / 'data'
OUTPUT_PATH = SCRIPT_DIR.parent / '_static' / 'opengraph_image.png'
DATA_HASH = 'sha256:7e39ddf7669b42303eec4cd24207dda1a1dd21847eb47354797ac647bd982110'
data_path = Path(
    pooch.retrieve(DATA_URL, known_hash=DATA_HASH, path=DATA_CACHE_DIR)
)
WINDOW_SIZE = (1200, 630)

# TZYX tribolium image — keep only the first timepoint.
img = imread(data_path)[:, :, :, :]

# use a tophat filter to remove the background
img_bs = ndimage.white_tophat(img, size=10)

# blur the image to smooth out noise from the background subtraction
img_blur = filters.gaussian(img_bs, 1)

# detect maxima in the blurred image for watershed seeds
img_spot_maxima = morphology.local_maxima(img_blur)

# create a threshold mask
img_otsu = img_blur > filters.threshold_otsu(img_blur)

# keep only maxima spots that are inside a thresholded area
img_threshold_spots = img_spot_maxima * img_otsu

# create a connected components labeling of the thresholded image
# using the local maxima as markers, as a seed for a voronoi diagram
img_labeled_spots = measure.label(img_threshold_spots)
img_labels = segmentation.watershed(
    img_otsu,
    markers=img_labeled_spots,
    mask=img_otsu
)

viewer = napari.Viewer()

image = viewer.add_image(
    img,
    name='tribolium',
    units=(None, 'µm', 'µm', 'µm'),
    axis_labels=['T', 'Z', 'X', 'Y'],
)
# image.histogram.enabled = True
labels = viewer.add_labels(
    img_labels,
    name='tribolium labels',
    opacity=0.5,
    iso_gradient_mode='smooth',
    units=(None,'µm', 'µm', 'µm'),
    axis_labels=['T', 'Z', 'X', 'Y'],

)
viewer.layers.selection = [image]
viewer.window.resize(*WINDOW_SIZE)
viewer.dims.ndisplay = 3
viewer.scene.camera.angles = (83, 12, -2)
viewer.canvas.overlays.axes.visible = True
viewer.canvas.overlays.scale_bar.visible = True
viewer.canvas.overlays.scale_bar.font_size = 20
viewer.fit_to_view(margin=0)

viewer.screenshot(path=OUTPUT_PATH, canvas_only=False)
print(f'Saved OpenGraph image to {OUTPUT_PATH}')

napari.run()
