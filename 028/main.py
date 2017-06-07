#!/usr/bin/python3
#_*_coding:utf8_*_

import sys
sys.path.append("../Lib")

import Config as config
from Mail import *
import RandomStr
import HTML

import random
import time

def GetRandText():
    try:
        with open('input.txt') as fileIn:
            string = fileIn.read();
            return RandomStr.randomSelect(string, 5000)
    except:
        print("Error : file open error")
        
def GetRandPic():
    try:
        with open('pic.md') as fileIn:
            lstPics = fileIn.read();
            lstPics = lstPics.split("\n")
           
            index = random.randint(0, len(lstPics) - 1)
            #print(index)
            
            ret = '<img src="' + lstPics[index] + '" />'
            return ret
    except:
        print("Error : pic file open error")

def SendOneTime():
    cnt = 0
    lstMails = HTML.GetFromGitHub()
    #print(lstMails)
    
    mail = Mail()
    receivers = []
    receivers.append(config.sendTo)
    
    for mailFrom in lstMails:
        ### Make Mail Content
        subject = RandomStr.GetRandomStr(8)[0]
        content = GetRandText()
        #print(content)
        
        mail_msg = "<p>" + subject + "</p><p>" + content + "</p>"
        
        pic = GetRandPic()
        #print(pic)
        mail_msg = mail_msg + pic
        
        print(mailFrom)
        mail.Init(config.smtpGmailServer, config.smtpGmailPort, mailFrom, config.smtpPwd, mailFrom, receivers)
        ret = mail.Send(mail_msg, subject)
        
        if ret == 1:
            cnt += 1;
    
    return len(lstMails) - cnt
    
def Alive():
    mail = Mail()
    receivers = []
    receivers.append("breakerthb@126.com")
    mail.Init(config.smtpGmailServer, config.smtpGmailPort, config.smtpGmailUser, config.smtpPwd, config.smtpGmailUser, receivers)
    
    mail_msg = """
        <p>I am alive!</p>
        """
    mail.Send(mail_msg, "subject")
    print("I am alive")
    
if __name__=='__main__':
    # Wait for can
    while 1:
         if SendOneTime() == 0:
            break
         print("wait")
         time.sleep(3600)
        
    # Start Send
    cnt = 0
    while 1:
        cnt += 1
        print("\n----- ----- -----\nSend %s times\n" % cnt)
        if SendOneTime() > 2:
            break
        
        if cnt % 500 == 1:
            Alive()

        time.sleep(4)
    
    print("Send : " + cnt)    