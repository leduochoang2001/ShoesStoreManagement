from PyQt5 import QtCore, QtGui, QtWidgets
import sys

def checklogin() :
    if text1.text() == 'djt mm ao that day' and text2.text() == 'passw' :
        label.setText("True")
    else : label.setText("User Name Or Password is incorrect \n please try again!")

app = QtWidgets.QApplication(sys.argv)
win = QtWidgets.QMainWindow()
win.setGeometry(200, 200, 400, 400)

text1 = QtWidgets.QLineEdit(win)
text1.move(100, 80)
text2 = QtWidgets.QLineEdit(win)
text2.move(100, 120)
text2.setEchoMode(QtWidgets.QLineEdit.Password)

label = QtWidgets.QLabel(win)
label.resize(250, 100)
label.move(100, 320)

but = QtWidgets.QPushButton(win)
but.setText("Click here")
but.move(100, 200)
but.clicked.connect(checklogin)

win.show()
sys.exit(app.exec_())   
