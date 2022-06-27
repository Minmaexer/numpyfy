import math
import numpy as np
from astropy.io import fits
from PIL import Image
from pathlib import Path

def test_default():
    return True

def from_png_file(path: Path) -> np.ndarray:
    """
    Converts a PNG file (in RGB or RGBA format) to a 1-D numpy array.

    Args:
        path (Path): path to the PNG file.

    Returns:
        np.ndarray: numpy array of the PNG file.
    """

    # Load a PNG file into a numpy array in RGB format
    data = np.asarray(Image.open(path).convert('RGBA')) # int
    return data.ravel()

def to_png_file(data: np.ndarray, target_path: Path) -> bool:
    """Converts a numpy array to a PNG file (RGBA) and stores it into a file.

    Args:
        data (np.ndarray): numpy array to convert.
        target_path (Path): path to the PNG file.

    Returns:
        bool: True if successful, False otherwise.
    """
    
    #TODO Flag for RGB or RGBA format for /3 or /4
    # Load a file into a numpy array
    shape_side = int(math.sqrt(data.size / 4))
    # Reshape array into RGBA format
    data = data.reshape(shape_side, shape_side,  4)
    # Create an image from a numpy array
    img = Image.fromarray(data)
    # Save the image to a file
    img.save(target_path)
    return True


# Convert a fits file into a numpy array
def from_fits(path: Path) -> np.ndarray:
    """Converts a fits file into a numpy array.

    Args:
        path (Path): path to the fits file.

    Returns:
        np.ndarray: numpy array of the fits file.
    """
    hdu_list = fits.open(path)
    data = hdu_list[0].data
    hdu_list.close()
    return data

# Convert a numpy array into a fits image
def to_fits(data: np.ndarray, path: Path) -> np.ndarray:
    """Converts a numpy array into a fits file.

    Args:
        data (np.ndarray): numpy array to convert.
        path (Path): path to the fits file.

    Returns:
        np.ndarray: numpy array of the fits file.
    """
    hdu = fits.PrimaryHDU(data)
    hdu.writeto(path)
    return True

# # Convert a JPEG file into a numpy array
# def from_jpeg(path: Path) -> np.ndarray::
#     img = Image.open(path: Path) -> np.ndarray:
#     data = np.array(img)
#     return data

# # Convert a numpy array into a JPEG image
# def to_jpeg(data, filename):
#     img = Image.fromarray(data)
#     img.save(filename)
#     return True

# # Convert a PNG file into a numpy array
# def from_png(filename):
#     img = Image.open(filename)
#     data = np.array(img)
#     return data

# # Convert a numpy array into a PNG image
# def to_png(data, filename):
#     img = Image.fromarray(data)
#     img.save(filename)
#     return True



# Development notes :)
# convert.to.

# class to:
#     @staticmethod 
#     def Bar(x, y):
#         return x + y

#     @staticmethod 
#     def Baz(x, y):
#         return x - y


