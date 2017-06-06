#!/usr/bin/python3
#_*_coding:utf8_*_
 
import smtplib
from email.mime.text import MIMEText
from email.header import Header
 
class MyMail:
    def __init__(self):
        self.subject = ""
 
    def Init(self, host, port, user, pw, sender, receivers):
        self.host = host    #设置服务器
        self.port = port
        self.user = user    #用户名
        self.pw = pw        #口令 
        self.sender = sender
        self.receivers = receivers  # 接收邮件 ['23456789@qq.com']
        
    def Send(self, msg, subject):
        message = MIMEText(msg, 'plain', 'utf-8')
        message['From'] = Header(self.sender, 'utf-8')
        message['To'] =  Header(self.receivers[0], 'utf-8')
        message['Subject'] = Header(subject, 'utf-8')
 
        print(message)
 
        try:
            smtpObj = smtplib.SMTP()
            print("connect : %s : %s" % (self.host, self.port))
            smtpObj.connect(self.host, self.port)
            smtpObj.starttls() #####
            print("start login : %s - %s" % (self.user, self.pw))
            smtpObj.login(self.user, self.pw)
            print("start send")
            smtpObj.sendmail(self.sender, self.receivers, message.as_string())
            print ("邮件发送成功")
        except smtplib.SMTPException as e:
            print ("Error: 无法发送邮件")
            print (e)
