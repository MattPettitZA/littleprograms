#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  abacus.py
#
# ~ "THE BEER-WARE LICENSE" (Revision 42):
# ~ <pettit.matt@gmail.com> wrote this file. As long as you retain this notice you
# ~ can do whatever you want with this stuff. If we meet some day, and you think
# ~ this stuff is worth it, you can buy me a beer in return. Matt Pettit


word = str(input("Enter a number"))

for i in range(len(word)):
	num= int(word[i])
	print(str("|"+(num*"x") + "-----"+ (10-num)*"x")+"|")
