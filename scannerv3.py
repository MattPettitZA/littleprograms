#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  test.py
#
# ~ "THE BEER-WARE LICENSE" (Revision 42):
# ~ <pettit.matt@gmail.com> wrote this file. As long as you retain this notice you
# ~ can do whatever you want with this stuff. If we meet some day, and you think
# ~ this stuff is worth it, you can buy me a beer in return. Matt Pettit

#
#
import os
print("""


███████╗ ██████╗ █████╗ ███╗   ██╗███╗   ██╗███████╗██████╗     ██╗   ██╗██████╗
██╔════╝██╔════╝██╔══██╗████╗  ██║████╗  ██║██╔════╝██╔══██╗    ██║   ██║╚════██╗
███████╗██║     ███████║██╔██╗ ██║██╔██╗ ██║█████╗  ██████╔╝    ██║   ██║ █████╔╝
╚════██║██║     ██╔══██║██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══██╗    ╚██╗ ██╔╝ ╚═══██╗
███████║╚██████╗██║  ██║██║ ╚████║██║ ╚████║███████╗██║  ██║     ╚████╔╝ ██████╔╝
╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝      ╚═══╝  ╚═════╝

Made by Matt Pettit
""")

ip = str(input("Input the first 2 subnets(eg 10.0.): " ))
for i in range(255):
		print("Testing: "+ip+str(i)+".*")
		os.system("nmap -sn "+ip+str(i)+".*")
