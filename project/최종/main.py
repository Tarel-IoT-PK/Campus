import sys 
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import pymysql
import qrcode

QRText = ''

class qtApp(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('./Project/login.ui', self)
        self.setWindowIcon(QIcon('./project/login.png'))
        self.hide()
        self.show()

        self.txtID.returnPressed.connect(self.txtPWReturned)
        self.txtPW.returnPressed.connect(self.txtPWReturned)
        self.btnlogin.clicked.connect(self.btnloginClicked)
        self.btnID.clicked.connect(self.btnIDClicked)
        self.btnPW.clicked.connect(self.btnPWClicked)

    def txtPWReturned(self):
        self.btnloginClicked()

    def btnloginClicked(self):
        global studentID
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
        self.setWindowIcon(QIcon('./project/student.png'))
        self.show()    

        self.initDB() # DB 초기화

        self.btnClose.clicked.connect(self.btnCloseClicked)
        self.btnLogout.clicked.connect(self.btnLogoutClicked)
    
    def btnCloseClicked(self):
        self.close()

    def btnLogoutClicked(self):
        self.hide()
        self.btnLogoutClicked= qtApp()


    def initDB(self):
        self.conn = pymysql.connect(host='210.119.12.57', user='root', password='12345',
                                    db='campusdb', charset='utf8')
        cur = self.conn.cursor()
        cursor = self.conn.cursor()

        query2 = '''SELECT studentName
                          FROM studenttbl
                         WHERE studentID = %s'''
        cursor.execute(query2, (studentID))

        query = '''SELECT s.studentID
                        , s.studentName
                        , s.major
                        , m.name
                     FROM studenttbl AS s
                    INNER JOIN major AS m
                    ON s.major = m.majorid  
                    WHERE s.studentID = %s;'''  # 학번 where 절 고치기 해야함!!!
        cur.execute(query, (studentID))
        rows = cur.fetchall()

        # print(rows)
        self.makeTable(rows)
        self.conn.close() # 프로그램 종료할 때

        qrName = self.tblstudentCard.item(0, 1).text()
        qrstudentID = self.tblstudentCard.item(0, 0).text()
        qrMajor = self.tblstudentCard.item(0, 2).text()
        QRText = f'이름 : {qrName} / 학번 : {qrstudentID} / 전공 : {qrMajor}'
        qr_img = qrcode.make(QRText)
        qr_img.save('./project/save.png')

        img = QPixmap('./project/save.png')
        self.lblQrCode.setPixmap(QPixmap(img).scaledToWidth(215))
        # print(qrMajor)
        

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
            birthday = row[3]
            self.tblstudentCard.setItem(i, 0 , QTableWidgetItem(str(studentId)))
            self.tblstudentCard.setItem(i, 1 , QTableWidgetItem(studentName))
            self.tblstudentCard.setItem(i, 2 , QTableWidgetItem(birthday))
        
        
        self.tblstudentCard.setVisible(False)
        self.tblstudentCard.hide()

        self.txtName.setText(str(studentName))
        self.txtstudentID.setText(str(studentId))
        self.txtMajor.setText(str(birthday))


class qtFindID(QWidget):
    conn = None
    curIdx = 0

    def __init__(self):
        super().__init__()
        uic.loadUi('./Project/findId.ui', self)
        self.setWindowIcon(QIcon('./project/find.png'))
        self.show()
        self.txtName.returnPressed.connect(self.txtNameReturned)
        self.txtBirthYear.returnPressed.connect(self.txtBirthYearReturned)
        self.txtMajor.returnPressed.connect(self.txtMajorReturned)
        self.btnHome.clicked.connect(self.btnHomeClicked)
        self.btnFind.clicked.connect(self.btnFindClicked)

    def txtNameReturned(self):
        self.btnFindClicked()

    def txtBirthYearReturned(self):
        self.btnFindClicked()

    def txtMajorReturned(self):
        self.btnFindClicked()

    def btnFindClicked(self): # 찾기
        self.conn = pymysql.connect(host='210.119.12.57', user ='root', password='12345',
                            db = 'campusdb', charset='utf8')
       
        name = self.txtName.text()
        birthYear = self.txtBirthYear.text()
        result = self.lblfindID.text()
        major = self.txtMajor.text()

        if name == '' or birthYear == '' or major == '':
            QMessageBox.warning(self, '주의', '이름, 생년월일, 전공을 입력하세요')
            return
        else:
            query = '''SELECT studentID
                         FROM studenttbl
                        WHERE studentName = %s
                          AND birthday = %s
                          AND major = %s
                        '''
        try:
            cur = self.conn.cursor()
            cur.execute(query, (name, birthYear, major))
            rows =cur.fetchall()
            self.lblfindID.setText(str(rows[0][0]))
            self.lblName.setText(f'{name} 님의 학번은 ')
            self.label_6.setText('입니다.')
        except:
            QMessageBox.warning(self, '주의', '없는 계정입니다')
            self.lblfindID.setText('')
            return            


    def btnHomeClicked(self):
        self.hide()
        self.btnLogoutClicked= qtApp()

class qtFindPW(QWidget):
    conn = None   

    def __init__(self):
       super().__init__()
       uic.loadUi('./Project/findPw.ui', self)
       self.setWindowIcon(QIcon('./project/find.png'))
       self.show()  
       self.txtPwstID.setFocus()
       self.btnPwtoHome.clicked.connect(self.btnPwtoHomeClicked)
       self.btnFindPw.clicked.connect(self.btnFindPwClicked)
       self.txtPwstID.returnPressed.connect(self.txtPwstIDReturned)
       self.txtPwName.returnPressed.connect(self.txtPwNameReturned)
       self.txtPwBirth.returnPressed.connect(self.txtPwBirthReturned)

    def txtPwstIDReturned(self):
        self.btnFindPwClicked()

    def txtPwNameReturned(self):
        self.btnFindPwClicked()

    def txtPwBirthReturned(self):
        self.btnFindPwClicked()
        

    def btnFindPwClicked(self):
        PwstID = self.txtPwstID.text()
        PwBirth = self.txtPwBirth.text()
        name = self.txtPwName.text()
        if PwstID == '' or PwBirth == '' or name =='':
            QMessageBox.warning(self, '주의', '학번, 이름, 생년월일을 입력하세요!')
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
                        AND studentName = %s
                        AND birthday = %s'''
            cur.execute(query, (PwstID, name, PwBirth))
            rows = cur.fetchall()
            self.lblfindPW.setText(str(rows[0][0]))
            self.lblPw.setText(f'{name} 님의 비밀번호는 ')
            self.lblind.setText('입니다.')
        except:
            QMessageBox.warning(self, '주의', '없는 계정입니다')
            self.lblfindPW.setText('')
            return          

    def btnPwtoHomeClicked(self):
        self.hide()
        self.btnLogoutClicked= qtApp()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = qtApp()
    ex.show()
    sys.exit(app.exec_())