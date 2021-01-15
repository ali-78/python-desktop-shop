# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddCustomer.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import atexit

def exit_handler():
    try:
        con = sqlite3.connect("file::memory:?cache=shared")
        cursor = con.cursor()
        cursor.execute("drop table if exists temp")
        cursor.execute("drop table if exists temp2")
        con.close()
    except:
        pass

atexit.register(exit_handler)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 700)
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(209, 62, 142, 255), stop:1 rgba(6, 77, 193, 255));")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 2, 1, 1, 1)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setMinimumSize(QtCore.QSize(600, 600))
        self.widget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 12px;")
        self.widget.setObjectName("widget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setMinimumSize(QtCore.QSize(0, 150))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("font: 75 30pt \"Arial\";")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_3.addWidget(self.label_6)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 40))
        self.label_2.setStyleSheet("font: 12pt \"Arial\";\n"
"color: rgb(255, 0, 0);")
        self.label_2.setText("")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.label_1 = QtWidgets.QLabel(self.widget)
        self.label_1.setMinimumSize(QtCore.QSize(0, 60))
        self.label_1.setStyleSheet("font: 14pt \"Arial\";\n"
"margin: 0 20px;")
        self.label_1.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_1.setObjectName("label_1")
        self.verticalLayout_3.addWidget(self.label_1)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("margin: 0 25px;\n"
"padding-left: 10px;\n"
"background-color: rgb(250, 250, 250);\n"
"border: 1px solid rgb(150, 150, 150);\n"
"border-radius: 5px;")
        self.lineEdit.setMaxLength(100)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_3.addWidget(self.lineEdit)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem4)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("margin: 0px 130px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(68, 134, 247);\n"
"border-radius: 30px;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.Submit)
        self.verticalLayout_3.addWidget(self.pushButton)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem5)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.gridLayout.addWidget(self.widget, 1, 1, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(50, 50))
        self.pushButton_2.setMaximumSize(QtCore.QSize(50, 50))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(209, 62, 142, 255), stop:1 rgba(6, 77, 193, 255));\n"
"border-radius: 25px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(6, 77, 193, 255), stop:1 rgba(209, 62, 142, 255));\n"
"}")
        self.pushButton_2.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons8-back-filled-50.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_2.clicked.connect(self.sellPageClick)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.cusCode = 0

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Add Customer"))
        self.label_6.setText(_translate("MainWindow", "Add Customer"))
        self.label_1.setText(_translate("MainWindow", "Customer Name"))
        self.pushButton.setText(_translate("MainWindow", "Add Customer"))

    def sellPageClick(self):
        try:
            con = sqlite3.connect("file::memory:?cache=shared")
            con.isolation_level = None
            cursor = con.cursor()
            cursor.execute("insert into temp(customerCode) values(?)", (self.cusCode,))
        except:
            pass
        finally:
            con.close()

        self.MainWindow.close()
        self.show_sell()

    def show_sell(self):
        from link import sellpage

        self.sell_window = QtWidgets.QMainWindow()
        self.sell_ui = sellpage()
        self.sell_ui.setupUi(self.sell_window)
        self.sell_window.show()

    def Submit(self):
        try:
            if (self.lineEdit.text() == ""):
                self.label_2.setText("Please enter the customer name")
                return
            con = sqlite3.connect("uniDB")
            cursor = con.cursor()
            cursor.execute("select max(id) from account")
            maxid = cursor.fetchall()
            if (maxid[0][0] == None):
                id = 1
            else:
                id = maxid[0][0] + 1
            cursor.execute('select max(code) from account where userType = "customer"')
            maxCode = cursor.fetchall()
            if (maxCode[0][0] == None):
                code = 1
            else:
                code = maxCode[0][0] + 1
            values = (id,code,self.lineEdit.text(),1111,"customer")
            cursor.execute("insert into account values(?,?,?,?,?)", values)
            con.commit()
            con.close()
            self.cusCode = code
            self.label_2.setStyleSheet("color: green")
            self.label_2.setText("The customer has be added :))")
        except:
            self.label_2.setStyleSheet("color: red")
            self.label_2.setText("The customer has been added before!!!")
        



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
