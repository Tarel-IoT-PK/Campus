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
#=======================================================================================================

#=======================================================================================================
        
class qtFindID(QWidget):
    conn = None
    curIdx = 0

    def __init__(self):
       super().__init__()
       uic.loadUi('./Project/findId.ui', self)
       self.show()
       self.btnHome.clicked.connect(self.btnHomeClicked)
       self.btnFind.clicked.connect(self.btnFindClicked)

    def btnFindClicked(self): # 찾기
        self.conn = pymysql.connect(host='210.119.12.57', user ='root', password='12345',
                            db = 'campusdb', charset='utf8')
       
        name = self.txtName.text()
        birthYear = self.txtBirthYear.text()
        result = self.lblfindID.text()
        #major = self.txtMajor.text()

        if name == '' or birthYear == '' :#or major == '':
            QMessageBox.warning(self, '주의', '이름과 생년월일을 입력하세요')
            return
        else:
            query = '''SELECT studentID
                         FROM studenttbl
                        WHERE studentName = %s
                          AND birthday = %s
                        '''
        try:
            cur = self.conn.cursor()
            cur.execute(query, (name, birthYear))
            rows =cur.fetchall()
            self.lblfindID.setText(str(rows[0][0]))
        except:
            QMessageBox.warning(self, '주의', '없는 계정입니다')
            self.lblfindID.setText('')
            return            


    def btnHomeClicked(self):
        self.close()

class qtFindPW(QWidget):
    conn = None   

    def __init__(self):
       super().__init__()
       uic.loadUi('./Project/findPw.ui', self)
       self.show()  
       self.btnPwtoHome.clicked.connect(self.btnPwtoHomeClicked)
       self.btnFindPw.clicked.connect(self.btnfindPwClicked)

    def btnfindPwClicked(self):
        PwstID = self.txtPwstID.text()
        PwBirth = self.txtPwBirth.text()
        if PwstID == '' or PwBirth == '':
            QMessageBox.warning(self, '주의', '이름과 생년월일을 입력하세요!')
            return
        else:
            self.conn = pymysql.connect(host='210.119.12.57', user='root', password='12345',
                                        db='campusdb', charset='utf8')
            
        try:
            cur = self.conn.cursor()
            query = '''SELECT password
                        FROM logintbl AS l
                        INNER JOIN studenttbl AS s
                        ON s.studentID = l.studentID
                        AND s.studentID = %s
                        AND birthday = %s'''
            cur.execute(query, (PwstID, PwBirth))
            rows = cur.fetchall()
            self.lblfindPW.setText(str(rows[0][0]))
        except:
            QMessageBox.warning(self, '주의', '없는 계정입니다')
            self.lblfindPW.setText('')
            return          

    def btnPwtoHomeClicked(self):
        self.close()
        super().__init__()
 #  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++================================
            




        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = qtApp()
    ex.show()
    sys.exit(app.exec_())