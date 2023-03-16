import sys 
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import pymysql

class qtApp(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('./Project/login.ui', self)

        self.btnlogin.clicked.connect(self.btnloginClicked)
        self.btnID.clicked.connect(self.btnIDClicked)
        self.btnPW.clicked.connect(self.btnPWClicked)

    def btnloginClicked(self):
        self.hide()
        self.studentCard = qtStudentCard()
        

    def btnIDClicked(self):
        self.findID = qtFindID()

    def btnPWClicked(self):
        self.findPW = qtFindPW()

class qtStudentCard(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('./Project/studentCard.ui', self)   
        self.show()    

        self.btnClose.clicked.connect(self.btnCloseClicked)
        self.btnLogout.clicked.connect(self.btnLogoutClicked)
    
    def btnCloseClicked(self):
        self.close()

    def btnLogoutClicked(self):
        self.close()
        super().__init__()
        uic.loadUi('./Project/login.ui', self) 
        self.show()

        
class qtFindID(QWidget):
    def __init__(self):
       super().__init__()
       uic.loadUi('./Project/findId.ui', self)   
       self.show()  

class qtFindPW(QWidget):
    def __init__(self):
       super().__init__()
       uic.loadUi('./Project/findPw.ui', self)   
       self.show()  

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = qtApp()
    ex.show()
    sys.exit(app.exec_())