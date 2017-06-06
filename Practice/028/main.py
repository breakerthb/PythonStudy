#!/usr/bin/python3
#_*_coding:utf8_*_

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
            return RandomStr.randomSelect(string, 500)
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
    lstMails = HTML.GetFromGitHub()
    
    mail = MyMail()
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
        mail.Init(config.smtpServer, config.smtpPort, mailFrom, config.smtpPwd, mailFrom, receivers)
        mail.Send(mail_msg, subject)
    
    
def Alive():
    mail = MyMail()
    receivers = []
    receivers.append("breakerthb@126.com")
    mail.Init(config.smtpServer, config.smtpPort, config.smtpUser, config.smtpPwd, config.smtpUser, receivers)
    
    mail_msg = """
        <p>I am alive!</p>
        """
    mail.Send(mail_msg, "subject")
    print("I am alive")
    
if __name__=='__main__':
    cnt = 0
    while 1:
        cnt += 1
        print("\n----- ----- -----\nSend %s times\n" % cnt)
        SendOneTime()
        
        if cnt % 1800 == 1:
            Alive()
            #cnt = 0
        
        time.sleep(1)
        