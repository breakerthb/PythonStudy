#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re

def filter_word(word):
    f = open('filter_words.txt', 'r').read()
    
    if word == '':
        print('Human Rights !')  
    elif len(re.findall(r'%s' % (word), f)) == 0:
        print('Human Rights !')    #非敏感词时，则打印出 Human Rights !
    else:
        print('Freedom !')         #输入敏感词语打印出 Freedom !


str = raw_input('请输入词语：')
filter_word(str)