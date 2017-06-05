#!/usr/bin/env python
# -*-coding:utf-8-*-

import string
import random
import redis

KEY_LEN = 20
KEY_ALL = 200


def base_str():
    return (string.letters + string.digits)


def key_gen():
    keylist = [random.choice(base_str()) for i in range(KEY_LEN)]
    return ("".join(keylist))


def key_num(num, result=None):
    if result is None:
        result = []
    for i in range(num):
        result.append(key_gen())
    return result


def redis_init():
    r = redis.Redis(host='localhost', port=6379, db=0)
    return r


def push_to_redis(key_list):
    for key in key_list:
        redis_init().lpush('keys', key)


def get_from_redis():
    key_list = redis_init().lrange('keys', 0, -1)
    for key in key_list:
        print key

if __name__ == "__main__":
    push_to_redis(key_num(200))
    get_from_redis()