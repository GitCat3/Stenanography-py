import zlib

hiddentext = input("Text to hide: ")
hiddentextbits = ''.join(format(ord(char), '08b') for char in hiddentext)
hiddentextbits = [int(digit) for digit in str(hiddentextbits)]

with open("..\\..\\Downloads\\tropical-frond-green-palm-leaf-tree-on-transparent-background-file-free-png-1958460337.png", 'rb') as file:
    file = file.read()
    image_data = file.split(bytearray.fromhex("49444154"), 1)[1]
    image_data = bytearray(image_data[:len(image_data)-16])

    for x in range(0, len(image_data)):
        if hiddentextbits[x] == 0:
            image_data[x] = image_data[x] & ~1
        else:
            image_data[x] = image_data[x] | 1

        if x == len(hiddentextbits)-1:
            break

    header_data = file.split(bytearray.fromhex("49444154"))[0] + bytearray.fromhex("49444154")
    image_data.extend((zlib.crc32(image_data) & 0xFFFFFFFF).to_bytes(4))
    end_data = file[-12:]
    new_file = header_data + image_data + end_data
    with open("newfile.png", "wb") as newfile:
        newfile.write(new_file)
