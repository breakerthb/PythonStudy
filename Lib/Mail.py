#!/usr/bin/python3
#_*_coding:utf8_*_
 
import smtplib
from email.mime.text import MIMEText
from email.header import Header
 
class Mail:
    def __init__(self):
        self.subject = ""
    
    # Init parameters
    def Init(self, host, port, user, pw, sender, receivers):
        self.host = host    #设置服务器
        self.port = port
        self.user = user    #用户名
        self.pw = pw        #口令 
        self.sender = sender
        self.receivers = receivers  # 接收邮件 ['23456789@qq.com']
    
    # Check password
    def Check(self):
        try:
            #print("----> Connect Mail Server : %s : %s" % (self.host, self.port))
            smtpObj = smtplib.SMTP(host=self.host, port=self.port)
            smtpObj.ehlo()
            smtpObj.starttls()
            #print("----> login : %s - %s" % (self.user, self.pw))
            smtpObj.login(self.user, self.pw)
            return 1
        except smtplib.SMTPException as e:
            print(e)
            return 0
        else:
            smtpObj.close()
        
    def Send(self, msg, subject):
        #message = MIMEText(msg, 'plain', 'utf-8')
        message = MIMEText(msg, 'html', 'utf-8')
        message['From'] = Header(self.sender, 'utf-8')
        message['To'] =  Header(self.receivers[0], 'utf-8')
        message['Subject'] = Header(subject, 'utf-8')
 
        #print("Message : \n" + str(message))
 
        try:
            '''
            smtpObj = smtplib.SMTP()
            smtpObj.connect(self.host, self.port)
            print("-> connect success")
            '''
            #print("----> Connect Mail Server : %s : %s" % (self.host, self.port))
            smtpObj = smtplib.SMTP(host=self.host, port=self.port)
            #smtpObj.set_debuglevel(1)
            smtpObj.ehlo()
            smtpObj.starttls()
            #print("----> login : %s - %s" % (self.user, self.pw))
            smtpObj.login(self.user, self.pw)
            #print("----> start send")
            smtpObj.sendmail(self.sender, self.receivers, message.as_string())
            print ("Send Success!")
            return 1
        except smtplib.SMTPHeloError as e:
            print(e)
            return 0
        except smtplib.SMTPException as e:
            print("Error: Send Failed")
            print(e)
            return 0
        else:
            smtpObj.close()
