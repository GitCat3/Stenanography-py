from PIL import Image


image_to_open = input("input image: ")

hiddentext = input("Text to hide: ") + '\x00'
hiddentextbits = [int(b) for b in ''.join(format(ord(c), '08b') for c in hiddentext)]

image = Image.open(image_to_open)
pixel_data = list(image.get_flattened_data())
new_pixel_data = []

for x in range(len(pixel_data)):
    if x < len(hiddentextbits):
        r, g, b, a = pixel_data[x]
        
        rgb_int = int.from_bytes(bytes([r, g, b]), 'big')
        
        if hiddentextbits[x] == 0:
            rgb_int = rgb_int & ~1
        else:
            rgb_int = rgb_int | 1
        
        rgb_bytes = rgb_int.to_bytes(3, 'big')
        new_pixel_data.append((rgb_bytes[0], rgb_bytes[1], rgb_bytes[2], a))
    else:
        new_pixel_data.append(pixel_data[x])

image.putdata(new_pixel_data)
image.save(f'newfile.png')