#!/usr/bin/python
# -*- coding: utf-8 -*-

import os 

def run(**args):
    print "[+] In enviroment module."
    return str(os.environ)
