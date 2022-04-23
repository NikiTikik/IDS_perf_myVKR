#!/usr/bin/env python
# -*- coding: utf-8 -*-

# exec_bash(cmd, read=False)

from subprocess import Popen, PIPE


def connectSSH():
    SSH_conn = SSH2()
    SSH_conn.connect(SSH_HOST)
    SSH_conn.login(account)
    return SSH_conn


def getResponse(SSH_conn, sendCommand):
    SSH_conn.execute(sendCommand)
    return SSH_conn.response


def closeSSH(SSH_conn):
    SSH_conn.close(force=True)


def restartSSH(SSH_conn):
    closeSSH(SSH_conn)
    SSH_conn = connectSSH()


def exec_bash(cmd, read=False):
    if read:
        result = Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE).stdout.read()
        return result
    else:
        Popen(cmd, shell=True, executable='/bin/bash').wait()
        return True
