"""Download the nilearn data for the gallery example ``surface_timeseries``.

The Makefile target ``prefetch-gallery`` runs this script before each build
that executes the gallery examples. nilearn stores the data under
``NILEARN_DATA``, which the Makefile sets to a directory in the OS cache.
"""

from nilearn import datasets

# The gallery example reads NILEARN_DATA too, so it finds this data.
datasets.fetch_surf_nki_enhanced(n_subjects=1)
datasets.fetch_surf_fsaverage()
