# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Loading.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

couter = 0


class Ui_Loading(object):
    def setupUi(self, Loading):
        Loading.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Loading.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        Loading.setObjectName("Loading")
        Loading.resize(522, 311)
        Loading.setStyleSheet("QFrame {\n"
"background-color: rgb(32, 51, 112);\n"
"    border-radius: 10px;\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(Loading)
        self.verticalLayout.setObjectName("verticalLayout")
        self.DropShadowFrame = QtWidgets.QFrame(Loading)
        self.DropShadowFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.DropShadowFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.DropShadowFrame.setObjectName("DropShadowFrame")
        self.label = QtWidgets.QLabel(self.DropShadowFrame)
        self.label.setGeometry(QtCore.QRect(0, 70, 501, 61))
        font = QtGui.QFont()
        font.setFamily("Nirmala UI")
        font.setPointSize(40)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("color: rgb(245, 215, 9);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.progressBar = QtWidgets.QProgressBar(self.DropShadowFrame)
        self.progressBar.setGeometry(QtCore.QRect(10, 210, 481, 23))
        self.progressBar.setStyleSheet("QProgressBar{\n"
"    \n"
"    background-color: rgb(134, 130, 255);\n"
"    \n"
"    color: rgb(32, 51, 112);\n"
"    border-style: none;\n"
"    border-radius: 10px;\n"
"    text-align: center;\n"
"    font-size: 15px\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"    border-radius: 10px;\n"
"    \n"
"    \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.455, x2:1, y2:0.489, stop:0 rgba(246, 214, 9, 255), stop:1 rgba(255, 247, 10, 255));\n"
"}")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.label_2 = QtWidgets.QLabel(self.DropShadowFrame)
        self.label_2.setGeometry(QtCore.QRect(220, 240, 61, 20))
        self.label_2.setStyleSheet("color: rgb(246, 215, 9);")
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.DropShadowFrame)

        self.retranslateUi(Loading)
        QtCore.QMetaObject.connectSlotsByName(Loading)

    def retranslateUi(self, Loading):
        _translate = QtCore.QCoreApplication.translate
        Loading.setWindowTitle(_translate("Loading", "Dialog"))
        self.label.setText(_translate("Loading", "<html><head/><body><p>HAND TRACKING</p><p><br/></p></body></html>"))
        self.label_2.setText(_translate("Loading", "LOADING..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Loading = QtWidgets.QDialog()
    Loading = QtWidgets.QWidget()
    ui = Ui_Loading()
    ui.setupUi(Loading)
    Loading.show()
    sys.exit(app.exec_())