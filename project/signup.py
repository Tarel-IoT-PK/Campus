import sys 
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import pymysql
import datetime

class qtApp(QMainWindow):
    conn = None
    curIdx = 0

    def __init__(self):
        super().__init__()
        uic.loadUi('./project/signup.ui', self)
        #self.setWindowIcon(QIcon('./studyPyQt/address-book.png')) # 아이콘
        self.setWindowTitle('새로운 학생 추가')

        #버튼 시그널/슬롯함수 지정
        self.btnSignUp.clicked.connect(self.btnSignUpClicked)

    def btnSignUpClicked(self): # 회원가입 버튼 누를 경우
        # DB 정보가져오기
        self.conn = pymysql.connect(host='localhost', user='root', password='12345',
                                    db ='campusdb', charset='utf8')
        cur = self.conn.cursor()
        now = datetime.datetime.now()

        try:
            name = self.txtname.text()
            pw = self.txtpasswd.text()
            major = self.txtmajor.text()
            phone = self.txtphone.text()
            address = self.txtaddress.text()
            gender = self.txtgender.text()
            birthday = self.txtbirthday.text()

            Year = now.year
            studentID = int(f'{Year}0{major}00')

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

            self.conn.commit()# 빼먹지 말 것
            self.conn.close()

            QMessageBox.about(self, '성공', '신규 데이터 저장 성공')  

        except Exception as e:
            QMessageBox.warning(self, '주의', '에러 발생, 로그 참조')
            print(e)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = qtApp()
    ex.show()
    sys.exit(app.exec_())