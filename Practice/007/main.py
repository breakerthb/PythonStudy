#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re

def count_num(path, file):
    arrCnts = [0, 0, 0]
    path = os.path.join(path, file)
    
    lines = open(path, 'r').readlines()
    
    # 统计注释
    for line in lines:
        if re.match(r'^\/*', line) == None:                          
            pass
        else:
            print(line)
            arrCnts[1] += 1  #获得注释行数，只匹配单行注释
            
    # 统计空行
    if lines[-1][-1:] == '\n':         #最后一行为空行时
        arrCnts[2] = lines.count('\n') + 1                     #获得空行行数
        arrCnts[0] = len(lines) + 1 - arrCnts[2] - arrCnts[1]  #获得代码行数
    else:
        arrCnts[2] = lines.count('\n')
        arrCnts[0] = len(lines) - arrCnts[2] - arrCnts[1]
    
    return arrCnts

def file_analysis(path, ext):
    files = [x for x in os.listdir(path) if os.path.splitext(x)[1]==ext]    #获得文件列表
    print(files)
    
    the_num = [0, 0, 0]
    for file in files:
        num = count_num(path, file)
        the_num[0] += num[0]                #累计
        the_num[1] += num[1]
        the_num[2] += num[2]
    print('''统计得目录中：
             代码有 %s 行
             注释 %s 行
             空行 %s 行''' % (the_num[0], the_num[1], the_num[2]))

if __name__ == '__main__':
    path = '.'
    ext = '.c'
    file_analysis(path, ext)