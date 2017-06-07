#! /usr/bin/env python
#! -*- coding:utf-8 -*-

from PIL import Image, ImageDraw, ImageFont


def add_num(imgIn, num, imgOut):
    image = Image.open(imgIn)

    draw = ImageDraw.Draw(image)
    # myfont = ImageFont.truetype('C:/windows/fonts/Arial.ttf', size=50)
    myfont = ImageFont.truetype('arial.ttf', size=50)
    fillcolor = "#ff0000"
    width, height = image.size
    draw.text((width - 40, 0), str(num), font=myfont, fill=fillcolor)
    image.save(imgOut, 'jpeg')

    return 0


if __name__ == '__main__':
    add_num('1.jpg', 5, 'result.jpg')