#!/usr/bin/python
# ~ "THE BEER-WARE LICENSE" (Revision 42):
# ~ <pettit.matt@gmail.com> wrote this file. As long as you retain this notice you
# ~ can do whatever you want with this stuff. If we meet some day, and you think
# ~ this stuff is worth it, you can buy me a beer in return. Matt Pettit


import os, sys
def rename():
	path = input('Enter Path to Folder(eg /path/to/item/ ): ')
	i = 0
	text = input('Enter what it must be renamed to: ')
	direc = os.listdir(path)
	direc = sorted(direc)

	for item in direc:
		i+= 1
		num = i
		if num < 10:
			num = '0'+str(num)

		os.rename(path+item, path+text+(str(num)))


while True:
	rename()
