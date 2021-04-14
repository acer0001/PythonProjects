#! /usr/bin/env python3

import subprocess

interface = input("Enter interface: ")
new_mac = input("Enter MAC address: ")

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])

print("[+] Changing MAC address for interface " + interface + " to", new_mac)
