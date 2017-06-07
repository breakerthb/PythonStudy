#!/usr/bin/python3
#_*_coding:utf8_*_

import Config as config
from Mail import *

if __name__=='__main__':
    mail = MyMail()
    receivers = []
    receivers.append("breakerthb@126.com")
    mail.Init(config.smtpServer, config.smtpPort, config.smtpUser, config.smtpPwd, config.smtpUser, receivers)

    mail_msg = """
        <p>I am alive!</p>
        """
    
    mail.Send(mail_msg, "subject")