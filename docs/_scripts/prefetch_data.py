"""Pre-fetch the remote data that some documentation builds download.

# fetch only what is needed per run type
python docs/_scripts/prefetch_data.py --gallery
python docs/_scripts/prefetch_data.py --notebooks

# fetch all data sets
python docs/_scripts/prefetch_data.py
"""

import sys

from nilearn import datasets
import pooch


def prefetch_gallery_data():
    """Warm the nilearn data used by gallery example surface_timeseries."""
    # nilearn caches into NILEARN_DATA, which the Makefile points at the OS
    # cache directory, so this and the gallery example agree on a location
    datasets.fetch_surf_nki_enhanced(n_subjects=1)
    datasets.fetch_surf_fsaverage()


def prefetch_notebook_data():
    """Warm the images used by the getting_started/open_images.md notebook."""
    # plain pooch.retrieve calls, so this shares the notebook's own cache
    pooch.retrieve(
        url="https://ftp.ebi.ac.uk/biostudies/fire/S-BIAD/582/S-BIAD582/Files/01_wt_Dprotein555-TL/raw_mps/5-2b_01_wt_Dprotein555-TL_003_rawmp.tif",
        known_hash='5b43ed0269eaa1eebf4c48079270a30e6cc40e87f20cc36c1b3d5a07c51c7b20',
        fname='5-2b_01_wt_Dprotein555-TL_003_rawmp.tif',
    )


def main(only=None):
    """Prefetch both data sets, or only the ``gallery``/``notebooks`` one."""
    if only not in (None, 'gallery', 'notebooks'):
        raise SystemExit(f'expected gallery or notebooks, got {only!r}')
    if only in (None, 'gallery'):
        prefetch_gallery_data()
    if only in (None, 'notebooks'):
        prefetch_notebook_data()


if __name__ == '__main__':
    main(*sys.argv[1:])
