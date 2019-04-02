#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  youtubelink.py
#  
# ~ "THE BEER-WARE LICENSE" (Revision 42):
# ~ <pettit.matt@gmail.com> wrote this file. As long as you retain this notice you
# ~ can do whatever you want with this stuff. If we meet some day, and you think
# ~ this stuff is worth it, you can buy me a beer in return. Matt Pettit
#
#  https://stackoverflow.com/questions/29069444/returning-the-urls-as-a-list-from-a-youtube-search-query
#  


import urllib
import urllib2
from bs4 import BeautifulSoup
import os
from youtube_dl import YoutubeDL
print("""


██╗     ██╗███╗   ██╗██╗  ██╗███████╗██████╗     ██╗   ██╗██████╗ 
██║     ██║████╗  ██║██║ ██╔╝██╔════╝██╔══██╗    ██║   ██║╚════██╗
██║     ██║██╔██╗ ██║█████╔╝ █████╗  ██████╔╝    ██║   ██║ █████╔╝
██║     ██║██║╚██╗██║██╔═██╗ ██╔══╝  ██╔══██╗    ╚██╗ ██╔╝██╔═══╝ 
███████╗██║██║ ╚████║██║  ██╗███████╗██║  ██║     ╚████╔╝ ███████╗ 
╚══════╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝      ╚═══╝  ╚══════╝   
    
|_|0|_|
|_|_|0|
|0|0|0|
                                                              
Made By Matt Pettit

""")

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
	link = links[0]
	
	
	var = str(input("Are you running on (1)Windows which will give you mp4 or (2)linux with youtube-dl installed? Please give either 1 or 2: "))
	if var == "2":
		place = str(raw_input("/home/matt/Music/Liams_Music or any other output dir: "))
		os.system("youtube-dl -o "+'"'+place+"%(title)s.%(ext)s"+'"'+" --extract-audio --audio-format mp3 "+link)
	else:
		try:
			YouTube(link).streams.first().download()
		except:
			print("There was an error.")
	print("Done")
	
linker()
