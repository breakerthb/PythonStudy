#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re

def filter_word(a):
    sensitive = False
    strs = '**'
    f = open('filter_words.txt', 'r').readlines()
    for i in f: 
        i = i.strip()                                               #去除\n
        b = re.split(r'%s' % (i), a)                                #分解字符串
        if len(b) > 1:
            c = i
            sensitive = True   
        else:
            pass
        
    if sensitive == True:
        b = re.split(r'%s' % (c.strip()), a)
        print(strs.join(b))
    else:
        print(a)
    return 0

z = raw_input('请输入：')
filter_word(z)