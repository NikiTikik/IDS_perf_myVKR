#!/usr/bin/env python
# -*- coding: utf-8 -*-

# count_total_events(start_time=start_time, end_time=end_time)
# count_uniq_events(start_time=start_time, end_time=end_time)
# last_cid()

import datetime
import sys
import MySQLdb as mdb
import time

BD_CONFIG = {
      'host': '127.0.0.1',
      'db': 'barnyard2',
      'passwd': 'russia',
      'user': 'root',
      'port': 3306
    }


class BD_funcs(object):

    start_time = datetime.datetime(1900, 1, 1, 1, 1)
    end_time = datetime.datetime(2100, 1, 1, 1, 1)

    def count_total_events(self, start_time=start_time, end_time=end_time):
        db_connect = mdb.connect(**BD_CONFIG)
        cur = db_connect.cursor()

        query = 'SELECT COUNT(cid) FROM event '
        'WHERE timestamp BETWEEN "%s" AND "%s";' % (start_time.strftime('%Y-%m-%d %H:%M:%S'), end_time.strftime('%Y-%m-%d %H:%M:%S'))
        cur.execute(query)
        count_total = cur.fetchone()[0]

        cur.close()
        db_connect.close()

        return count_total

    def count_uniq_events(self, start_time=start_time, end_time=end_time):
        db_connect = mdb.connect(**BD_CONFIG)
        cur = db_connect.cursor()

        query = 'SELECT COUNT(DISTINCT signature) FROM event;'
        'WHERE timestamp BETWEEN "%s" AND "%s";' % (start_time.strftime('%Y-%m-%d %H:%M:%S'), end_time.strftime('%Y-%m-%d %H:%M:%S'))
        cur.execute(query)
        count = cur.fetchone()[0]

        cur.close()
        db_connect.close()

        return count

    def last_cid(self):
        db_connect = mdb.connect(**BD_CONFIG)
        cur = db_connect.cursor()

        query = "SELECT MAX(cid) from event;"
        cur.execute(query)
        last_c = cur.fetchall()[-1]

        cur.close()
        db_connect.close()

        return last_c[0]

    def barnyard2_finish(self):
        a = last_cid()
        time.sleep(5)
        b = last_cid()
        if a == b:
            return True
        else:
            return False


def last_cid():
        db_connect = mdb.connect(**BD_CONFIG)
        cur = db_connect.cursor()

        query = "SELECT MAX(cid) from event;"
        cur.execute(query)
        last_c = cur.fetchall()[-1]

        cur.close()
        db_connect.close()

        return last_c[0]

"""
print(count_total_events())
print(count_uniq_events())
"""


# def last_cid():
#     db_connect = mdb.connect(**BD_CONFIG)
#     cur = db_connect.cursor()

#     query = "SELECT MAX(cid) from event;"
#     cur.execute(query)
#     last_c = cur.fetchall()[-1]

#     cur.close()
#     db_connect.close()

#     return last_c[0]

# print(last_cid())
