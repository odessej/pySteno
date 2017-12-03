"""
Stenography Module.

Allow to stenograph images
"""
# Standard import
from collections import deque

# External import
from PIL import Image

masks = [0, 1, 3, 7, 15, 31, 63, 127]


def bit_and(num1, lt_num):
    """Modify the last bit on the num1.

    Using the most significant of lt_numt[0].
    """
    if not lt_num:
        return num1

    if lt_num[0][1] < 0:
        lt_num.popleft()

    if not lt_num:
        return num1

    num1 = (num1 >> 1 << 1) + (lt_num[0][0] >> lt_num[0][1])
    lt_num[0] = (lt_num[0][0] & masks[lt_num[0][1]], lt_num[0][1] - 1)
    return num1


def modify_pixel(pixel, data):
    """Modify pixel with data."""
    red = bit_and(pixel[0], data)
    green = bit_and(pixel[1], data)
    blue = bit_and(pixel[2], data)
    return (red, green, blue)


def iter_image_pixels(img, pixel_values, data, func_hide=modify_pixel):
    """
    Iterate through the image, apply function provided to each pixel.

    Will continue until no data is left
    """
    for x in range(0, img.size[0]):        # width
        for y in range(0, img.size[1]):    # height
            if not data:
                return
            pixel_values[x, y] = func_hide(pixel_values[x, y], data)


def ret_pixel(pixel):
    """Get data from pixel."""
    return bin(pixel[0])[-1] + bin(pixel[1])[-1] + bin(pixel[2])[-1]


def iter_image_pixels_ret(img, pixel_values, func_ret=ret_pixel):
    """Iterate through the image, get data until the end."""
    data = ''
    for x in range(0, img.size[0]):        # width
        for y in range(0, img.size[1]):    # height
            data += func_ret(pixel_values[x, y])
    return data


def get_data(filepath):
    """Get the data from the file (list of int)."""
    with open(filepath, mode='rb') as file:
        # Convert to list of integers, then binary, join everything
        return deque((x, 7) for x in list(file.read()))


def get_array_image(image_path):
    """Get an array of image."""
    image = Image.open(image_path, 'r')
    pixel_values = image.load()
    return pixel_values, image


def hide_file_in_photo(file_data, photo, output, padding=False, func_hide=modify_pixel):
    """Hide the data in the file."""
    if output is None:
        output = photo

    data = get_data(file_data)
    pixel_values, img = get_array_image(photo)
    calc = (img.size[0] * img.size[1] * 3) - (8 * len(data))
    if calc < 0:
        print("Can't hide file in photo, to much data : %d " % calc)
        return
    elif padding:
        data += [(0, 7) for x in range(0, calc)]

    iter_image_pixels(img, pixel_values, data)
    img.save(output)


def chunks(s, n):
    """Get chunks from container."""
    for start in range(0, len(s), n):
        yield s[start:start+n]


def clean_padding(lt_octets):
    """Remove padding octets at the end of the list."""
    while True:
        val = lt_octets.pop()
        if val != 0:
            lt_octets.append(val)
            return lt_octets
    return lt_octets


def retrieve_file_in_photo(photo, output, func_ret=None):
    """Retrieve the data in the photo."""
    pixel_values, img = get_array_image(photo)
    data = iter_image_pixels_ret(img, pixel_values)
    data = chunks(iter_image_pixels_ret(img, pixel_values), 8)
    data = bytes(clean_padding([int(x, 2) for x in data]))

    if output is None:
        print(data)
    else:
        with open(output, 'wb') as f:
            f.write(data)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='Stenography tool')
    parser.add_argument('-p', '--photo', help='Path to the photo file',
                        required=True)
    parser.add_argument('-m', '--mode', help='Mode (Retrieve or Hide)',
                        required=False)
    parser.add_argument('-o', '--output', help='Specify the name of the output file.',
                        required=True)
    parser.add_argument('-f', '--file', help='Specify the file to take data from.',
                        required=False)
    parser.add_argument('-P', '--padding', help='Pads the data with zeros',
                        required=False, action='store_true')
    args = vars(parser.parse_args())

    if args['mode'].lower() == 'hide':
        if args['file'] is None:
            print("Missing input, specify a file to hide\n")
            import sys
            sys.exit()

        if args['padding'] is None:
            args['padding'] = False

        hide_file_in_photo(args['file'], args['photo'], args['output'], args['padding'])

    elif args['mode'].lower() == 'retrieve':
        if args['file'] is not None:
            retrieve_file_in_photo(args['photo'], args['output'], args['output'])
