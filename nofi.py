#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  nofi.py
#
# ~ "THE BEER-WARE LICENSE" (Revision 42):
# ~ <pettit.matt@gmail.com> wrote this file. As long as you retain this notice you
# ~ can do whatever you want with this stuff. If we meet some day, and you think
# ~ this stuff is worth it, you can buy me a beer in return. Matt Pettit
# 
#

import os
import sys
import time

print("""


███╗   ██╗ ██████╗ ███████╗██╗
████╗  ██║██╔═══██╗██╔════╝██║
██╔██╗ ██║██║   ██║█████╗  ██║
██║╚██╗██║██║   ██║██╔══╝  ██║
██║ ╚████║╚██████╔╝██║     ██║
╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝

by Matt Pettit
""")


def start():
	try:
		global interface
		interface = str(sys.argv[1])

	except:
		print("Error: Did you forget the interface name?")
		sys.exit(1)

	global mac
	mac = str(input("Enter the Targets MAC Address: "))

def maccer():
	while True:
		os.system("ifconfig " + interface + " down")
		os.system("ifconfig " + interface + " hw ether "+mac)
		os.system("ifconfig " + interface + " up")
		os.system("nmcli radio wifi off")
		os.system("nmcli radio wifi on")
		print("Mac Set to: "+mac)
		input("Press Enter to Kick MAC Again")


def main():
	start()
	maccer()

main()
