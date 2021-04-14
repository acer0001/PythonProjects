#! //usr/bin/env python3

import subprocess
import optparse
import random

def get_args():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface for MAC address change")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
    parser.add_option("-r", "--random", dest="random",  help="Random MAC address")
    # Include conditional to make sure -i and -m or -r are used for a complete command.
    # Include conditional to verify that -r and -m are Both both used simultaneously
    return parser.parse_args()

def change_mac(interface, new_mac):
    print("[+] Changing MAC address for interface " + interface + " to", new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

(options, arguments) = get_args()

# Use arguments.random from return of get_args to start the random generation process

def hex_convert():
    # GOAL: Create six sets of two numbers for a random mac address
    # Cycle through 12 times to get a 12 digit number
    # Separate each set of two numbers with a colon

# (hex(random.randrange(0, 17)).lstrip("0x"))

def gen_rand_digit ():
    hex_list = ["0", "1", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
    rand_digit = random.choice(hex_list)
    return print(rand_digit)

print(gen_rand_digit)


change_mac(options.interface, options.new_mac)