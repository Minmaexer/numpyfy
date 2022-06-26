import numpy

def test_default():
    return True

# Convert a fits file into a numpy array
def fits_to_numpy(filename):
    hdu_list = fits.open(filename)
    data = hdu_list[0].data
    hdu_list.close()
    return data

