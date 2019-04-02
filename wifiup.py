#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  wifiup.py
#
# ~ "THE BEER-WARE LICENSE" (Revision 42):
# ~ <pettit.matt@gmail.com> wrote this file. As long as you retain this notice you
# ~ can do whatever you want with this stuff. If we meet some day, and you think
# ~ this stuff is worth it, you can buy me a beer in return. Matt Pettit

#


import os
import time
hostname = "8.8.8.8"


while True:
	if (os.system("ping -c 1 " + hostname)) == 0:
		print ('Netoworking is up!')
	else:
		print ('Networking is down!')

	time.sleep(5)
