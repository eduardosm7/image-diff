"""
Image diff
"""

from PIL import Image
import argparse
import os


def get_args() -> None:
    """
    Gets args from user
    """
    
    parser = argparse.ArgumentParser("Gets the difference between two images.")

    parser.add_argument('image1', help="Image 1")
    parser.add_argument('image2', help="Image 2")
    parser.add_argument('-t', '--threshold', type=int, default=0, 
                        help="Threshold between pixel difference")
    parser.add_argument('-p', '--path', type=str, default="output.png", 
                        help="Path to store output image")

    return parser.parse_args() 


def compare(image1: str, image2: str, threshold: int) -> []:
    """
    Compares Image1 and Image2 and return a array containing the difference
    """

    img1 = Image.open(image1)
    img2 = Image.open(image2)
    
    pixels1 = list(img1.getdata())
    pixels2 = list(img2.getdata())

    img1.close()
    img2.close()

    diff = lambda x, y: True if abs(max([a - b for a, b in zip(x, y)])) > threshold else False

    return [p2 if diff(p1, p2) else (0, 0, 0) for p1, p2 in zip(pixels1, pixels2)]


def get_size(image1: str, image2: str) -> int:
    """
    Gets images size and validates it's the same
    """

    img1 = Image.open(image1)
    img2 = Image.open(image2)

    if img1.size != img2.size:
        print("Both images have to be the same size.")
        sys.exit(1)
    
    img1.close()
    img2.close()

    return img1.size


def save(array: [], size: int, path: str) -> None:
    """
    Saves output image
    """

    output_image = Image.new('RGB', size)
    output_image.putdata(array)
    output_image.save(path)

def main() -> None:

    args = get_args()

    size = get_size(args.image1, args.image2)

    diff_array = compare(args.image1, args.image2, args.threshold)

    save(diff_array, size, args.path)


if __name__ == "__main__":
    main()