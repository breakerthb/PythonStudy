#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re
import urllib2

def GetHtml(url):
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    return response.read()

def ReadURL(oriURL):
    html = GetHtml(oriURL)

    Imageurl(html)  # 输出Data

    return 0

def Imageurl(data):
    re_Imageurl = re.compile(r'src="(http://imgsrc.baidu.com/forum/.*?)"')
    data = re_Imageurl.findall(data)  # 输出图片链接
    
    downloadImage(data)

def downloadImage(pic_url):
    dirct = 'pics'
    try:
        if not os.path.exists(dirct):  # 创建存放目录
            os.mkdir(dirct)
    except:
        print('Failed to create directory in %s' % dirct)
        exit()

    for i in pic_url:
        request = urllib2.Request(i)
        data = urllib2.urlopen(request).read()
        print(i)
        i = re.split('/', i)[-1]
        print(i)
        
        path = dirct + '/' + i
        f = open(path, 'wb')
        f.write(data)
        f.close()
        
    print('Done !')

if __name__ == '__main__':
    #url = 'http://tieba.baidu.com/p/2166231880'
    url = 'http://tieba.baidu.com/p/1787902805?pn=2'
    ReadURL(url)