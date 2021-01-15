# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FactorList.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

import sqlite3

from PyQt5 import QtCore, QtGui, QtWidgets
import atexit

def exit_handler():
    try:
        con = sqlite3.connect("file::memory:?cache=shared")
        cursor = con.cursor()
        cursor.execute("drop table if exists user")
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
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.clicked.connect(self.Home)
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
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 1, 1, 1)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setMinimumSize(QtCore.QSize(1000, 600))
        self.widget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 12px;")
        self.widget.setObjectName("widget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setMinimumSize(QtCore.QSize(0, 120))
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
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setMinimumSize(QtCore.QSize(0, 50))
        self.label.setMaximumSize(QtCore.QSize(16777215, 40))
        self.label.setStyleSheet("font: 12pt \"Arial\";\n"
"color: rgb(255, 0, 0);")
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.widget)
        self.tableWidget.setMinimumSize(QtCore.QSize(600, 450))
        self.tableWidget.setMaximumSize(QtCore.QSize(600, 450))
        self.tableWidget.setStyleSheet("border: 1px solid rgb(150, 150, 150);\n"
"border-radius: 5px;")
        self.tableWidget.setLineWidth(1)
        self.tableWidget.setMidLineWidth(2)
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(93)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(49)
        self.horizontalLayout.addWidget(self.tableWidget)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setMinimumSize(QtCore.QSize(185, 60))
        self.label_3.setMaximumSize(QtCore.QSize(185, 16777215))
        self.label_3.setStyleSheet("font: 12pt \"Arial\";\n"
"margin: 0 0 0 20px;")
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_6.addWidget(self.label_3)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setMinimumSize(QtCore.QSize(150, 35))
        self.lineEdit.setMaximumSize(QtCore.QSize(500, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("padding-left: 10px;\n"
"background-color: rgb(250, 250, 250);\n"
"border: 1px solid rgb(150, 150, 150);\n"
"border-radius: 5px;")
        self.lineEdit.setMaxLength(100)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_6.addWidget(self.lineEdit)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.clicked.connect(self.Find)
        self.pushButton.setMinimumSize(QtCore.QSize(170, 70))
        self.pushButton.setMaximumSize(QtCore.QSize(500, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("margin: 20px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(68, 134, 247);\n"
"border-radius: 5px;")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_1 = QtWidgets.QLabel(self.widget)
        self.label_1.setMinimumSize(QtCore.QSize(185, 60))
        self.label_1.setMaximumSize(QtCore.QSize(185, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_1.setFont(font)
        self.label_1.setStyleSheet("font: 12pt \"Arial\";\n"
"margin: 0 0 0 20px;")
        self.label_1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_1.setObjectName("label_1")
        self.horizontalLayout_4.addWidget(self.label_1)
        self.comboBox_1 = QtWidgets.QComboBox(self.widget)
        self.comboBox_1.setMinimumSize(QtCore.QSize(150, 35))
        self.comboBox_1.setMaximumSize(QtCore.QSize(650, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.comboBox_1.setFont(font)
        self.comboBox_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboBox_1.setStyleSheet("background-color: rgb(250, 250, 250);\n"
"border: 1px solid rgb(150, 150, 150);\n"
"border-radius: 5px;\n"
"color:black;")
        self.comboBox_1.setFrame(False)
        self.comboBox_1.setObjectName("comboBox_1")
        self.horizontalLayout_4.addWidget(self.comboBox_1)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem6)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setMinimumSize(QtCore.QSize(185, 60))
        self.label_2.setMaximumSize(QtCore.QSize(185, 16777215))
        self.label_2.setStyleSheet("font: 12pt \"Arial\";\n"
"margin: 0 0 0 20px;")
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.comboBox_2 = QtWidgets.QComboBox(self.widget)
        self.comboBox_2.setMinimumSize(QtCore.QSize(150, 35))
        self.comboBox_2.setMaximumSize(QtCore.QSize(5000, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboBox_2.setStyleSheet("background-color: rgb(250, 250, 250);\n"
"border: 1px solid rgb(150, 150, 150);\n"
"border-radius: 5px;\n"
"color:black;")
        self.comboBox_2.setFrame(False)
        self.comboBox_2.setObjectName("comboBox_2")
        self.horizontalLayout_5.addWidget(self.comboBox_2)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem7)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem8)
        self.pushButton_1 = QtWidgets.QPushButton(self.widget)
        self.pushButton_1.clicked.connect(self.Sort)
        self.pushButton_1.setMinimumSize(QtCore.QSize(170, 70))
        self.pushButton_1.setMaximumSize(QtCore.QSize(500, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.pushButton_1.setFont(font)
        self.pushButton_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_1.setStyleSheet("margin: 20px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(68, 134, 247);\n"
"border-radius: 5px;")
        self.pushButton_1.setObjectName("pushButton_1")
        self.horizontalLayout_3.addWidget(self.pushButton_1)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem9)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem10)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.gridLayout.addWidget(self.widget, 1, 1, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem11, 1, 2, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem12, 1, 0, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem13, 0, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.userType = ""

        try:
            con = sqlite3.connect("uniDB")
            cursor = con.cursor()
            cursor.execute("select name from account where userType = \"salesManager\"")
            productsName = cursor.fetchall()
            self.comboBox_1.addItem("")
            self.comboBox_1.setItemText(0, "All SalesManagers")
            i = 1 
            for item in productsName:
                self.comboBox_1.addItem("")
                self.comboBox_1.setItemText(i, item[0])
                i = i + 1
            con.close()
        except:
            self.label.setText("Datas can't be loaded")

        try:
            con = sqlite3.connect("uniDB")
            cursor = con.cursor()
            cursor.execute("select name from account where userType = \"customer\"")
            productsName = cursor.fetchall()
            self.comboBox_2.addItem("")
            self.comboBox_2.setItemText(0, "All Customers")
            i = 1 
            for item in productsName:
                self.comboBox_2.addItem("")
                self.comboBox_2.setItemText(i, item[0])
                i = i + 1
            con.close()
        except:
            self.label.setText("Data can't be loaded")

        try:
            db = sqlite3.connect("file::memory:?cache=shared")
            cursor = db.cursor()
            cursor.execute("select * from user")
            value = cursor.fetchall()
            self.userType = value[0][0]
            cursor.execute("drop table temp")
        except:
            pass
        finally:
            db.close()


        try:
            con = sqlite3.connect("uniDB")
            cursor = con.cursor()
            cursor.execute("select * from factorList")
            factorList = cursor.fetchall()
            self.tableWidget.setRowCount(len(factorList))
            i = 0
            for row in factorList:
                item = QtWidgets.QTableWidgetItem()
                item.setText(str(row[0]))
                item.setFlags(QtCore.Qt.ItemIsEnabled)
                self.tableWidget.setItem(i, 0, item)
                item = QtWidgets.QTableWidgetItem()
                item.setText(str(row[1]))
                item.setFlags(QtCore.Qt.ItemIsEnabled)
                self.tableWidget.setItem(i, 1, item)
                item = QtWidgets.QTableWidgetItem()
                item.setText(str(row[2]))
                item.setFlags(QtCore.Qt.ItemIsEnabled)
                self.tableWidget.setItem(i, 2, item)
                item = QtWidgets.QTableWidgetItem()
                item.setText(row[3])
                item.setFlags(QtCore.Qt.ItemIsEnabled)
                self.tableWidget.setItem(i, 3, item)
                item = QtWidgets.QTableWidgetItem()
                item.setText(row[4])
                item.setFlags(QtCore.Qt.ItemIsEnabled)
                self.tableWidget.setItem(i, 4, item)
                item = QtWidgets.QTableWidgetItem()
                item.setText(str(row[5]))
                item.setFlags(QtCore.Qt.ItemIsEnabled)
                self.tableWidget.setItem(i, 5, item)
                i = i + 1
        except:
            self.label.styleSheet("color:red;")
            self.label.setText("Data hasn't been found!!!")
        finally:
            con.close

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Factor List"))
        self.label_6.setText(_translate("MainWindow", "Factor list"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Factor Code"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Customer"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Admin"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Date"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Time"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Total Price"))
        self.label_3.setText(_translate("MainWindow", "Enter Factor code"))
        self.pushButton.setText(_translate("MainWindow", "Find"))
        self.label_1.setText(_translate("MainWindow", "Enter Admin Name"))
        self.label_2.setText(_translate("MainWindow", "Enter Customer Name"))
        self.pushButton_1.setText(_translate("MainWindow", "Find"))

    def Sort(self):

        if (self.comboBox_1.currentText() != "All SalesManagers" and self.comboBox_2.currentText() == "All Customers"):
            try:
                con = sqlite3.connect("uniDB")
                cursor = con.cursor()
                cursor.execute("select code from account where name = ?",(self.comboBox_1.currentText(),))
                manager = cursor.fetchall()
                cursor.execute("select * from factorList where adminCode = ?", (manager[0][0],))
                data = cursor.fetchall()

                self.tableWidget.setRowCount(len(data))
                i = 0
                for row in data:
                    item = QtWidgets.QTableWidgetItem()
                    item.setText(str(row[0]))
                    item.setFlags(QtCore.Qt.ItemIsEnabled)
                    self.tableWidget.setItem(i, 0, item)
                    item = QtWidgets.QTableWidgetItem()
                    item.setText(str(row[1]))
                    item.setFlags(QtCore.Qt.ItemIsEnabled)
                    self.tableWidget.setItem(i, 1, item)
                    item = QtWidgets.QTableWidgetItem()
                    item.setText(str(row[2]))
                    item.setFlags(QtCore.Qt.ItemIsEnabled)
                    self.tableWidget.setItem(i, 2, item)
                    item = QtWidgets.QTableWidgetItem()
                    item.setText(row[3])
                    item.setFlags(QtCore.Qt.ItemIsEnabled)
                    self.tableWidget.setItem(i, 3, item)
                    item = QtWidgets.QTableWidgetItem()
                    item.setText(row[4])
                    item.setFlags(QtCore.Qt.ItemIsEnabled)
                    self.tableWidget.setItem(i, 4, item)
                    item = QtWidgets.QTableWidgetItem()
                    item.setText(str(row[5]))
                    item.setFlags(QtCore.Qt.ItemIsEnabled)
                    self.tableWidget.setItem(i, 5, item)
                    i = i + 1
                self.label.setStyleSheet("color:green;")
                self.label.setText("Data has been sorted by saleManager {0}".format(self.comboBox_1.currentText(),))        
            except:
                self.label.setStyleSheet("color:red;")
                self.label.setText("Data hasn't been found!!!")
        elif (self.comboBox_1.currentText() == "All SalesManagers" and self.comboBox_2.currentText() != "All Customers"):
            try:
                con = sqlite3.connect("uniDB")
                cursor = con.cursor()
                cursor.execute("select code from account where name = ?",(self.comboBox_2.currentText(),))
                customer = cursor.fetchall()
                cursor.execute("select * from factorList where customerCode = ?", (customer[0][0],))
                data = cursor.fetchall()

                self.tableWidget.setRowCount(len(data))
                i = 0
                for row in data:
                    item = QtWidgets.QTableWidgetItem()
                    item.setText(str(row[0]))
                    item.setFlags(QtCore.Qt.ItemIsEnabled)
                    self.tableWidget.setItem(i, 0, item)
                    item = QtWidgets.QTableWidgetItem()
                    item.setText(str(row[1]))
                    item.setFlags(QtCore.Qt.ItemIsEnabled)
                    self.tableWidget.setItem(i, 1, item)
                    item = QtWidgets.QTableWidgetItem()
                    item.setText(str(row[2]))
                    item.setFlags(QtCore.Qt.ItemIsEnabled)
                    self.tableWidget.setItem(i, 2, item)
                    item = QtWidgets.QTableWidgetItem()
                    item.setText(row[3])
                    item.setFlags(QtCore.Qt.ItemIsEnabled)
                    self.tableWidget.setItem(i, 3, item)
                    item = QtWidgets.QTableWidgetItem()
                    item.setText(row[4])
                    item.setFlags(QtCore.Qt.ItemIsEnabled)
                    self.tableWidget.setItem(i, 4, item)
                    item = QtWidgets.QTableWidgetItem()
                    item.setText(str(row[5]))
                    item.setFlags(QtCore.Qt.ItemIsEnabled)
                    self.tableWidget.setItem(i, 5, item)
                    i = i + 1
                self.label.setStyleSheet("color:green;")
                self.label.setText("Data has been sorted by customer {0}".format(self.comboBox_2.currentText(),)) 
            except:
                self.label.setStyleSheet("color:red;")
                self.label.setText("Data hasn't been found!!!")
        
        elif (self.comboBox_1.currentText() == "All SalesManagers" and self.comboBox_2.currentText() == "All Customers"):
            try:
                con = sqlite3.connect("uniDB")
                cursor = con.cursor()
                cursor.execute("select * from factorList")
                factorList = cursor.fetchall()
                self.tableWidget.setRowCount(len(factorList))
                i = 0
                for row in factorList:
                    item = QtWidgets.QTableWidgetItem()
                    item.setText(str(row[0]))
                    item.setFlags(QtCore.Qt.ItemIsEnabled)
                    self.tableWidget.setItem(i, 0, item)
                    item = QtWidgets.QTableWidgetItem()
                    item.setText(str(row[1]))
                    item.setFlags(QtCore.Qt.ItemIsEnabled)
                    self.tableWidget.setItem(i, 1, item)
                    item = QtWidgets.QTableWidgetItem()
                    item.setText(str(row[2]))
                    item.setFlags(QtCore.Qt.ItemIsEnabled)
                    self.tableWidget.setItem(i, 2, item)
                    item = QtWidgets.QTableWidgetItem()
                    item.setText(row[3])
                    item.setFlags(QtCore.Qt.ItemIsEnabled)
                    self.tableWidget.setItem(i, 3, item)
                    item = QtWidgets.QTableWidgetItem()
                    item.setText(row[4])
                    item.setFlags(QtCore.Qt.ItemIsEnabled)
                    self.tableWidget.setItem(i, 4, item)
                    item = QtWidgets.QTableWidgetItem()
                    item.setText(str(row[5]))
                    item.setFlags(QtCore.Qt.ItemIsEnabled)
                    self.tableWidget.setItem(i, 5, item)
                    i = i + 1
                self.label.setStyleSheet("color:green;")
                self.label.setText("All data has been reloaded:))") 
            except:
                self.label.setStyleSheet("color:red;")
                self.label.setText("Data hasn't been found!!!")
            finally:
                con.close
        
        else:
            try:
                con = sqlite3.connect("uniDB")
                cursor = con.cursor()
                cursor.execute("select code from account where name = ?",(self.comboBox_1.currentText(),))
                manager = cursor.fetchall()
                cursor.execute("select code from account where name = ?",(self.comboBox_2.currentText(),))
                customer = cursor.fetchall()
                cursor.execute("select * from factorList where adminCode = ? and customerCode = ?", (manager[0][0],customer[0][0]))
                data = cursor.fetchall()

                self.tableWidget.setRowCount(len(data))
                i = 0
                for row in data:
                    item = QtWidgets.QTableWidgetItem()
                    item.setText(str(row[0]))
                    item.setFlags(QtCore.Qt.ItemIsEnabled)
                    self.tableWidget.setItem(i, 0, item)
                    item = QtWidgets.QTableWidgetItem()
                    item.setText(str(row[1]))
                    item.setFlags(QtCore.Qt.ItemIsEnabled)
                    self.tableWidget.setItem(i, 1, item)
                    item = QtWidgets.QTableWidgetItem()
                    item.setText(str(row[2]))
                    item.setFlags(QtCore.Qt.ItemIsEnabled)
                    self.tableWidget.setItem(i, 2, item)
                    item = QtWidgets.QTableWidgetItem()
                    item.setText(row[3])
                    item.setFlags(QtCore.Qt.ItemIsEnabled)
                    self.tableWidget.setItem(i, 3, item)
                    item = QtWidgets.QTableWidgetItem()
                    item.setText(row[4])
                    item.setFlags(QtCore.Qt.ItemIsEnabled)
                    self.tableWidget.setItem(i, 4, item)
                    item = QtWidgets.QTableWidgetItem()
                    item.setText(str(row[5]))
                    item.setFlags(QtCore.Qt.ItemIsEnabled)
                    self.tableWidget.setItem(i, 5, item)
                    i = i + 1
                self.label.setStyleSheet("color:green;")
                self.label.setText("Data has been sorted by saleManager {0} and customer {1}".format(self.comboBox_1.currentText(),self.comboBox_2.currentText())) 
            except:
                self.label.setStyleSheet("color:red;")
                self.label.setText("Data hasn't been found!!!")

    def Find(self):
        try:
            row = int(self.lineEdit.text()) - 1
            values = (self.tableWidget.item(row,0).text(),self.tableWidget.item(row,1).text(),self.tableWidget.item(row,2).text(),self.tableWidget.item(row,3).text(),self.tableWidget.item(row,4).text(),self.tableWidget.item(row,5).text())
            con = sqlite3.connect("file::memory:?cache=shared")
            con.isolation_level = None
            cursor = con.cursor()
            cursor.execute("create table factorRow(facId,customerCode,adminCode,date,time,totalPrice)")
            cursor.execute("insert into factorRow(facId,customerCode,adminCode,date,time,totalPrice) values(?,?,?,?,?,?)", values)
            con.commit()
            con.close()

            self.MainWindow.close()
            self.show_factor()
        except ValueError:
            self.label.setText("Please enter the correct format!!!")
        except:
            pass

    def show_factor(self):
        from link import factor
        self.fac_window = QtWidgets.QMainWindow()
        self.fac_ui = factor()
        self.fac_ui.setupUi(self.fac_window)
        self.fac_window.show()

    def Home(self):
        try:
            con = sqlite3.connect("file::memory:?cache=shared")
            cursor = con.cursor()
            cursor.execute("drop table if exists user")
            con.close()
        except:
            pass

        if (self.userType == "sellManager"):
            self.MainWindow.close()
            self.show_sell()
        else:
            self.MainWindow.close()
            self.show_store()

    def show_sell(self):
        from link import sellpage
        self.sell_window = QtWidgets.QMainWindow()
        self.sell_ui = sellpage()
        self.sell_ui.setupUi(self.sell_window)
        self.sell_window.show()
    
    def show_store(self):
        from link import storepage
        self.store_window = QtWidgets.QMainWindow()
        self.store_ui = storepage()
        self.store_ui.setupUi(self.store_window)
        self.store_window.show()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
