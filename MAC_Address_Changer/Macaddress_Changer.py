#!/usr/bin/env python3


import subprocess
import optparse

parser = optparse.OptionParser()

parser.add_option("-i", "--interface", dest= "interface", help="Interface to change MAC Address")
parser.add_option("-m", "--mac", dest="mac_add", help="Specify the new mac address")

(options, arguments) = parser.parse_args()

# subprocess.call("sudo ifconfig", shell=True)
interface = options.interface
mac_add = options.mac_add


subprocess.call(["sudo", "ifconfig", interface, "down"])
subprocess.call(["sudo", "ifconfig", interface, "hw", "ether", mac_add])
subprocess.call(["sudo", "ifconfig", interface, "up"])
