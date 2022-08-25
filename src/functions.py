
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
       def setupUi(self, MainWindow):
              def show_screen1(self) :
                            self.tabWidget.setCurrentWidget(self.tab)

              def show_screen2(self) :
                            self.tabWidget.setCurrentWidget(self.tab_2)
                            
              def show_screen3(self) :
                            self.tabWidget.setCurrentWidget(self.tab_3)

       self.but_viewpro.clicked.connect(self.show_screen1)
       self.but_order.clicked.connect(self.show_screen2)
       self.but_editdata.clicked.connect(self.show_screen3)