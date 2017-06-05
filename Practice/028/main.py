#!/usr/bin/python3
#_*_coding:utf8_*_

import Config as config
from Mail import *
import RandomStr

if __name__=='__main__':
    mail = MyMail()
    receivers = []
    receivers.append(config.sendTo)
    mail.Init(config.smtpServer, config.smtpUser, config.smtpPwd, config.smtpUser, receivers)
    
    mail_msg = """
        <p>Python 邮件发送测试...</p>
        <p><a href="http://www.runoob.com">这是一个链接</a></p>
        """
    
    subject = RandomStr.GetRandomStr(8)[0]
    
    mail.Send(mail_msg, subject)