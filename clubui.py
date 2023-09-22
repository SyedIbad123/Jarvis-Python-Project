from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SECRET(object):
    def setupUi(self, SECRET):
        SECRET.setObjectName("SECRET")
        SECRET.resize(1368, 702)
        self.centralwidget = QtWidgets.QWidget(SECRET)
        self.centralwidget.setObjectName("centralwidget")
        self.gif_1 = QtWidgets.QLabel(self.centralwidget)
        self.gif_1.setGeometry(QtCore.QRect(0, 0, 1441, 761))
        self.gif_1.setText("")
        self.gif_1.setPixmap(QtGui.QPixmap("Iron_Template_1.gif"))
        self.gif_1.setScaledContents(True)
        self.gif_1.setObjectName("gif_1")
        self.gif_2 = QtWidgets.QLabel(self.centralwidget)
        self.gif_2.setGeometry(QtCore.QRect(0, 0, 471, 311))
        self.gif_2.setText("")
        self.gif_2.setPixmap(QtGui.QPixmap("Earth.gif"))
        self.gif_2.setScaledContents(True)
        self.gif_2.setObjectName("gif_2")
        self.gif_3 = QtWidgets.QLabel(self.centralwidget)
        self.gif_3.setGeometry(QtCore.QRect(1060, 20, 291, 251))
        self.gif_3.setText("")
        self.gif_3.setPixmap(QtGui.QPixmap("Code_Template.gif"))
        self.gif_3.setScaledContents(True)
        self.gif_3.setObjectName("gif_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(120, 560, 131, 51))
        self.pushButton.setStyleSheet("color: rgb(255, 255, 0);\n"
"background-color: rgb(0, 85, 0);\n"
"font: 36pt \"Algerian\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(1180, 570, 131, 51))
        self.pushButton_2.setStyleSheet("color: rgb(255, 255, 0);\n"
"background-color: rgb(170, 0, 0);\n"
"font: 36pt \"Algerian\";")
        self.pushButton_2.setObjectName("pushButton_2")
        SECRET.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(SECRET)
        self.statusbar.setObjectName("statusbar")
        SECRET.setStatusBar(self.statusbar)

        self.retranslateUi(SECRET)
        QtCore.QMetaObject.connectSlotsByName(SECRET)

    def retranslateUi(self, SECRET):
        _translate = QtCore.QCoreApplication.translate
        SECRET.setWindowTitle(_translate("SECRET", "MainWindow"))
        self.pushButton.setText(_translate("SECRET", "RUN"))
        self.pushButton_2.setText(_translate("SECRET", "EXIT"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SECRET = QtWidgets.QMainWindow()
    ui = Ui_SECRET()
    ui.setupUi(SECRET)
    SECRET.show()
    sys.exit(app.exec_())


