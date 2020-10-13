# -*- coding: utf-8 -*-
"""
Created on Sat May 16 04:03:47 2020

@author: hp
"""

import urllib.request as url_req
from pygame import mixer

host = "http://google.com"
filepath = "files\\SYT.mp3"

def notify():
    mixer.init()
    mixer.music.load(filepath)
    mixer.music.play()


def looper():
	while True:
		print("Net Asche", end=" ")

	

def isConnection():
    try:
        url_req.urlopen(host)
        return True
    except:
        return False





print("Initiating....", end="\n\n")
print("Trying to Ping...")    
    
while True:
    if(isConnection()):
        notify()
        looper()
        break
		
		
# mixer.music.get_busy() boolean for music stop!
    