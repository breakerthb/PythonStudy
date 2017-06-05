#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import glob
from PIL import Image

def thumbnail_pic(path):
    pics = glob.glob(r'*.jpg')
    for pic in pics:
        name = os.path.join(path, pic)
        
        im = Image.open(name)
        im.thumbnail((1136, 640))
        print(im.format, im.size, im.mode)
        im.save("result.jpg", 'JPEG')
    print('Done!')

if __name__ == '__main__':
    path = '.'
    thumbnail_pic(path)