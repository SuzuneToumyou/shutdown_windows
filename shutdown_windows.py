#!/usr/bin/python3
# -*- coding: utf-8 -*

import subprocess

def shutdown_windows(host,owner,passwd,reboot_flag):
    if reboot_flag == 1:
        message = "net rpc shutdown -I " + host + " -U " + owner + "%" + passwd + " -r"
    else:
        message = "net rpc shutdown -I " + host + " -U " + owner + "%" + passwd
    res = subprocess.run(message, shell=True,text=True)
    #print (res)

if __name__ == "__main__":
    shutdown_windows('192.168.0.1', 'user', 'passwd',0)
