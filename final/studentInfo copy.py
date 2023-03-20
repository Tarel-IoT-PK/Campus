import sys 
from PyQt5 import uic
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import pymysql


class qtApp(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('./final/studentInfo.ui', self)
        self.setWindowTitle('학생명부 v0.5')
        self.btnInfo.clicked.connect(self.btnInfoClicked)
        self.btnSearch.clicked.connect(self.btnSearchClicked)

        self.txtSearch.returnPressed.connect(self.txtSearchClicked)


    def btnInfoClicked(self):
        self.initDB()

    def txtSearchClicked(self):# 단축키 엔터
        self.btnSearchClicked()

    def initDB(self):
        self.conn = pymysql.connect(host='210.119.12.57', user='root', password='12345',
                                    db ='campusdb', charset='utf8')
        cur = self.conn.cursor()
        query = '''SELECT studentID
                        , studentName
                        , birthday
                        , major
                        , phoneNum
                        , address
                        , gender
                    FROM studenttbl '''
        cur.execute(query)
        rows = cur.fetchall()

        self.makeTable(rows)
        self.conn.close() # 프로그램 종료할 때

    def makeTable(self, rows):
        self.tblInfo.setColumnCount(7)
        self.tblInfo.setRowCount(len(rows))
        self.tblInfo.setHorizontalHeaderLabels(['학번', '이름', '생년월일', '전공', '핸드폰', '주소', '성별'])
        self.tblInfo.setColumnWidth(0, 80)
        self.tblInfo.setColumnWidth(1, 60)
        self.tblInfo.setColumnWidth(2, 70)
        self.tblInfo.setColumnWidth(3, 100)
        self.tblInfo.setColumnWidth(4, 100)
        self.tblInfo.setColumnWidth(5, 200)
        self.tblInfo.setColumnWidth(6, 20)
        self.tblInfo.setEditTriggers(QAbstractItemView.NoEditTriggers)

        for i,row in enumerate(rows):
            print(row)
            studentId = row[0]
            name = row[1]
            birthday = row[2]
            major = row[3]
            phoneNum = row[4]
            Address = row[5]
            Gender = row[6]

            self.tblInfo.setItem(i, 0, QTableWidgetItem(str(studentId)))
            self.tblInfo.setItem(i, 1, QTableWidgetItem(name))
            self.tblInfo.setItem(i, 2, QTableWidgetItem(birthday))
            self.tblInfo.setItem(i, 3, QTableWidgetItem(major))
            self.tblInfo.setItem(i, 4, QTableWidgetItem(phoneNum))
            self.tblInfo.setItem(i, 5, QTableWidgetItem(Address))
            self.tblInfo.setItem(i, 6, QTableWidgetItem(Gender))

    def btnSearchClicked(self):
        self.conn = pymysql.connect(host='210.119.12.57', user='root', password='12345',
                                    db ='campusdb', charset='utf8')
        cur = self.conn.cursor()
        
        search_term = self.txtSearch.text()
        query = f"""SELECT * FROM studenttbl
                    WHERE studentName LIKE '%{search_term}%'"""
        cur.execute(query)


        # 결과 출력
        results = cur.fetchall()
        self.makeTable(results)


        # 연결 종료
        self.conn.close()
        print()









if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = qtApp()
    ex.show()
    sys.exit(app.exec_())