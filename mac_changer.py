#!usr/bin/env python3

import subprocess
from optparse import OptionParser


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


options = get_arguments()
change_mac(options.interface, options.new_mac)

