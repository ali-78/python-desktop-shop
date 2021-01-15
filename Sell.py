# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Sell.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

import sqlite3
import jdatetime
import threading
from time import time,sleep
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.listRow = 0  # for AddToList()
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
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_35 = QtWidgets.QLabel(self.widget)
        self.label_35.setMinimumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_35.setFont(font)
        self.label_35.setStyleSheet("margin: 0 20px;")
        self.label_35.setObjectName("label_35")
        self.gridLayout_5.addWidget(self.label_35, 1, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setMinimumSize(QtCore.QSize(300, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: rgb(250, 250, 250);\n"
"border: 1px solid rgb(150, 150, 150);\n"
"border-radius: 5px;")
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_5.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.label_45 = QtWidgets.QLabel(self.widget)
        self.label_45.setMinimumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_45.setFont(font)
        self.label_45.setStyleSheet("margin: 0 20px;")
        self.label_45.setObjectName("label_45")
        self.gridLayout_5.addWidget(self.label_45, 0, 0, 1, 1)
        self.label_56 = QtWidgets.QLabel(self.widget)
        self.label_56.setMinimumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_56.setFont(font)
        self.label_56.setStyleSheet("margin: 0 20px;")
        self.label_56.setObjectName("label_56")
        self.gridLayout_5.addWidget(self.label_56, 2, 0, 1, 1)
        self.label_85 = QtWidgets.QLabel(self.widget)
        self.label_85.setMinimumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_85.setFont(font)
        self.label_85.setStyleSheet("margin: 0 20px;")
        self.label_85.setObjectName("label_85")
        self.gridLayout_5.addWidget(self.label_85, 3, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(300, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color: rgb(250, 250, 250);\n"
"border: 1px solid rgb(150, 150, 150);\n"
"border-radius: 5px;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_5.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_4.setMinimumSize(QtCore.QSize(300, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("background-color: rgb(250, 250, 250);\n"
"border: 1px solid rgb(150, 150, 150);\n"
"border-radius: 5px;")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout_5.addWidget(self.lineEdit_4, 3, 1, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.widget)
        self.pushButton_4.clicked.connect(self.addToList)
        self.pushButton_4.setMinimumSize(QtCore.QSize(0, 75))
        self.pushButton_4.setMaximumSize(QtCore.QSize(170, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(68, 134, 247);\n"
"border-radius: 5px;\n"
"margin: 20px 0px 20px 20px;")
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_5.addWidget(self.pushButton_4, 4, 1, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.widget)
        self.pushButton_5.clicked.connect(self.done)
        self.pushButton_5.setMinimumSize(QtCore.QSize(0, 75))
        self.pushButton_5.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_5.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(68, 134, 247);\n"
"border-radius: 5px;\n"
"margin: 20px 0 20px 80px;")
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_5.addWidget(self.pushButton_5, 4, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.widget)
        self.comboBox.setMinimumSize(QtCore.QSize(300, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("background-color: rgb(250, 250, 250);\n"
"border: 1px solid rgb(150, 150, 150);\n"
"border-radius: 5px\n;"
"color: black")
        self.comboBox.setFrame(False)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout_5.addWidget(self.comboBox, 2, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_5)
        self.tableWidget = QtWidgets.QTableWidget(self.widget)
        self.tableWidget.setStyleSheet("border: 1px solid rgb(150, 150, 150);\n"
"border-radius: 5px;")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(1)
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
        self.tableWidget.horizontalHeader().setDefaultSectionSize(220)
        self.verticalLayout.addWidget(self.tableWidget)
        self.horizontalLayout.addLayout(self.verticalLayout)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setMinimumSize(QtCore.QSize(0, 80))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("margin: 0 70px;")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_5.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("margin: 0 70px;")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_5.addWidget(self.label_5)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem3)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem4, 3, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem5, 5, 1, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.clicked.connect(self.addCustomer)
        self.pushButton_2.setMinimumSize(QtCore.QSize(200, 35))
        self.pushButton_2.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(68, 134, 247);\n"
"border-radius: 5px;")
        self.pushButton_2.setFlat(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_4.addWidget(self.pushButton_2, 4, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.clicked.connect(self.financialPage)
        self.pushButton_3.setMinimumSize(QtCore.QSize(0, 35))
        self.pushButton_3.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(68, 134, 247);\n"
"border-radius: 5px;")
        self.pushButton_3.setFlat(False)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_4.addWidget(self.pushButton_3, 2, 1, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem6, 2, 2, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem7, 2, 0, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem8, 1, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 35))
        self.pushButton.setMaximumSize(QtCore.QSize(5555, 35))
        self.pushButton.clicked.connect(self.factorList)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(68, 134, 247);\n"
"border-radius: 5px;")
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_4.addWidget(self.pushButton, 0, 1, 1, 1)
        self.verticalLayout_5.addLayout(self.gridLayout_4)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem9 = QtWidgets.QSpacerItem(30, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem9, 0, 1, 1, 1)
        self.pushButton_1 = QtWidgets.QPushButton(self.widget)
        self.pushButton_1.clicked.connect(self.DeleteFromList)
        self.pushButton_1.setMinimumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.pushButton_1.setFont(font)
        self.pushButton_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_1.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(68, 134, 247);\n"
"border-radius: 5px;")
        self.pushButton_1.setFlat(False)
        self.pushButton_1.setObjectName("pushButton_1")
        self.gridLayout_3.addWidget(self.pushButton_1, 0, 0, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_5.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setStyleSheet("background-color: rgb(250, 250, 250);\n"
"border: 1px solid rgb(150, 150, 150);\n"
"border-radius: 5px;")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout_3.addWidget(self.lineEdit_5, 0, 2, 1, 1)
        self.verticalLayout_5.addLayout(self.gridLayout_3)
        self.horizontalLayout.addLayout(self.verticalLayout_5)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem10)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
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

        threading.Thread(target=self.setTime,daemon=True).start()
        
        try:
            con = sqlite3.connect("uniDB")
            cursor = con.cursor()
            cursor.execute("select name from products")
            productsName = cursor.fetchall()
            i = 0 
            for item in productsName:
                self.comboBox.addItem("")
                self.comboBox.setItemText(i, item[0])
                i = i + 1
            con.close()
        except:
            self.label.setText("Datas can't be loaded")

        self.label_4.setText(str(jdatetime.datetime.now().date()))

        try:
            con = sqlite3.connect("file::memory:?cache=shared")
            cursor = con.cursor()
            cursor.execute("select * from temp")
            code = cursor.fetchall()
            self.lineEdit.setText(str(code[1][0]))
            self.lineEdit_2.setText(code[0][1])
            cursor.execute("drop table temp")
            cursor.execute("select * from temp2")
            rows = cursor.fetchall()
            cursor.execute("drop table temp2")
            self.tableWidget.setRowCount(len(rows[0]))
            i = 0
            for row in rows:
                item = QtWidgets.QTableWidgetItem()
                item.setText(row[0])
                item.setFlags(QtCore.Qt.ItemIsEnabled)
                self.tableWidget.setItem(i, 0, item)
                item = QtWidgets.QTableWidgetItem()
                item.setText(row[1])
                item.setFlags(QtCore.Qt.ItemIsEnabled)
                self.tableWidget.setItem(i, 1, item)
                i = i + 1
        except:
            pass
        finally:
            con.close()


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.lineEdit, self.lineEdit_2)
        MainWindow.setTabOrder(self.lineEdit_2, self.comboBox)
        MainWindow.setTabOrder(self.comboBox, self.lineEdit_4)
        MainWindow.setTabOrder(self.lineEdit_4, self.pushButton_4)
        MainWindow.setTabOrder(self.pushButton_4, self.pushButton_5)
        MainWindow.setTabOrder(self.pushButton_5, self.pushButton)
        MainWindow.setTabOrder(self.pushButton, self.pushButton_3)
        MainWindow.setTabOrder(self.pushButton_3, self.pushButton_2)
        MainWindow.setTabOrder(self.pushButton_2, self.lineEdit_5)
        MainWindow.setTabOrder(self.lineEdit_5, self.pushButton_1)
        MainWindow.setTabOrder(self.pushButton_1, self.tableWidget)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sell"))
        self.label_6.setText(_translate("MainWindow", "Sell Page"))
        self.label_35.setText(_translate("MainWindow", "Admin Code"))
        self.label_45.setText(_translate("MainWindow", "Customer Code"))
        self.label_56.setText(_translate("MainWindow", "Product Name"))
        self.label_85.setText(_translate("MainWindow", "Product Number"))
        self.pushButton_4.setText(_translate("MainWindow", "Add to List"))
        self.pushButton_5.setText(_translate("MainWindow", "Done"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Product Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Product Number"))
        self.pushButton_2.setText(_translate("MainWindow", "Add New Customer"))
        self.pushButton_3.setText(_translate("MainWindow", "Financial Page"))
        self.pushButton.setText(_translate("MainWindow", "Factor List"))
        self.pushButton_1.setText(_translate("MainWindow", "Delete"))

    def setTime(self):
        while True:
            self.label_5.setText(str(jdatetime.datetime.now().time().replace(microsecond=0)))
            sleep(1)

    def addToList(self):
        self.label.setText("")
        try:
            value = int(self.lineEdit_4.text())
            
            if int(self.lineEdit_4.text()) <= 0:
                self.label.setText("Enter the number of product")
                return
            con = sqlite3.connect("uniDB")
            cursor = con.cursor()
            cursor.execute("select number from products where name = ?", (self.comboBox.currentText(),))
            productNumber = cursor.fetchall()
            if productNumber[0][0] < int(self.lineEdit_4.text()):
                self.label.setText("There isn't enough {0} to sell".format(self.comboBox.currentText()))
                con.close()
                return
            for i in range(self.tableWidget.rowCount()-1):
                if self.tableWidget.item(i, 0).text() == self.comboBox.currentText():
                    if int(self.tableWidget.item(i, 1).text()) + int(self.lineEdit_4.text()) > productNumber[0][0]:
                        self.label.setText("There isn't enough {0} to sell".format(self.comboBox.currentText()))
                        return
                    else:
                        self.tableWidget.item(i, 1).setText(str(int(self.tableWidget.item(i, 1).text()) + int(self.lineEdit_4.text())))
                        return
            item = QtWidgets.QTableWidgetItem()
            item.setText(self.comboBox.currentText())
            item.setFlags(QtCore.Qt.ItemIsEnabled)
            self.tableWidget.setItem(self.listRow, 0, item)
            item = QtWidgets.QTableWidgetItem()
            item.setText(self.lineEdit_4.text())
            item.setFlags(QtCore.Qt.ItemIsEnabled)
            self.tableWidget.setItem(self.listRow, 1, item)
            self.listRow = self.listRow + 1
            self.tableWidget.setRowCount(self.listRow +1)
            con.close()
        except ValueError:
            self.label.setText("You have used wrong format in prodectNumber field!!!")
        except:
            self.label.setText("Current product wasn't be added to list!!!")
    
    def done(self):
        status = ""
        listProduct = []
        totalPrice = 0

        try:
            con = sqlite3.connect("uniDB")

            test = int(self.lineEdit.text())
            test = int(self.lineEdit_2.text())

            cursor = con.cursor()
            cursor.execute("select name from account where code = ?", (self.lineEdit.text(),))
            v = cursor.fetchall()
            if (v == []):    
                self.label.setText("The customer wasn't registerated!!!")
                return
            cursor.execute("select name from account where code = ?", (self.lineEdit_2.text(),))
            v = cursor.fetchall()
            if (v == []):    
                self.label.setText("There isn't this admin code!!!")
                return
                
            cursor.execute("select max(id) from factorList")
            mid = cursor.fetchall()
            if (mid[0][0] == None):
                id1 = 1
            else:
                id1 = mid[0][0] + 1
            for i in range(self.tableWidget.rowCount() - 1):
                cursor.execute("select max(id) from factorProducts")
                mid2 = cursor.fetchall()
                if (mid2[0][0] == None):
                    id2 = 1
                else:
                    id2 = mid2[0][0] + 1
                cursor.execute("select price from products where name = ?", (self.tableWidget.item(i, 0).text(),))
                price = cursor.fetchall()
                totalPrice = totalPrice + (price[0][0] * int(self.tableWidget.item(i, 1).text()))

                cursor.execute("select number from products where name = ?", (self.tableWidget.item(i, 0).text(),))
                pNumber = cursor.fetchall()
                
                proNumber = pNumber[0][0] - int(self.tableWidget.item(i, 1).text())
                cursor.execute("update products set number = ? where name = ?", (proNumber, self.tableWidget.item(i, 0).text()))
                con.commit()

                values2 = (id2,self.lineEdit.text(),self.tableWidget.item(i, 0).text(),self.tableWidget.item(i, 1).text(),price[0][0] * int(self.tableWidget.item(i, 1).text()),self.label_4.text(),self.label_5.text(),id1)
                cursor.execute("insert into factorProducts values(?,?,?,?,?,?,?,?)", values2)

                listProduct.append((self.tableWidget.item(i,0).text(),self.tableWidget.item(i,1).text(),price[0][0] * int(self.tableWidget.item(i, 1).text())))
            values = (id1,self.lineEdit.text(),self.lineEdit_2.text(),self.label_4.text(),self.label_5.text(),totalPrice)
            cursor.execute("insert into factorList values(?,?,?,?,?,?)", values)
            con.commit()

            status = "ok"
        except ValueError:
            self.label.setText("The value of some fields has problem!!!")
        except:
            self.label.setText("The factor hasn't been submited!!!")

        finally:
            con.close()

        if (status == "ok"):
            try:
                db = sqlite3.connect("file::memory:?cache=shared")
                db.isolation_level = None 
                cursor = db.cursor()
                cursor.execute("create table temp(userType)")
                cursor.execute("insert into temp(userType)  values(\"sellManager\")")
    
                cursor.execute("create table factorProduct(name,number,price)")

                for item in listProduct:
                    cursor.execute("insert into factorProduct(name,number,price) values(?,?,?)", (item[0], item[1], item[2]))
               
                cursor.execute("create table factorList(customerCode,adminCode,date,time,totalPrice)")
                cursor.execute("insert into factorList(customerCode,adminCode,date,time,totalPrice) values(?,?,?,?,?)", (self.lineEdit.text(), self.lineEdit_2.text(), self.label_4.text(), self.label_5.text(), str(totalPrice)))
                self.MainWindow.close()
                self.show_factor()
            except:
                pass
            finally:
                db.close()
    

    def addCustomer(self):
        try:
            db = sqlite3.connect("file::memory:?cache=shared")
            db.isolation_level = None
            cursor = db.cursor()
            cursor.execute("create table temp(customerCode,adminCode)")
            cursor.execute("insert into temp(adminCode) values(?)", (self.lineEdit_2.text(),))
            cursor.execute("create table temp2(productName,productNumber)")
            for i in range(self.tableWidget.rowCount()-1):
                cursor.execute("insert into temp2(productName,productNumber) values(?,?)",(self.tableWidget.item(i, 0).text(),self.tableWidget.item(i, 1).text()))
        except:
            pass
        finally:
            db.close()
        self.MainWindow.close()
        self.show_addCustomer()

    def show_addCustomer(self):
        from link import addCustomer
        self.cus_window = QtWidgets.QMainWindow()
        self.cus_ui = addCustomer()
        self.cus_ui.setupUi(self.cus_window)
        self.cus_window.show()

    def show_factor(self):
        from link import factor
        self.fac_window = QtWidgets.QMainWindow()
        self.fac_ui = factor()
        self.fac_ui.setupUi(self.fac_window)
        self.fac_window.show()

    def DeleteFromList(self):
        try:
            for i in range(self.tableWidget.rowCount() - 1):
                if (self.tableWidget.item(i, 0).text() == self.lineEdit_5.text()):
                    self.tableWidget.removeRow(i)
                    self.listRow = self.listRow - 1
                    self.tableWidget.setRowCount(self.listRow + 1)
        except:
            pass

    def factorList(self):
        try:
            db = sqlite3.connect("file::memory:?cache=shared")
            db.isolation_level = None
            cursor = db.cursor()
            cursor.execute("create table user(userType)")
            cursor.execute("insert into user(userType) values(?)",("sellManager",))
            self.MainWindow.close()
            self.show_factorList()
        except:
            pass
        finally:
            db.close()

    def show_factorList(self):
        from link import factorList
        self.factor_window = QtWidgets.QMainWindow()
        self.factor_ui = factorList()
        self.factor_ui.setupUi(self.factor_window)
        self.factor_window.show()

    def financialPage(self):
        try:
            db = sqlite3.connect("file::memory:?cache=shared")
            db.isolation_level = None
            cursor = db.cursor()
            cursor.execute("create table user(userType)")
            cursor.execute("insert into user(userType) values(?)", ("sellManager",))
            self.MainWindow.close()
            self.show_financialPage()
        except:
            pass
        finally:
            db.close()

    def show_financialPage(self):
        from link import financialPage
        self.factor_window = QtWidgets.QMainWindow()
        self.factor_ui = financialPage()
        self.factor_ui.setupUi(self.factor_window)
        self.factor_window.show()
    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
