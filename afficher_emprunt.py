# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI\afficher_emprunt.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1139, 873)
        Form.setStyleSheet("")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_2 = QtWidgets.QWidget(Form)
        self.widget_2.setStyleSheet("background-color: rgb(31, 53, 61);\n"
"color : rgb(255, 255, 255);\n"
"\n"
"")
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame = QtWidgets.QFrame(self.widget_2)
        self.frame.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setContentsMargins(-1, 20, -1, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Forte")
        font.setPointSize(20)
        font.setUnderline(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(16)
        self.frame_2.setFont(font)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setContentsMargins(40, 5, 50, 11)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.reference = QtWidgets.QLineEdit(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(16)
        self.reference.setFont(font)
        self.reference.setStyleSheet("QLineEdit {\n"
"    border :2px solid ;\n"
"    border-radius : 15px;\n"
"    border-color: rgb(197, 181, 61);\n"
"    background-color: rgb(255, 255, 255);\n"
"    color :rgb(0, 0, 0);\n"
"}\n"
"QLineEdit:hover {\n"
"    border : 2px solid rgbrgb(97, 89, 30);\n"
"}\n"
"\n"
"")
        self.reference.setMaxLength(3)
        self.reference.setObjectName("reference")
        self.horizontalLayout.addWidget(self.reference)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 2)
        self.verticalLayout_2.addWidget(self.frame_2)
        self.widget = QtWidgets.QWidget(self.frame)
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(16)
        self.widget.setFont(font)
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(40, 5, 50, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.num_insc = QtWidgets.QLineEdit(self.widget)
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(16)
        self.num_insc.setFont(font)
        self.num_insc.setStyleSheet("QLineEdit {\n"
"    border :2px solid ;\n"
"    border-radius : 15px;\n"
"    border-color: rgb(197, 181, 61);\n"
"    background-color: rgb(255, 255, 255);\n"
"    color :rgb(0, 0, 0);\n"
"}\n"
"QLineEdit:hover {\n"
"    border : 2px solid rgbrgb(97, 89, 30);\n"
"}\n"
"\n"
"")
        self.num_insc.setObjectName("num_insc")
        self.horizontalLayout_2.addWidget(self.num_insc)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 2)
        self.verticalLayout_2.addWidget(self.widget)
        self.verticalLayout_4.addWidget(self.frame)
        self.frame_5 = QtWidgets.QFrame(self.widget_2)
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(16)
        self.frame_5.setFont(font)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_5)
        self.gridLayout.setContentsMargins(40, 30, 50, 20)
        self.gridLayout.setObjectName("gridLayout")
        self.dateEdit = QtWidgets.QDateEdit(self.frame_5)
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(16)
        self.dateEdit.setFont(font)
        self.dateEdit.setStyleSheet("QDateEdit  {\n"
"    border :2px solid ;\n"
"    border-radius : 15px;\n"
"    border-color: rgb(197, 181, 61);\n"
"    background-color: rgb(255, 255, 255);\n"
"    color : rgb(0, 0, 0)\n"
"}\n"
"QDateEdit:hover {\n"
"    border : 2px solid rgbrgb(97, 89, 30);\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.dateEdit.setDate(QtCore.QDate(9999, 12, 31))
        self.dateEdit.setObjectName("dateEdit")
        self.gridLayout.addWidget(self.dateEdit, 0, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(16)
        self.label_8.setFont(font)
        self.label_8.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 1, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(16)
        self.label_7.setFont(font)
        self.label_7.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.frame_5)
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet("QPushButton{\n"
"    height : 35px;\n"
"    background-color :rgb(0, 71, 104);\n"
"    border-radius : 15px;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(0, 92, 157);\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 2, 1, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_5)
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"    height : 35px;\n"
"    background-color :rgb(0, 71, 104);\n"
"    border-radius : 15px;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(0, 92, 157);\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 3, 1, 1, 1)
        self.dateEdit_2 = QtWidgets.QDateEdit(self.frame_5)
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(16)
        self.dateEdit_2.setFont(font)
        self.dateEdit_2.setStyleSheet("QDateEdit  {\n"
"    border :2px solid ;\n"
"    border-radius : 15px;\n"
"    border-color: rgb(197, 181, 61);\n"
"    background-color: rgb(255, 255, 255);\n"
"    color : rgb(0, 0, 0)\n"
"}\n"
"QDateEdit:hover {\n"
"    border : 2px solid rgbrgb(97, 89, 30);\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.dateEdit_2.setDate(QtCore.QDate(9999, 12, 31))
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.gridLayout.addWidget(self.dateEdit_2, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setFamily("Sitka Small")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(170, 170, 170);")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout_4.addWidget(self.frame_5)
        self.tableView = QtWidgets.QTableView(self.widget_2)
        self.tableView.setStyleSheet("\n"
"QHeaderView::section {\n"
"    background-color: rgb(96, 164, 189);\n"
"    color: rgb(0, 0, 0);\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"tableView::item {\n"
"    text-align: center;\n"
"}")
        self.tableView.setObjectName("tableView")
        self.verticalLayout_4.addWidget(self.tableView)
        self.verticalLayout_4.setStretch(0, 1)
        self.verticalLayout_4.setStretch(1, 1)
        self.verticalLayout_4.setStretch(2, 2)
        self.verticalLayout.addWidget(self.widget_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", " Afficher Un Emprunt"))
        self.label_2.setText(_translate("Form", "Référence"))
        self.label_3.setText(_translate("Form", "Num D\'inscription"))
        self.num_insc.setInputMask(_translate("Form", "999999"))
        self.label_8.setText(_translate("Form", "Date De Retour"))
        self.label_7.setText(_translate("Form", "Date D\'emprunt"))
        self.pushButton.setText(_translate("Form", "Afficher"))
        self.pushButton_2.setText(_translate("Form", "Afficher Tous"))
        self.label_4.setText(_translate("Form", "Date Par Défaut 12/31/9999"))
#import etudiant