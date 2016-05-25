import sys
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import SIGNAL, QTimer
from PyQt4.QtGui import QDialog, QApplication, QPushButton, QLineEdit, QFormLayout, QGridLayout, QLabel, QTextEdit
from lxml import html
import requests
import time
import subprocess
import os

# constants
INTERVAL_FOR_CHECKS = 1000000  # seconds to wait for chk

class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        #unused label
        self.title1 = QLabel('Items')

        #string displayed to user on bottom
        self.foundLabel = QLabel('If found, will appear here')

        #text box to take input
        self.textBox1 = QTextEdit()
        self.textBox1.setObjectName("Item to Search For")
        self.textBox1.setText("Please enter a list of items to search for, separated by commas.")

        #begins the search button
        self.btn1 = QPushButton()
        self.btn1.setObjectName("Search")
        self.btn1.setText("Search")

        #stops the search button
        self.btn2 = QPushButton()
        self.btn2.setObjectName("Stop")
        self.btn2.setText("Stop")

        #CONNECT BUTTON SIGNALS
        self.connect(self.btn1, SIGNAL("clicked()"), self.button_click)
        self.connect(self.btn2, SIGNAL("clicked()"), self.cancel_search)
        #timer used to call a function many times, is set up during the search button press
        self.timer = QTimer()

        # THis layout is used to give the app it's grid form
        layout = QGridLayout()
        layout.setSpacing(10)

        layout.addWidget(self.title1, 1, 0)
        layout.addWidget(self.textBox1, 1, 1)
        layout.addWidget(self.btn1, 2, 1)
        layout.addWidget(self.btn2, 2, 0)
        layout.addWidget(self.foundLabel, 3, 1)

        self.setLayout(layout)

        #windows properties
        self.setWindowTitle("Warframe Alert Tool")
        self.setGeometry(300, 300, 600, 200)

    def button_click(self):
        # shost is a QString object
        alertItems = str(self.textBox1.toPlainText())
        alertList = alertItems.split(',')

        # for fetching page data, using requests
        page = requests.get('https://deathsnacks.com/wf/')
        tree = html.fromstring(page.content)

        # our list of items to search for
        response = ''
        boolExists = False

        # sound used to alert
        soundAlert = 'Spirit.mp3'
        boolExists = False
        response = ''

        # get page text
        page = requests.get('https://deathsnacks.com/wf/')
        pageText = page.text
        pageText = pageText.lower()

        # audio boolean
        playedLast = False
        # parse
        for x in alertList:
            # looking for stuff in alertList
            if pageText.find(x) != -1:
                boolExists = True
                # if we find stuff, add it to our response string
                if response != '':
                    response += ' + '
                response += 'We found: ' + x
            else:
                # if we dont find it, say we didnt
                if response != '':
                    response += ' + '
                response += 'We DIDNT find: ' + x
        # print found string
        if boolExists:
            print response
            qsResponse = QtCore.QString(response)
            self.foundLabel.setText(qsResponse)
            if playedLast == False:
                os.system("start C:\Araw\Spirit.mp3")
                playedLast = True
        else:
            response = 'Nothing found, will check again in a bit ' + response
            print response
            qsResponse = QtCore.QString(response)
            self.foundLabel.setText(qsResponse)
            playedLast = False
        #set up constant calls
        self.timer.timeout.connect(self.button_click)
        self.timer.start(INTERVAL_FOR_CHECKS)
    def cancel_search(self):
        self.timer.stop()
        self.foundLabel.setText('Stopping Search')

app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()