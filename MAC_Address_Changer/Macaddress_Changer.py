#!/usr/bin/env python

#Please note: All this is done for ethical purposes. Please stay within the law. 

import subprocess

interface = input("Please input the name the interface you wish to change: ")
mac_add = input("Enter your new mac address : ")

subprocess.call(["sudo", "ifconfig", interface, "down"])
subprocess.call(["sudo", "ifconfig", interface, "hw", "ether", mac_add])
subprocess.call(["sudo", "ifconfig", interface, "up"]) 
