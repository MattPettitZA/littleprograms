#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  ipexternal.py
#  
# ~ "THE BEER-WARE LICENSE" (Revision 42):
# ~ <pettit.matt@gmail.com> wrote this file. As long as you retain this notice you
# ~ can do whatever you want with this stuff. If we meet some day, and you think
# ~ this stuff is worth it, you can buy me a beer in return. Matt Pettit
#
#https://stackoverflow.com/questions/2311510/getting-a-machines-external-ip-address-with-python/22157882#22157882

import time
import ipgetter

def getter():
	while True:
		IP = ipgetter.myip()
		print(IP)
		time.sleep(5)
		
	
	

getter()

