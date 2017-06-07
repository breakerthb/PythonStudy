#! /usr/bin/env python3
#! -*- coding:utf-8 -*-

import RandomStr

if __name__ == '__main__':
    for i in range(10):
        lst = RandomStr.GetRandomStr(8)
        print(lst[0])