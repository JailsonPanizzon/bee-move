# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bee.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1073, 584)
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(9, 9, 791, 561))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(809, 9, 241, 121))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 20, 211, 16))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(10, 40, 221, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(80, 80, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(809, 129, 241, 191))
        self.groupBox_2.setObjectName("groupBox_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 50, 181, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_3.setGeometry(QtCore.QRect(9, 109, 231, 81))
        self.groupBox_3.setTitle("")
        self.groupBox_3.setObjectName("groupBox_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 10, 181, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_4.setGeometry(QtCore.QRect(20, 50, 181, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(30, 20, 151, 16))
        self.label_6.setObjectName("label_6")
        self.altura = QtWidgets.QLineEdit(self.groupBox_2)
        self.altura.setGeometry(QtCore.QRect(150, 20, 71, 20))
        self.altura.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.altura.setObjectName("altura")
        self.progressBar = QtWidgets.QProgressBar(Form)
        self.progressBar.setGeometry(QtCore.QRect(830, 340, 221, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(840, 410, 161, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(990, 410, 47, 20))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(840, 440, 111, 16))
        self.label_5.setObjectName("label_5")
        self.vlc = QtWidgets.QLabel(Form)
        self.vlc.setGeometry(QtCore.QRect(990, 440, 47, 13))
        self.vlc.setObjectName("vlc")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(840, 470, 121, 16))
        self.label_7.setObjectName("label_7")
        self.tmpcam = QtWidgets.QLabel(Form)
        self.tmpcam.setGeometry(QtCore.QRect(990, 470, 47, 13))
        self.tmpcam.setObjectName("tmpcam")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(840, 500, 111, 16))
        self.label_9.setObjectName("label_9")
        self.tempdesc = QtWidgets.QLabel(Form)
        self.tempdesc.setGeometry(QtCore.QRect(990, 500, 47, 13))
        self.tempdesc.setObjectName("tempdesc")
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(840, 530, 111, 16))
        self.label_11.setObjectName("label_11")
        self.tempestaci = QtWidgets.QLabel(Form)
        self.tempestaci.setGeometry(QtCore.QRect(990, 530, 47, 13))
        self.tempestaci.setObjectName("tempestaci")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "Carregar Video"))
        self.label.setText(_translate("Form", "Nome ou diretório do video"))
        self.pushButton.setText(_translate("Form", "Carregar"))
        self.groupBox_2.setTitle(_translate("Form", "Selecionar abelha"))
        self.pushButton_2.setText(_translate("Form", "Selecionar abelha"))
        self.pushButton_3.setText(_translate("Form", "Iniciar"))
        self.pushButton_4.setText(_translate("Form", "Selecionar novamente"))
        self.label_6.setText(_translate("Form", "Altura da area do video"))
        self.label_3.setText(_translate("Form", "Distancia percorrida"))
        self.label_4.setText(_translate("Form", "0.0"))
        self.label_5.setText(_translate("Form", "Velociadade Média"))
        self.vlc.setText(_translate("Form", "0.0"))
        self.label_7.setText(_translate("Form", "Tempo de caminhamento"))
        self.tmpcam.setText(_translate("Form", "0.0"))
        self.label_9.setText(_translate("Form", "Tempo de descanço"))
        self.tempdesc.setText(_translate("Form", "0.0"))
        self.label_11.setText(_translate("Form", "Tempo estacionario"))
        self.tempestaci.setText(_translate("Form", "0.0"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_MainWindow()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
