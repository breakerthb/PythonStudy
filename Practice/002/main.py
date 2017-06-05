#!/usr/bin/env python
# -*-coding:utf-8-*-

from LinkMySQL import MySQLLink

import string
import random

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
        result.append(str(key_gen()))
    return result

# def execute(sql):
#     '''执行sql'''
#     conn=dbconn.cursor()
#     conn.execute(sql)

# def executemany(sql, tmp):
#     '''插入多条数据'''
#     conn=dbconn.cursor()
#     conn.executemany(sql,tmp)


def query(sql, conn):
    '''查询sql'''
    conn.execute(sql)
    rows = conn.fetchall()
    return rows


def DropTable(conn):
    conn.execute("DROP TABLE IF EXISTS `user_key`")


def CreateTable(conn):
    sql_create = ''' CREATE TABLE `user_key` (`key` varchar(50) NOT NULL)'''
    conn.execute(sql_create)

def InsertDatas(conn):
    insert_sql = "INSERT INTO user_key VALUES (%(value)s)"
    key_list = key_num(KEY_ALL)
    # print len(key_list)
    # conn.executemany(insert_sql,str(key_listi))
    # conn.executemany("INSERT INTO user_key VALUES (%(value)s)",
    #                   [dict(value=v) for v in key_list])
    conn.executemany(insert_sql, [dict(value=v) for v in key_list])


def DeleteData(id):
    del_sql = "delete from user_key where id=" + str(id)
    conn.execute(del_sql)

def PrintResult(rows):
    if rows is None:
        print "rows None"
    for row in rows:
        print row
        
def QueryData(conn):
    sql = "select * from user_key"
    rows = query(sql, conn)
    PrintResult(rows)

if __name__ == "__main__":
    dbconn = MySQLLink(None)
    dbconn.connect()
    
    conn = dbconn.cursor()
    
    DropTable(conn)
    CreateTable(conn)
    InsertDatas(conn)
    QueryData(conn)
    dbconn.close()