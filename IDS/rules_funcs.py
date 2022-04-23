#!/usr/bin/env python
# -*- coding: utf-8 -*-

# disable_all_rules()
# enable_all_rules()
# disable_class(class)
# enable_class(class)
# disable_sid(sid)
# enable_sid(sid)
# ids_rulesreload()

import os
from helper_funcs import exec_bash

# RULES_DIRECTORY = '/etc/suricata/rules/'
RULES_DIRECTORY = '/perf_scripts/rules/'
FILE = 'voip.rules'


class Rules_funcs(object):

    def disable_all_rules(self):
        files = get_filelist()
        for filename in files:
            disable_all_rules_in_file(filename)

    def enable_all_rules(self):
        files = get_filelist()
        for filename in files:
            enable_all_rules_in_file(filename)

    def disable_class(self, clas):
        files = get_filelist()
        for filename in files:
            disable_class_rules_in_file(clas, filename)

    def enable_class(self, clas):
        files = get_filelist()
        for filename in files:
            enable_class_rules_in_file(clas, filename)

    def disable_sid(self, sid):
        files = get_filelist()
        for filename in files:
            disable_sid_rule_in_file(sid, filename)

    def enable_sid(self, sid):
        files = get_filelist()
        for filename in files:
            enable_sid_rule_in_file(sid, filename)

    def get_filelist(self, dir=RULES_DIRECTORY):
        files = os.listdir(RULES_DIRECTORY)
        result = []
        for f in files:
            if (".rules" in f) and ('hash' not in f):
                result.append(f)
        return result

    def disable_all_rules_in_file(self, filename):

        f = open(RULES_DIRECTORY+filename, 'r')
        lines = f.readlines()
        f.close()

        f = open(RULES_DIRECTORY+filename, 'w')
        for line in lines:
            if line[0:5] == 'alert':
                f.write('#' + line)
            else:
                f.write(line)
        f.close()

    def enable_all_rules_in_file(self, filename):

        f = open(RULES_DIRECTORY+filename, 'r')
        lines = f.readlines()
        f.close()

        f = open(RULES_DIRECTORY+filename, 'w')
        for line in lines:
            if line[0:6] == '#alert':
                f.write(line.replace('#', ''))
            else:
                f.write(line)
        f.close()

    def disable_class_rules_in_file(self, clas, filename):

        f = open(RULES_DIRECTORY+filename, 'r')
        lines = f.readlines()
        f.close()

        f = open(RULES_DIRECTORY+filename, 'w')
        for line in lines:
            if 'classtype:' + clas in line:
                f.write('#' + line)
            else:
                f.write(line)
        f.close()

    def enable_class_rules_in_file(self, clas, filename):

        f = open(RULES_DIRECTORY+filename, 'r')
        lines = f.readlines()
        f.close()

        f = open(RULES_DIRECTORY+filename, 'w')
        for line in lines:
            if 'classtype:' + clas in line:
                f.write(line.replace('#', ''))
            else:
                f.write(line)
        f.close()

    def disable_sid_rule_in_file(self, sid, filename):

        f = open(RULES_DIRECTORY+filename, 'r')
        lines = f.readlines()
        f.close()

        f = open(RULES_DIRECTORY+filename, 'w')
        for line in lines:
            if 'sid:' + sid in line:
                f.write('#' + line)
            else:
                f.write(line)
        f.close()

    def enable_sid_rule_in_file(self, sid, filename):

        f = open(RULES_DIRECTORY+filename, 'r')
        lines = f.readlines()
        f.close()

        f = open(RULES_DIRECTORY+filename, 'w')
        for line in lines:
            if 'sid:' + sid in line:
                f.write(line.replace('#', ''))
            else:
                f.write(line)
        f.close()

    def ids_rulesreload(self):
        cmd = "/etc/init.d/ids rules-reload"
        exec_bash(cmd)
