#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  links2.py
#
# ~ "THE BEER-WARE LICENSE" (Revision 42):
# ~ <pettit.matt@gmail.com> wrote this file. As long as you retain this notice you
# ~ can do whatever you want with this stuff. If we meet some day, and you think
# ~ this stuff is worth it, you can buy me a beer in return. Matt Pettit

#
#
import pafy
import urllib
import urllib2
from bs4 import BeautifulSoup
import webbrowser
import os

def linker():
	global links
	links = []
	textToSearch = str(raw_input("What would you like to search? "))
	query = urllib.quote(textToSearch)
	url = "https://www.youtube.com/results?search_query=" + query
	response = urllib2.urlopen(url)
	html = response.read()
	soup = BeautifulSoup(html, "html.parser")
	for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
		links.append('https://www.youtube.com' + vid['href'])
	global link
	link = links[0]
linker()

video = pafy.new(link)

audiostreams = video.audiostreams
for i in audiostreams:
    print(i.extension, i.get_filesize())

audiostreams[2].download()
