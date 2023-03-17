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

        self.initDB() # DB 초기화

        self.btnClose.clicked.connect(self.btnCloseClicked)
        self.btnLogout.clicked.connect(self.btnLogoutClicked)
    
    def btnCloseClicked(self):
        self.close()

    def btnLogoutClicked(self):
        self.close()
        super().__init__()
        uic.loadUi('./Project/login.ui', self) 
        self.show()

    def initDB(self):
        self.conn = pymysql.connect(host='210.119.12.57', user='root', password='12345',
                                    db='campusdb', charset='utf8')
        cur = self.conn.cursor()
        query = '''SELECT studentID
                        , studentName
                        , birthday
                     FROM studenttbl
                    WHERE studentID = 20214210;''' 
        cur.execute(query)
        rows = cur.fetchall()

        # print(rows)
        self.makeTable(rows)
        self.conn.close() # 프로그램 종료할 때
        

    def makeTable(self, rows) -> None:
        self.tblstudentCard.setColumnCount(3)  # setColumnCount -> 대소문자 구분함,,
        self.tblstudentCard.setRowCount(len(rows))
        self.tblstudentCard.setHorizontalHeaderLabels(['학번', '이름', '생년월일'])
        self.tblstudentCard.setColumnWidth(0,0)   # 번호 -> 숨김
        self.tblstudentCard.setColumnWidth(1,70)  # 이름 열 사이즈 : 70
        self.tblstudentCard.setColumnWidth(2,105) # 핸드폰 열 사이즈 : 105
        self.tblstudentCard.setEditTriggers(QAbstractItemView.NoEditTriggers)

        for i, row in enumerate(rows):
            # row[0] ~ row[2] 까지 쓸 수 있음
            studentId = row[0]
            studentName = row[1]
            birthday = row[2]
            self.tblstudentCard.setItem(i, 0 , QTableWidgetItem(str(studentId)))
            self.tblstudentCard.setItem(i, 1 , QTableWidgetItem(studentName))
            self.tblstudentCard.setItem(i, 2 , QTableWidgetItem(birthday))
        
        
        self.tblstudentCard.setVisible(False)
        self.tblstudentCard.hide()

        self.txtName.setText(str(studentName))

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