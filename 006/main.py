#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import glob
from collections import OrderedDict

def get_num(key_word, filename):
    '''获得词汇出现次数'''
    str = open(filename, 'r').read()
    re_zhengze = re.compile(r'[\s\,\;\.\n]{1}'+key_word+r'[\s\,\;\.\n]{1}')
    numbers = re_zhengze.findall(str)
    return len(numbers)

def article_analysis(path):
    files = glob.glob(r'*.txt')
    dictdata = OrderedDict()
    
    for file in files:
        str = open(file, 'r').read()
        words = re.findall("\b?([a-zA-Z]+)\b?", str)   #获得单词list

        for word in words:
            dictdata[word] = get_num(word, file)
            
        dict = OrderedDict(sorted(dictdata.items(), key=lambda x: x[1], reverse = True))   #dict排序
        print('在 %s 中出现次数最多的单词是：' % file)
       
        # 打印第一个元素
        for item in dict:
            print(item + ' : %s 次' % dict[item])
            break
        
    return 0

if __name__ == '__main__':
    path = '.'
    article_analysis(path)