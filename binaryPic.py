from PIL import Image
import numpy as np
import glob
from utils import reset_folder


def binfile_to_pics(bin_filename: str):
    with open(bin_filename, 'rb') as file:
        file_contents = file.read()

    file_contents = file_contents.decode("utf-8")
    img = Image.new('RGB', (480, 360))

    pixels = img.load()
    x = y = 0
    count = 0
    reset_folder("video")

    for z in file_contents:
        if z == '1':
            pixels[x, y] = (0, 0, 0)
        else:
            pixels[x, y] = (255, 255, 255)
        x += 1
        if x == 480:
            x = 0
            y += 1
            if y == 360:
                img.save(f'video/outputvideo{count}.png')
                x = 0
                y = 0
                count += 1


def read_binary_pics():
    string_binary = ''
    for z in range(len(glob.glob("videoout/*.png"))):
        filename = f"videoout/frame_{z}.jpg"
        img = Image.open(filename)
        width, height = img.size
        for y in range(height):
            for x in range(width):
                color = img.getpixel((x, y))
                if color == (0, 0, 0):
                    string_binary += '1'
                else:
                    string_binary += '0'

    bytes_binary = bytes(string_binary, 'utf-8')
    with open("restore_file.bin", 'wb') as test:
        test.write(bytes_binary)



