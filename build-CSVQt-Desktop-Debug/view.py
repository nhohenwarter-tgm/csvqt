# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/niklas/repositories/csvqt/CSVQt/csvqt.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CSVQt(object):
    def setupUi(self, CSVQt):
        CSVQt.setObjectName("CSVQt")
        CSVQt.resize(568, 293)
        self.centralWidget = QtWidgets.QWidget(CSVQt)
        self.centralWidget.setObjectName("centralWidget")
        self.output = QtWidgets.QTableWidget(self.centralWidget)
        self.output.setGeometry(QtCore.QRect(10, 0, 551, 211))
        self.output.setObjectName("output")
        self.output.setColumnCount(0)
        self.output.setRowCount(0)
        self.filepath = QtWidgets.QLineEdit(self.centralWidget)
        self.filepath.setGeometry(QtCore.QRect(10, 230, 371, 31))
        self.filepath.setText("")
        self.filepath.setObjectName("filepath")
        self.ok = QtWidgets.QPushButton(self.centralWidget)
        self.ok.setGeometry(QtCore.QRect(400, 230, 151, 31))
        self.ok.setObjectName("ok")
        CSVQt.setCentralWidget(self.centralWidget)

        self.retranslateUi(CSVQt)
        self.ok.clicked.connect(CSVQt.read_file)
        QtCore.QMetaObject.connectSlotsByName(CSVQt)

    def retranslateUi(self, CSVQt):
        _translate = QtCore.QCoreApplication.translate
        CSVQt.setWindowTitle(_translate("CSVQt", "CSVQt"))
        self.filepath.setPlaceholderText(_translate("CSVQt", "Filepath..."))
        self.ok.setText(_translate("CSVQt", "OK"))

