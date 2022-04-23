#!/usr/bin/env python
# -*- coding: utf-8 -*-

# exec_bash(cmd, read=False)
# connect_SSH()
# getResponse(SSH_conn, sendCommand)
# close_SSH(SSH_conn)
# restart_SSH(SSH_conn)


from subprocess import Popen, PIPE

from Exscript.util.interact import read_login
from Exscript.protocols import SSH2
from Exscript.protocols import Exception
from Exscript import Host, Account

'''
SSH_HOST = '10.0.223.112'
USERNAME = 'root'
PASSWORD = 'russia'
account = Account(USERNAME, PASSWORD)
'''


def connect_SSH(host, account):
    SSH_conn = SSH2()
    SSH_conn.connect(host)
    SSH_conn.login(account)
    return SSH_conn


def get_SSH_response(SSH_conn, sendCommand):
    SSH_conn.execute(sendCommand)
    return SSH_conn.response


def get_SSH_send(SSH_conn, sendCommand):
    SSH_conn.send(sendCommand)
    return SSH_conn.send


def close_SSH(SSH_conn):
    SSH_conn.close(force=True)


def restart_SSH(SSH_conn):
    close_SSH(SSH_conn)
    SSH_conn = connect_SSH()


def exec_bash(cmd, read=False):
    if read:
        result = Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE).stdout.read()
        return result
    else:
        Popen(cmd, shell=True, executable='/bin/bash').wait()
        return True

'''
def run_tcpreplay(speed, loop, filename):
    conn = connect_SSH()
    cmd = 'tcpreplay -i eth1 --mbps "%s" --loop "%s" --stats=3 --unique-ip "%s"' % (speed, loop, filename)
    output = get_SSH_response(conn, cmd)
    print(output)
    close_SSH(conn)


def run_ping(number):
    conn = connect_SSH()
    cmd = 'ping -i 0.009 -c "%s" -I eth1 10.0.223.111' % (number)
    output = get_SSH_response(conn, cmd)
    print(output)
    close_SSH(conn)


run_tcpreplay(400, 1, "out_dump.pcap")
run_ping(100)

conn = connect_SSH()
cmd = "ping 127.0.0.1 -c 4"
output = get_SSH_response(conn, cmd)
print(output)
close_SSH(conn)
'''