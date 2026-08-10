from nilearn import datasets
import pooch


def main():
    # example surface timeseries
    datasets.fetch_surf_nki_enhanced(n_subjects=1)
    datasets.fetch_surf_fsaverage()

    #getting_started/open_images.md
    pooch.retrieve(
        url="https://ftp.ebi.ac.uk/biostudies/fire/S-BIAD/582/S-BIAD582/Files/01_wt_Dprotein555-TL/raw_mps/5-2b_01_wt_Dprotein555-TL_003_rawmp.tif",
        known_hash='5b43ed0269eaa1eebf4c48079270a30e6cc40e87f20cc36c1b3d5a07c51c7b20',
        fname='5-2b_01_wt_Dprotein555-TL_003_rawmp.tif',
        path=download_folder
    )
