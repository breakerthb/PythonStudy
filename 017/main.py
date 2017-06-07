#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xlrd, codecs
from lxml import etree
from collections import OrderedDict

def ReadXLS(filename):
    data = xlrd.open_workbook(filename)
    sheet = data.sheets()[0]
    dictSheet = OrderedDict()
    for i in range(sheet.nrows):
        dictSheet[sheet.cell(i, 0).value] = sheet.row_values(i)[1:]
    return dictSheet

def save_xml(data):
    output = codecs.open('student.xml', 'w', 'utf-8')
    root = etree.Element('root')
    student_xml = etree.ElementTree(root)
    student = etree.SubElement(root, 'student')
    
    student.append(etree.Comment('学生信息表\n\"id\": [名字，数学，语文，英语]'))
    student.text = str(data)
    
    output.write(etree.tounicode(student_xml.getroot()))
    output.close()

if __name__ == '__main__':
    file = 'student.xls'
    xls = ReadXLS(file)
    save_xml(xls)