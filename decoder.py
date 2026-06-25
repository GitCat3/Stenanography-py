from PIL import Image

def rgb2hex(r, g, b):
    return "{:02x}{:02x}{:02x}".format(r, g, b)

image_to_open = input("path to image: ")

image = Image.open(image_to_open)
pixel_data = list(image.get_flattened_data())

char_list = ""
int_list = ""
counter = 1

for pixel in pixel_data:
    r, g, b, a = pixel
    rgb_int = int.from_bytes(bytes([r, g, b]), 'big')
    lsb = str(rgb_int & 1)
    int_list += lsb
    if counter == 8:
        char = chr(int(int_list, 2))
        char_list += char
        if char == '\x00':
            break
        int_list = ""
        counter = 1
    else:
        counter += 1

print(f"Decoded message: {char_list}")