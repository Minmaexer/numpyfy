import numpy as np
import numpyfy as nfy
from PIL import Image
import math
from astropy.io import fits
from pathlib import Path

# a = nfy.to_fits(np.ones((10, 10)), 'test.fits')
# b = nfy.from_png_file('/home/preller/h/workspace/pypi/manual/numpyfy/tests/files/test.png')
# print(b)


# # Save the contents of a variable to a file
# def to_file(data, filename):
#     # Using savetxt
#     np.savetxt(filename, data)


# to_file(b, '/home/preller/h/workspace/pypi/manual/numpyfy/tests/files/test_data')

# # numpy print all unique values in array
# print(np.unique(b))

# # print all unique values in array and count them
# print(np.unique(b, return_counts=True))

# # create an image from a numpy array
# img = Image.fromarray(b)
# img.save('/home/preller/h/workspace/pypi/manual/numpyfy/tests/files/test_image2.png')


imgpath = '/home/preller/h/workspace/pypi/manual/numpyfy/tests/files/test.png'
datapath = '/home/preller/h/workspace/pypi/manual/numpyfy/tests/files/test_data2'
resultpath = '/home/preller/h/workspace/pypi/manual/numpyfy/tests/files/test3.png'

# # Load a PNG file into a numpy array in RGB format
# data = np.asarray(Image.open(imgpath).convert('RGBA')) # int

# data = data.ravel()
# # Save the contents of a variable to a file
# np.savetxt(datapath, data)

# # # Load a file into a numpy array
# # data = np.loadtxt(datapath).astype(np.uint8) # Since PNG already in uint8

# shape_side = int(math.sqrt(data.size / 4))
# # Reshape array into RGBA format
# data = data.reshape(shape_side, shape_side,  4)
# # Create an image from a numpy array
# img = Image.fromarray(data)
# # Save the image to a file
# img.save(resultpath)


# data = nfy.from_png_file(imgpath)
# nfy.to_png_file(data, resultpath)

#----------


# # Load a PNG file into a numpy array in RGB format
# data = np.asarray(Image.open(path).convert('RGBA')) # int
# return data.ravel()


# Load a FITS file into a numpy array
def from_fits(path: Path) -> np.ndarray:
    hdu_list = fits.open(path)
    data = hdu_list[0].data
    hdu_list.close()
    return data

data = from_fits(Path('/home/preller/h/workspace/pypi/manual/numpyfy/tests/files/test.fits'))

print(data)


# Convert a numpy array into a fits image
def to_fits(data, path: Path) -> np.ndarray:
    hdu = fits.PrimaryHDU(data)
    hdu.writeto(path)
    return True

to_fits(data, Path('/home/preller/h/workspace/pypi/manual/numpyfy/tests/files/test2.fits'))
