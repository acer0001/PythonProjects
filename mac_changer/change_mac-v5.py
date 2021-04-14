#! /usr/bin/env python3

# Added a function for the for the optparse parameters

import subprocess
import optparse

def get_args():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface for MAC address change")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify and interface with -i or --interface")
    elif not options.new_mac:
        parser.error("[-] Please specify a MAC address with --m or --mac")
    return options

def change_mac(interface, new_mac):
    print("[+] Changing MAC address for interface " + interface + " to", new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

options = get_args()
change_mac(options.interface, options.new_mac)

