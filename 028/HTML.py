#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib.request

# 得到url的html页面
def GetHtml(url):
    resp=urllib.request.urlopen(url)
    return resp.read()

def ReadMail(oriURL):
    strMails = GetHtml(oriURL).decode('utf-8')
    #print(strMails)

    lstMails = strMails.split("\n")
    #print(lstMails)
    
    while 1:
        item = lstMails.pop()
        if item != '':
            lstMails.append(item)
            break;
    
    return lstMails

def GetFromGitHub():
    url = 'https://raw.githubusercontent.com/breakerthb/PythonStudy/Practice/028/MailList.md'
    return ReadMail(url)

    