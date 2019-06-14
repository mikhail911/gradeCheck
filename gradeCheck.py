"""
    presentationPointer (c) 2019 by Michał Stojke, LICENSE: MIT
	
	Program, which check website if it's context have been changed. 
	Work only with website which don't have dynamic content (such as timer, 
	date, etc..). Before run define website address, and check it charset. 
	Also copy any sound which be played, after website change.
"""

import os.path
import urllib.request
import time
import winsound

tm = 120 #refresh time in seconds
www = 'http://sample_website.com' #website address
chars = 'utf-8' #website charset
sound = 'sound.wav'

#if org website don't exist
web_org = 'org.txt'

if os.path.isfile('org.txt'):
	comm = ''+time.asctime(time.localtime(time.time()))+' : good \n'
	print(comm)

else:
	web = urllib.request.urlopen(www)
	charset = web.info().get_content_charset(chars) #check it!
	content = web.read().decode(charset, 'ignore')
	print(content)
	file = open(web_org, "w")
	file.write(content)
	file.close()

def compareWeb():
	logfile = open('log.txt','a') 
	web_new = 'new.txt'
	web = urllib.request.urlopen(www)
	charset = web.info().get_content_charset(chars) #check it!
	content = web.read().decode(charset, 'ignore')
	file2 = open(web_new, "w")
	file2.write(content)
	file2.close()
	comp1 = open(web_org, 'r')
	comp2 = open(web_new, 'r')

	if comp1.read() != comp2.read() :
		comm= ''+time.asctime(time.localtime(time.time()))+' : results!!! \n'
		print(comm)
		logfile.write(comm) 
		winsound.PlaySound(sound, winsound.SND_FILENAME)
	else:
		comm = ''+time.asctime(time.localtime(time.time()))+' : nothing changed \n'
		print(comm)
		logfile.write(comm)
	comp1.close()
	comp2.close()
	logfile.close()
	time.sleep(tm)

while True:
	compareWeb()
