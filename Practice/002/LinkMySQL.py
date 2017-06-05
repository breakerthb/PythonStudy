#!/usr/bin/env python
# -*-coding:utf-8-*-

import MySQLdb

class MySQLLink(object):

    def __init__(self, conn):
        self.conn = None

    # connect to mysql
    def connect(self):
        self.conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user="root",
            passwd="",
            db="TESTDB",
            charset="utf8"
        )

    def cursor(self):
        try:
            return self.conn.cursor()
        except (AttributeError, MySQLdb.OperationalError):
            self.connect()
            return self.conn.cursor()

    def commit(self):
        return self.conn.commit()

    def close(self):
        return self.conn.close()