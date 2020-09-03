

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QMessageBox
from main_gui import Ui_MainWindow


class Ui_Dialog(object):
    def login(self):
        correct_user_name="HOTEL"	#User name
        correct_password="1234"		#Password
		
        user_name=self.txt_user_name.text()
        password=self.txt_password.text() 
        if(user_name==correct_user_name and password==correct_password):
            
            Dialog.hide()
            
            self.window=QtWidgets.QMainWindow()
            self.ui1 = Ui_MainWindow()
            self.ui1.setupUi(self.window)
            self.window.show()
            
        elif(user_name==correct_user_name):
            self.txt_password.setText("")
            msg=QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Wrong Password")
            msg.setIcon(QMessageBox.Critical)
            msg.exec_()
        elif(password==correct_password):
            self.txt_user_name.setText("")
            msg=QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Wrong Username")
            msg.setIcon(QMessageBox.Critical)
            msg.exec_()
        else :
            self.txt_user_name.setText("")
            self.txt_password.setText("")
            msg=QMessageBox()
            msg.setWindowTitle("Error")
            msg.setText("Wrong Username\nWrong Password")
            msg.setIcon(QMessageBox.Critical)
            msg.exec_()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(580, 501)
        self.txt_user_name = QtWidgets.QLineEdit(Dialog)
        self.txt_user_name.setGeometry(QtCore.QRect(220, 120, 300, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.txt_user_name.setFont(font)
        self.txt_user_name.setText("")
        self.txt_user_name.setObjectName("txt_user_name")

        self.lbl_username = QtWidgets.QLabel(Dialog)
        self.lbl_username.setGeometry(QtCore.QRect(46, 120, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lbl_username.setFont(font)
        self.lbl_username.setObjectName("lbl_username")



        self.txt_password = QtWidgets.QLineEdit(Dialog)
        self.txt_password.setGeometry(QtCore.QRect(224, 210, 300, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.txt_password.setFont(font)
        #self.txt_password.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        #self.txt_password.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.txt_password.setToolTip("")
        self.txt_password.setText("")
        self.txt_password.setObjectName("txt_password")
        self.txt_password.setEchoMode(QtWidgets.QLineEdit.Password)




        self.lbl_password = QtWidgets.QLabel(Dialog)
        self.lbl_password.setGeometry(QtCore.QRect(50, 210, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lbl_password.setFont(font)
        self.lbl_password.setObjectName("lbl_password")

        self.btn_login = QtWidgets.QPushButton(Dialog)
        self.btn_login.setGeometry(QtCore.QRect(224, 302, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btn_login.setFont(font)
        self.btn_login.setObjectName("btn_login")
	
        self.btn_login.clicked.connect(self.login)	

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.lbl_username.setText(_translate("Dialog", "User Name"))
        self.lbl_password.setText(_translate("Dialog", "Password"))
        self.btn_login.setText(_translate("Dialog", "Login"))
        

import sys
app = QtWidgets.QApplication(sys.argv)
Dialog = QtWidgets.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)
Dialog.show()
sys.exit(app.exec_())
