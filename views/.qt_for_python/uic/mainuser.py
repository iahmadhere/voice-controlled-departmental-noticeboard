# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Precision\Desktop\abc\mainuser.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(839, 645)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(580, 40, 211, 31))
        self.lineEdit.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color:#365372;\n"
"border:none;\n"
"border-radius:0px;")
        self.lineEdit.setObjectName("lineEdit")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(-20, -10, 851, 631))
        self.widget.setStyleSheet("background-color:#be808e;")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(79, 223, 91, 91))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(63)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(0, 0))
        self.label.setStyleSheet("background-color:none;")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("c:\\Users\\Precision\\Desktop\\abc\\src/user (3).png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(50, 219, 161, 241))
        self.label_2.setStyleSheet("background-color:#c5bacc;\n"
" border-radius: 10px ;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(670, 30, 31, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(63)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QtCore.QSize(0, 0))
        self.label_3.setStyleSheet("background-color:#01264E;")
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("c:\\Users\\Precision\\Desktop\\abc\\src/user (3).png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(680, 70, 31, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(63)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QtCore.QSize(0, 0))
        self.label_4.setStyleSheet("background-color:#01264E;")
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("c:\\Users\\Precision\\Desktop\\abc\\src/padlock.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(80, 420, 111, 21))
        self.pushButton.setMouseTracking(False)
        self.pushButton.setStyleSheet("background-color:#01264e;\n"
"border-radius:10px;\n"
"color:white;\n"
"font: 75 10pt \"Tahoma\";\n"
"letter-spacing: 2 px;")
        self.pushButton.setCheckable(False)
        self.pushButton.setObjectName("pushButton")
        self.radioButton = QtWidgets.QRadioButton(self.widget)
        self.radioButton.setGeometry(QtCore.QRect(240, 30, 101, 21))
        self.radioButton.setStyleSheet("background-color:#c5bacc;\n"
"border-radius:20px;\n"
"letter-spacing:1px;")
        self.radioButton.setObjectName("radioButton")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(630, 100, 211, 31))
        self.lineEdit_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color:#365372;\n"
"border:none;\n"
"border-radius:0px;")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_3.setGeometry(QtCore.QRect(680, 140, 113, 20))
        font = QtGui.QFont()
        font.setItalic(False)
        font.setKerning(True)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("background-color:#c5bacc;\n"
"border:none;")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(240, 217, 161, 241))
        self.label_5.setStyleSheet("background-color:#c5bacc;\n"
" border-radius: 10px ;")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(420, 218, 161, 241))
        self.label_6.setStyleSheet("background-color:#c5bacc;\n"
" border-radius: 10px ;")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setGeometry(QtCore.QRect(600, 216, 161, 241))
        self.label_7.setStyleSheet("background-color:#c5bacc;\n"
" border-radius: 10px ;")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setGeometry(QtCore.QRect(290, 220, 61, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(63)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setMinimumSize(QtCore.QSize(0, 0))
        self.label_8.setStyleSheet("background-color:none;")
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("c:\\Users\\Precision\\Desktop\\abc\\src/user (3).png"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.widget)
        self.label_9.setGeometry(QtCore.QRect(470, 220, 61, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(63)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setMinimumSize(QtCore.QSize(0, 0))
        self.label_9.setStyleSheet("background-color:none;")
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("c:\\Users\\Precision\\Desktop\\abc\\src/user (3).png"))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.widget)
        self.label_10.setGeometry(QtCore.QRect(650, 218, 61, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(63)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setMinimumSize(QtCore.QSize(0, 0))
        self.label_10.setStyleSheet("background-color:none;")
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap("c:\\Users\\Precision\\Desktop\\abc\\src/user (3).png"))
        self.label_10.setScaledContents(True)
        self.label_10.setObjectName("label_10")
        self.label_2.raise_()
        self.label.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.pushButton.raise_()
        self.radioButton.raise_()
        self.lineEdit_2.raise_()
        self.lineEdit_3.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.widget.raise_()
        self.lineEdit.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 839, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", " User Email"))
        self.pushButton.setText(_translate("MainWindow", "NOTIFICATION"))
        self.radioButton.setText(_translate("MainWindow", "Remember Me"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", " Password"))
        self.lineEdit_3.setText(_translate("MainWindow", "Forget password"))
