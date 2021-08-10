#!usr/bin/env python3

import subprocess
from optparse import OptionParser
import re


def get_arguments():
    parser = OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] please specify the interface, use --help for more information")
    elif not options.new_mac:
        parser.error("[-] please specify the MAC address, use --help for more information")
    else:
        return options


def change_mac(interface, new_mac):
    print("[+] Changing the MAC address for " + interface + " to " + new_mac)

    subprocess.run(["ifconfig", interface, "down"])
    subprocess.run(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.run(["ifconfig", interface, "up"])


def get_curr_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])

    mac_address_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result))

    if mac_address_result:
        return mac_address_result.group(0)

    else:
        print("[-] could not read MAC Address ")


options = get_arguments()

curr_mac = get_curr_mac(options.interface)
print("current MAC address = " + str(curr_mac))

change_mac(options.interface, options.new_mac)

curr_mac = get_curr_mac(options.interface)

if curr_mac == options.new_mac:
    print("[-] MAC address changed successfully")
else:
    print("[-] ERROR MAC address did not change")

