from lxml import html
import requests
import time
import subprocess
import os

#constants
INTERVAL_FOR_CHECKS = 1200 #seconds to wait for chk

#for fetching page data, using requests
page = requests.get('https://deathsnacks.com/wf/')
tree = html.fromstring(page.content)

#our list of items to search for
response = ''
boolExists = False

#sound used to alert
soundAlert = 'Spirit.mp3'
while(1):
    boolExists = False
    response = ''

    #get page text
    page = requests.get('https://deathsnacks.com/wf/')
    pageText = page.text
    pageText = pageText.lower()

    #audio boolean
    playedLast = False
    #parse
    for x in alertList:
        #looking for stuff in alertList
        if pageText.find(x) != -1:
            boolExists = True
            #if we find stuff, add it to our response string
            if response != '':
                response += ' + '
            response += 'We found: ' + x
        else:
            #if we dont find it, say we didnt
            if response != '':
                response += ' + '
            response += 'We DIDNT find: ' + x
    #print found string
    if boolExists:
        print response
        if playedLast == False:
            os.system("start C:\Araw\Spirit.mp3")
            playedLast = True
    else:
        print 'Nothing found, will check again in a bit ' + response
        playedLast = False
    #wait
    time.sleep(INTERVAL_FOR_CHECKS)