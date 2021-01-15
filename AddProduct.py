# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AddProduct.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

import sqlite3

from PyQt5 import QtCore, QtGui, QtWidgets

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
        self.label_ = QtWidgets.QLabel(self.widget)
        self.label_.setMinimumSize(QtCore.QSize(0, 150))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_.setFont(font)
        self.label_.setStyleSheet("font: 75 30pt \"Arial\";")
        self.label_.setAlignment(QtCore.Qt.AlignCenter)
        self.label_.setObjectName("label_")
        self.verticalLayout_3.addWidget(self.label_)
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 40))
        self.label_6.setStyleSheet("font: 12pt \"Arial\";\n"
"color: rgb(255, 0, 0);")
        self.label_6.setText("")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_3.addWidget(self.label_6)
        self.label_1 = QtWidgets.QLabel(self.widget)
        self.label_1.setMinimumSize(QtCore.QSize(0, 60))
        self.label_1.setStyleSheet("font: 14pt \"Arial\";\n"
"margin: 0 20px;")
        self.label_1.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_1.setObjectName("label_1")
        self.verticalLayout_3.addWidget(self.label_1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("margin: 0 25px;\n"
"padding-left: 10px;\n"
"background-color: rgb(250, 250, 250);\n"
"border: 1px solid rgb(150, 150, 150);\n"
"border-radius: 5px;")
        self.lineEdit_2.setMaxLength(100)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_3.addWidget(self.lineEdit_2)
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setMinimumSize(QtCore.QSize(0, 60))
        self.label_5.setStyleSheet("font: 14pt \"Arial\";\n"
"margin: 0 20px;")
        self.label_5.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
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
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_3.addWidget(self.lineEdit)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setMinimumSize(QtCore.QSize(0, 60))
        self.label.setStyleSheet("font: 14pt \"Arial\";\n"
"margin: 0 20px;")
        self.label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_3.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("margin: 0 25px;\n"
"padding-left: 10px;\n"
"background-color: rgb(250, 250, 250);\n"
"border: 1px solid rgb(150, 150, 150);\n"
"border-radius: 5px;")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout_3.addWidget(self.lineEdit_3)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem4)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.clicked.connect(self.add_product)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("margin: 0px 130px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(68, 134, 247);\n"
"border-radius: 30px;")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_3.addWidget(self.pushButton)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem5)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.gridLayout.addWidget(self.widget, 1, 1, 1, 1)
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
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Add Product"))
        self.label_.setText(_translate("MainWindow", "Add Product"))
        self.label_1.setText(_translate("MainWindow", "Product Name"))
        self.label_5.setText(_translate("MainWindow", "Product Price"))
        self.label.setText(_translate("MainWindow", "Product Number"))
        self.pushButton.setText(_translate("MainWindow", "Add Product"))

    def add_product(self):
        try:
            produtPrice = int(self.lineEdit.text())
            produtName = self.lineEdit_2.text()
            produtNumber = int(self.lineEdit_3.text())
            x = 0
            if (produtName == "" or produtNumber <= 0 or produtPrice <= 0):
                self.label_6.setText("Your command hasn't been done!!!")
                return
                
            con = sqlite3.connect("uniDB")
            cursor = con.cursor()
            cursor.execute("select max(id),max(code) from products")
            value = cursor.fetchall()
            if (value[0][0] == None or value[0][1] == None):
                id = 1
                code = 1001
            else:
                id = value[0][0] + 1
                code = value[0][1] + 1
            cursor.execute(
                "insert into products values(?,?,?,?,?)",
                (id, produtName, code, produtNumber, produtPrice),
            )
            con.commit()
            con.close()
            self.label_6.setStyleSheet("color: green;")
            self.label_6.setText("Your command has been done :))")
        except ValueError:
            self.label_6.setStyleSheet("color: red;")
            self.label_6.setText("Some fields format aren't correct!!!")
        except:
            self.label_6.setStyleSheet("color: red;")
            self.label_6.setText("Your command hasn't been done!!!")   
                
    
    def Home(self):
        self.MainWindow.close()
        self.show_store()
    
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
