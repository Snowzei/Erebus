# Erebus

This Python script takes an image file and cuts it into half or quarters, saving the sections as new image files.

The requirements for this script are:

``
    Python 3
``

``
    Pillow (Python Imaging Library)
``

To easily get the libraries needed, run this command:

`` pip install -r requirements.txt ``

## Usage

To use the script, run the following command:

`` python Erebus.py image_file -q ``

Replace image_file with the file path of the image to be cut, and the -q flag for the type of cut, -q for a quarter cut. The flag is optional; if not specified, the image will be cut into halves.
Examples

To cut an image called "image.jpg" into halves:

`` python Erebus.py image.jpg ``

To cut the image into quarters:

`` Erebus.py image.jpg -q ``

## Output

The script will save the sections of the image as new image files with the original image file name and either "left", "right", "top_left", "top_right", "bottom_left", or "bottom_right".
Notes

##### The script uses the Python Imaging Library (PIL) to open and manipulate the image file.
##### The script will exit if it encounters an error when opening the image file.
