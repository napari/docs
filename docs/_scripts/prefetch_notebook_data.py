"""Download the TIFF image that ``getting_started/open_images.md`` opens.

The Makefile target ``prefetch-notebooks`` runs this script before each build
that executes the notebooks. pooch stores the file in its default OS cache
directory.
"""

import pooch

# The notebook makes this same call, so both use one cached file.
pooch.retrieve(
    url="https://ftp.ebi.ac.uk/biostudies/fire/S-BIAD/582/S-BIAD582/Files/01_wt_Dprotein555-TL/raw_mps/5-2b_01_wt_Dprotein555-TL_003_rawmp.tif",
    known_hash='5b43ed0269eaa1eebf4c48079270a30e6cc40e87f20cc36c1b3d5a07c51c7b20',
    fname='5-2b_01_wt_Dprotein555-TL_003_rawmp.tif',
)
