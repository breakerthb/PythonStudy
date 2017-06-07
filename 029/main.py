#!/usr/bin/python3
#_*_coding:utf8_*_

import sys
sys.path.append("../Lib")

from Mail import *


if __name__=='__main__':
    try:
        with open('mail.txt') as fileIn, open('out.txt', "w") as fileOut:
            line = fileIn.readline()
            while line:
                print(line)
                (name, pw) = line.split()
                #print(name)
                #print(pw)
                mail = Mail()
                mail.Init('smtp.gmail.com', '587', name, pw, name, '')
                ret = mail.Check()
                if ret == 1:
                    fileOut.write(name + " " + pw)
                    print("%s - %s" % (name, pw))
                else:
                    print("Invalid")
                
                line = fileIn.readline()
    except:
        print("Error")
