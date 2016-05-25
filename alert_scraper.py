from lxml import html
import requests
import time

page = requests.get('https://deathsnacks.com/wf/')
tree = html.fromstring(page.content)

alertList = ['vauban chassis', 'nitain extract', 'neural sensors']
response = ''
boolExists = False

while(1):
    boolExists = False
    response = ''
    #get page text
    page = requests.get('https://deathsnacks.com/wf/')
    pageText = page.text
    pageText = pageText.lower()

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
    else:
        print 'Nothing found, will check again in a bit'
    #wait
    time.sleep(10)