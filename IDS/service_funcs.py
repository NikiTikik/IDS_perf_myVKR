#!/usr/bin/env python
# -*- coding: utf-8 -*-

# suricata_status()
# suricata_start()
# suricata_stop()
# ids_status()
# ids_start()
# ids_stop()
# calc_integr()

from helper_funcs import exec_bash


class Service_funcs(object):

    def suricata_status(self):
        cmd = "/etc/init.d/suricata status"
        result = exec_bash(cmd, True)
        if "not running" in result:
            return False
        else:
            return True

    def suricata_start(self):
        cmd = "/etc/init.d/suricata start"
        exec_bash(cmd)
        return suricata_status()

    def suricata_stop(self):
        cmd = "/etc/init.d/suricata stop"
        exec_bash(cmd)
        return suricata_status()

    def ids_status(self):
        cmd = "/etc/init.d/ids status"
        result = exec_bash(cmd, True)
        if "not running" in result:
            return False
        else:
            return True

    def ids_start(self):
        cmd = "/etc/init.d/ids start"
        exec_bash(cmd)
        return ids_status()

    def ids_stop(self):
        cmd = "/etc/init.d/ids stop"
        exec_bash(cmd)
        return ids_status()

    def calc_integr(self):
        cmd = "/opt/S-Terra_IDS/bin/integr_ids calc"
        exec_bash(cmd)
