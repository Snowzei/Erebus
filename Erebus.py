import argparse
import sys
from PIL import Image


def cut_image(image_file, quater=False):
    """
    Cut an image file into half or quarters and save the sections as new files.

    Parameters:
    - image_file (str): The file path of the image to be cut.
    - quater (bool, optional): The type of cut to be performed. If true, cut into quaters. If not, cut into halves.

    Returns:
    None
    """
    # Open the image file
    try:
        image = Image.open(image_file)
        image = image.convert('RGB')
    except IOError:
        print("Error opening image file")
        sys.exit()

    # Get the size of the image
    width, height = image.size

    # Cut the image into half or quarters
    if quater:
        # Cut the image into quarters
        left_top = image.crop((0, 0, width//2, height//2))
        right_top = image.crop((width//2, 0, width, height//2))
        left_bottom = image.crop((0, height//2, width//2, height))
        right_bottom = image.crop((width//2, height//2, width, height))

        # Save the quarters as new image files
        left_top.save(f"{image_file.split('.')[0]}_top_left.jpg")
        right_top.save(f"{image_file.split('.')[0]}_top_right.jpg")
        left_bottom.save(f"{image_file.split('.')[0]}_bottom_left.jpg")
        right_bottom.save(f"{image_file.split('.')[0]}_bottom_right.jpg")
    else:
        # Cut the image into half
        left = image.crop((0, 0, width//2, height))
        right = image.crop((width//2, 0, width, height))

        # Save the halves as new image files
        left.save(f"{image_file.split('.')[0]}_left.jpg")
        right.save(f"{image_file.split('.')[0]}_right.jpg")

    # Close the image file
    image.close()


def main():
    # Set up the argument parser
    parser = argparse.ArgumentParser(
        description="Cut an image file into half or quarters and save the sections as new files.")
    parser.add_argument(
        "image_file", help="The file path of the image to be cut.")
    parser.add_argument("-q", "--quarter", action='store_true',
                        help="Perform a quarter cut instead of a half cut.")

    # Parse the arguments
    args = parser.parse_args()
    image_file = args.image_file
    cut_type = args.quarter

    # Cut the image
    cut_image(image_file, cut_type)


# Run the main function
if __name__ == "__main__":
    main()
