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
        studentID = self.txtID.text()
        password = self.txtPW.text()

        if studentID == '' or password == '':
            QMessageBox.warning(self, '주의', '학번과 비밀번호를 입력하세요!') 
            return 
        else:
            self.conn = pymysql.connect(host='210.119.12.57', user='root', password='12345',
                                        db='campusdb', charset='utf8')
            cursor = self.conn.cursor()

            query = '''SELECT password FROM logintbl WHERE studentID = %s'''
            cursor.execute(query, (studentID))
            result = cursor.fetchone()
            
            if result is not None and result[0] == password:
                QMessageBox.information(self, "로그인 성공", "로그인 되었습니다.")
                self.hide()
                self.studentCard = qtStudentCard()
            else:
                QMessageBox.warning(self, "로그인 실패", "잘못된 학번과 비밀번호 입니다.")
                
                self.txtID.setText('')
                self.txtPW.setText('')
                self.txtID.setFocus()
            
            # 데이터베이스 연결 해제
            cursor.close()
            self.conn.close()
            

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

class qtFindID(QMainWindow):
    def __init__(self):
       super().__init__()
       uic.loadUi('./Project/findId.ui', self)   
       # self.hide()
       self.show()  
       

class qtFindPW(QMainWindow):
    def __init__(self):
       super().__init__()
       uic.loadUi('./Project/findPw.ui', self)   
       # self.hide()
       self.show()  
       

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = qtApp()
    ex.show()
    sys.exit(app.exec_())