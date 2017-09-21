#!/usr/bin/env python3

from PIL import Image

def parse(f):
    img = Image.open(f)
    pix = img.convert("RGB").load()
    x_size, y_size = img.size[0], img.size[1]

    result = str()
    for x in range(x_size):
        result += chr(sum([1 for y in range(y_size) if pix[x, y] == (255, 0, 0)]))
    return result

print(parse("6c09e7b9cb58b1d939845d68fccd0b1a5d466a32_mission_15_leak.png"))
