#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from collections import OrderedDict
from openpyxl import Workbook

def txt2xlsx(filename):
    file = open(filename, 'r')
    file_content = json.load(file, encoding = 'UTF-8')
    print(file_content)
    
    workbook = Workbook()
    worksheet = workbook.worksheets[0]
    
    for i in range(1, len(file_content) + 1):
        print("i : %s" % i)
        for m in range(1, len(file_content[i - 1]) + 1):
            print("m : %s" % m)
            worksheet.cell(row = i, column = m).value = file_content[i - 1][m - 1]
        print("\n")
        
    workbook.save(filename = 'numbers.xls')

if __name__ == '__main__':
    txt2xlsx('numbers.txt')