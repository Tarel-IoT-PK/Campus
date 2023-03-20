import sys 
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import pymysql
import datetime

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
        uic.loadUi('./final/login2.ui', self)
        self.setWindowIcon(QIcon('./final/login.png'))
        self.hide()
        self.show()

        self.txtID.returnPressed.connect(self.txtPWReturned)
        self.txtPW.returnPressed.connect(self.txtPWReturned)
        self.btnlogin.clicked.connect(self.btnloginClicked)
        self.btnID.clicked.connect(self.btnIDClicked)
        self.btnPW.clicked.connect(self.btnPWClicked)
        self.btnNew.clicked.connect(self.btnNewClicked)

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

    def btnNewClicked(self):
        self.findID = qtNew()


class qtStudentCard(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('./final/studentCard.ui', self)   
        self.setWindowIcon(QIcon('./final/student.png'))
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
                    WHERE s.studentID = %s;'''# 학번 where 절 고치기 해야함!!!
        cur.execute(query, (studentID))
        rows = cur.fetchall()

        # print(rows)
        self.makeTable(rows)
        self.conn.close() # 프로그램 종료할 때

        print(rows[0][3])
        qrName = self.tblstudentCard.item(0, 1).text()
        qrstudentID = self.tblstudentCard.item(0, 0).text()
        qrMajor = self.tblstudentCard.item(0, 2).text()
        QRText = f'이름 : {qrName} / 학번 : {qrstudentID} / 전공 : {qrMajor}'
        qr_img = qrcode.make(QRText)
        qr_img.save('./final/save.png')

        img = QPixmap('./final/save.png')
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
        uic.loadUi('./final/findId.ui', self)
        self.setWindowIcon(QIcon('./final/find.png'))
        self.show()
        self.txtName.returnPressed.connect(self.txtNameReturned)
        self.txtBirthYear.returnPressed.connect(self.txtBirthYearReturned)
        self.txtPhone.returnPressed.connect(self.txtPhoneReturned)
        self.btnHome.clicked.connect(self.btnHomeClicked)
        self.btnFind.clicked.connect(self.btnFindClicked)

    def txtNameReturned(self):
        self.btnFindClicked()

    def txtBirthYearReturned(self):
        self.btnFindClicked()

    def txtPhoneReturned(self):
        self.btnFindClicked()

    def btnFindClicked(self): # 찾기
        self.conn = pymysql.connect(host='210.119.12.57', user ='root', password='12345',
                            db = 'campusdb', charset='utf8')
       
        name = self.txtName.text()
        birthYear = self.txtBirthYear.text()
        result = self.lblfindID.text()
        phone = self.txtPhone.text()

        if name == '' or birthYear == '' or phone == '':
            QMessageBox.warning(self, '주의', '이름, 생년월일, 전화번호를 입력하세요')
            return
        else:
            query = '''SELECT studentID
                         FROM studenttbl
                        WHERE studentName = %s
                          AND birthday = %s
                          AND phoneNum = %s
                        '''
        try:
            cur = self.conn.cursor()
            cur.execute(query, (name, birthYear, phone))
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
       uic.loadUi('./final/findPw.ui', self)
       self.setWindowIcon(QIcon('./final/find.png'))
       self.show()  
       self.txtPwstID.setFocus()
       self.btnPwtoHome.clicked.connect(self.btnPwtoHomeClicked)
       self.btnFindPw.clicked.connect(self.btnFindPwClicked)
       self.txtPwstID.returnPressed.connect(self.txtPwstIDReturned)
       self.txtPwName.returnPressed.connect(self.txtPwNameReturned)
       self.txtPwPhone.returnPressed.connect(self.txtPwPhoneReturned)

    def txtPwstIDReturned(self):
        self.btnFindPwClicked()

    def txtPwNameReturned(self):
        self.btnFindPwClicked()

    def txtPwPhoneReturned(self):
        self.btnFindPwClicked()
        

    def btnFindPwClicked(self):
        PwstID = self.txtPwstID.text()
        PwPhone = self.txtPwPhone.text()
        name = self.txtPwName.text()
        if PwstID == '' or PwPhone == '' or name =='':
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
                        AND phoneNum = %s'''
            cur.execute(query, (PwstID, name, PwPhone))
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

class qtNew(QWidget):
    conn = None
    curIdx = 0

    def __init__(self):
        super().__init__()
        uic.loadUi('./final/signup.ui', self)
        #self.setWindowIcon(QIcon('./studyPyQt/address-book.png')) # 아이콘
        self.show()
        self.setWindowTitle('새로운 학생 추가')

        #버튼 시그널/슬롯함수 지정
        self.btnSignUp.clicked.connect(self.btnSignUpClicked)

    def btnSignUpClicked(self): # 회원가입 버튼 누를 경우
        # DB 정보가져오기
        self.conn = pymysql.connect(host='210.119.12.57', user='root', password='12345',
                                    db ='campusdb', charset='utf8')
        cur = self.conn.cursor()
        now = datetime.datetime.now()
        
        name = self.txtname.text()
        pw = self.txtpasswd.text()
        pwConfirm = self.txtpasswd_2.text()        
        phone = self.txtphone.text()
        address = self.txtaddress.text()
        gender = self.txtgender.text()
        birthday = self.txtbirthday.text()

        try:
            majorQ = '''SELECT majorid, name
                        FROM major'''
            cur.execute(majorQ)
            # majorList = cur.fetchall()
            one_text = self.majorBox.currentText()
            major = one_text[0]
            print(one_text)
            print(major)
            print(type(major))

            #major = self.majorBox.text()
            # for i in range:
            #     majorList[i] = i
            
            # self.majorBox = QComboBox(self)
            # for i in range(0, self.majorBox):
            #     self.majorBox.addItem(majorQ[i])

            Year = now.year
            studentID = int(f'{Year}0{major}00')

            if pw != pwConfirm:
                QMessageBox.warning(self, '주의', '비밀번호가 일치하지 않습니다.')
                return # 진행불가 

            veri = '''SELECT studentID
                        FROM logintbl'''
            cur.execute(veri)
            rows = cur.fetchall()

            for i in range(0, len(rows)):
                if rows[i][0] == studentID:
                    studentID += 1
                    

            if name == '' or major == '' or phone == '' or address == '' or gender == '':
                QMessageBox.warning(self, '주의', '모든 정보를 입력하세요')
                return # 진행불가
            else:
                query_1 = '''INSERT INTO studenttbl(studentID, studentName, birthday, major, phoneNum, address, gender)
                             VALUES(%s, %s, %s, %s, %s, %s, %s)'''
                query_2 = '''INSERT INTO logintbl(studentID, password)
                             VALUES(%s, %s)'''

            cur.execute(query_1, (studentID, name, birthday, major, phone, address, gender))
            cur.execute(query_2, (studentID, pw))
            self.lblshowNum.setText(f'{name}의 학번은 {studentID} 입니다.')

            self.conn.commit()# 빼먹지 말 것
            self.conn.close()

            QMessageBox.about(self, '성공', '신규 데이터 저장 성공')  

        except Exception as e:
            QMessageBox.warning(self, '주의', '전화번호는 중복될 수 없습니다.')
            print(e)
            self.txtphone.setText('')
            




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = qtApp()
    ex.show()
    sys.exit(app.exec_())