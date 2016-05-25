#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
ZetCode PyQt4 tutorial

In this example, we determine the event sender
object.

author: Jan Bodnar
website: zetcode.com
last edited: October 2011
"""

import sys
from PyQt4 import QtGui, QtCore
from lxml import html
import requests
import time
import subprocess
import os

class Example(QtGui.QMainWindow):
    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):
        self.btn1 = QtGui.QPushButton("Search", self)
        self.btn1.setGeometry(50, 300, 100, 50)

        self.btn2 = QtGui.QPushButton("Stop", self)
        self.btn2.setGeometry(200, 300, 100, 50)

        self.textBox1 = QtGui.QTextEdit("Pleas enter the items you seek on alerts, separated by commas.", self)
        self.textBox1.setGeometry(50, 50, 400, 100)

        self.connect(self.btn1, SIGNAL("clicked()"), self.buttonClickedSearch())

        self.setGeometry(300, 300, 640, 480)
        self.setWindowTitle('WF Alert Checker')
        self.show()

    def buttonClickedSearch(self):
        print self.textBox1.toPlainText()
        # # constants
        # INTERVAL_FOR_CHECKS = 1200  # seconds to wait for chk
        #
        # # for fetching page data, using requests
        # page = requests.get('https://deathsnacks.com/wf/')
        # tree = html.fromstring(page.content)
        #
        # # our list of items to search for
        # alertList = ['vauban chassis', 'nitain extract']
        # response = ''
        # boolExists = False
        #
        # # sound used to alert
        # soundAlert = 'Spirit.mp3'
        # while (1):
        #     boolExists = False
        #     response = ''
        #
        #     # get page text
        #     page = requests.get('https://deathsnacks.com/wf/')
        #     pageText = page.text
        #     pageText = pageText.lower()
        #
        #     # audio boolean
        #     playedLast = False
        #     # parse
        #     for x in alertList:
        #         # looking for stuff in alertList
        #         if pageText.find(x) != -1:
        #             boolExists = True
        #             # if we find stuff, add it to our response string
        #             if response != '':
        #                 response += ' + '
        #             response += 'We found: ' + x
        #         else:
        #             # if we dont find it, say we didnt
        #             if response != '':
        #                 response += ' + '
        #             response += 'We DIDNT find: ' + x
        #     # print found string
        #     if boolExists:
        #         print response
        #         if playedLast == False:
        #             os.system("start C:\Araw\Spirit.mp3")
        #             playedLast = True
        #     else:
        #         print 'Nothing found, will check again in a bit ' + response
        #         playedLast = False
        #     # wait
        #     time.sleep(INTERVAL_FOR_CHECKS)



def main():
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()