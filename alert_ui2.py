import sys
from PyQt4.QtCore import SIGNAL
from PyQt4.QtGui import QDialog, QApplication, QPushButton, QLineEdit, QFormLayout, QGridLayout, QLabel, QTextEdit

class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        self.title1 = QLabel('Items')

        self.foundLabel = QLabel('If found, will appear here')

        self.textBox1 = QTextEdit()
        self.textBox1.setObjectName("Item to Search For")
        self.textBox1.setText("Please enter a list of items to search for, separated by commas.")

        self.btn1 = QPushButton()
        self.btn1.setObjectName("Search")
        self.btn1.setText("Search")

        # layout = QFormLayout()
        layout = QGridLayout()
        layout.setSpacing(10)

        layout.addWidget(self.title1, 1, 0)
        layout.addWidget(self.textBox1, 1, 1)
        layout.addWidget(self.btn1, 2, 1)
        layout.addWidget(self.foundLabel, 3, 1)

        self.setLayout(layout)
        self.connect(self.btn1, SIGNAL("clicked()"), self.button_click)
        self.setWindowTitle("Warframe Alert Tool")
        self.setGeometry(300, 300, 600, 200)

    def button_click(self):
        # shost is a QString object
        alertItems = str(self.textBox1.toPlainText())
        alertList = alertItems.split(',')

        #print alertItems
        #print alertList


app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()