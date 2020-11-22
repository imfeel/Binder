import keyboard
from PyQt5 import QtCore, QtGui, QtWidgets
from design import *
import sys
import time
app = QtWidgets.QApplication(sys.argv)
mainWindow = QtWidgets.QMainWindow()
ui = Ui_mainWindow()
ui.setupUi(mainWindow)
mainWindow.show()
# code
def main():
    ask = ui.lineEdit.text()
    ask1 = ui.lineEdit_2.text()
    ask2 = ui.lineEdit_3.text()
    while True:
        keyboard.wait(ask)
        keyboard.press_and_release(ask2);time.sleep(0.1)
        keyboard.write(ask1 , delay=0)
        keyboard.press_and_release('enter')
ui.pushButton.clicked.connect(main)
# Not code
sys.exit(app.exec_())