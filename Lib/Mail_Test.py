#!/usr/bin/python3
#_*_coding:utf8_*_

from Mail import *

smtpGmailServer='smtp.gmail.com'
smtpGmailPort='587'
smtpGmailUser='tomtom55731@gmail.com'
smtpPwd='qetuo_159357^' 
sendTo='breakerthb@126.com'

if __name__=='__main__':
    mail = Mail()
    receivers = []
    receivers.append(sendTo)
    mail.Init(smtpGmailServer, smtpGmailPort, smtpGmailUser, smtpPwd, smtpGmailUser, receivers)

    mail_msg = """
        <p>I am alive!</p>
        """
    
    mail.Send(mail_msg, "subject")