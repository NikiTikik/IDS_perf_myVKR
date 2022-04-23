#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import Pyro4

from threading import Thread

from helper_funcs import connect_SSH, get_SSH_response, close_SSH, restart_SSH

from Exscript.util.interact import read_login
from Exscript.protocols import SSH2
from Exscript.protocols import Exception
from Exscript import Host, Account

SSH_HOST = '10.0.223.112'
SSH_IDS = '10.0.223.111'
USERNAME = 'root'
PASSWORD = 'russia'
ACCOUNT = Account(USERNAME, PASSWORD)


def connect_via_Pyro(obj):
    uri = "PYRO:%s@10.0.223.111:9999" % obj

    # get a Pyro proxy to the object
    conn = Pyro4.Proxy(uri)
    return conn


class universalThread(Thread):

    def __init__(self, f, **kwargs):
        Thread.__init__(self)
        self.f = f
        self.args = kwargs

    def run(self):
        self.f(**self.args)


def run_tcpreplay(speed, loop, filename):
    print('_____tcpreplay_start____')
    conn = connect_SSH(SSH_HOST, ACCOUNT)
    cmd = 'tcpreplay -i eth1 --mbps "%s" --loop "%s" --stats=3 --unique-ip "%s"' % (speed, loop, filename)
    output = get_SSH_response(conn, cmd)
    # print(output)
    close_SSH(conn)
    print('_____tcpreplay_stop_____')


def run_ping(number):
    print('_____ping_start_________')
    conn = connect_SSH(SSH_HOST, ACCOUNT)
    time.sleep(2)
    cmd = 'ping -i 0.009 -c "%s" -I eth1 10.0.223.111' % (number)
    output = get_SSH_response(conn, cmd)
    # print(output)
    close_SSH(conn)
    print('_____ping_stop__________')


def run_parallel(f1, f1_args, f2, f2_args):
    T_thread = universalThread(f1, **f1_args)
    P_thread = universalThread(f2, **f2_args)

    P_thread.setDaemon(True)
    T_thread.setDaemon(True)

    T_thread.start()
    P_thread.start()

    T_thread.join()
    P_thread.join()

    time.sleep(3)

"""
def run_pyro_server():
    conn = connect_SSH(SSH_HOST, ACCOUNT)
    cmd = 'python /perf_scripts/pyro_server.py'
    close_SSH(conn)
"""
