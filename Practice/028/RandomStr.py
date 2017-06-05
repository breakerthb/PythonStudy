#! /usr/bin/env python3
#! -*- coding:utf-8 -*-

import random, string

def randomSequence(num, length):
    letters = string.ascii_letters + string.digits + '@#$%&*'
    random_seq = []

    lstLetters = list(letters)
    # print(lstLetters)
    for i in range(num):
        random.shuffle(lstLetters)
        random_seq.append(''.join(lstLetters[:length]))
    return random_seq

def GetRandomStr(length):
    return randomSequence(1, length)
