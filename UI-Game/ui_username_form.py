# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'username_formEPgZic.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_login(object):
    def setupUi(self, login):
        if not login.objectName():
            login.setObjectName(u"login")
        login.resize(800, 494)
        login.setStyleSheet(u"background-color:rgb(24,24,36);\n"
"color:white;")
        self.centralwidget = QWidget(login)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.mainframe = QFrame(self.centralwidget)
        self.mainframe.setObjectName(u"mainframe")
        self.mainframe.setFrameShape(QFrame.StyledPanel)
        self.mainframe.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.mainframe)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.welcome_frame = QFrame(self.mainframe)
        self.welcome_frame.setObjectName(u"welcome_frame")
        self.welcome_frame.setFrameShape(QFrame.StyledPanel)
        self.welcome_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.welcome_frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.welcome_frame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamily(u"Papyrus")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)


        self.verticalLayout_2.addWidget(self.welcome_frame)

        self.entry_frame = QFrame(self.mainframe)
        self.entry_frame.setObjectName(u"entry_frame")
        self.entry_frame.setFrameShape(QFrame.StyledPanel)
        self.entry_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.entry_frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.name_txt = QLineEdit(self.entry_frame)
        self.name_txt.setObjectName(u"name_txt")
        self.name_txt.setMinimumSize(QSize(0, 40))
        self.name_txt.setStyleSheet(u"border: 2px solid rgb(230,5,64);")

        self.verticalLayout_4.addWidget(self.name_txt)

        self.submit_btn = QPushButton(self.entry_frame)
        self.submit_btn.setObjectName(u"submit_btn")
        self.submit_btn.setMinimumSize(QSize(0, 30))
        self.submit_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.submit_btn.setStyleSheet(u"border: 2px solid rgb(230,5,64);")

        self.verticalLayout_4.addWidget(self.submit_btn)


        self.verticalLayout_2.addWidget(self.entry_frame)


        self.verticalLayout.addWidget(self.mainframe)

        login.setCentralWidget(self.centralwidget)

        self.retranslateUi(login)

        QMetaObject.connectSlotsByName(login)
    # setupUi

    def retranslateUi(self, login):
        login.setWindowTitle(QCoreApplication.translate("login", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("login", u"Greetings! Welcome to Doni, an adventure based game\n"
"Please enter your name to continue\n"
"Furthter details will be shown once you enter the game", None))
        self.name_txt.setPlaceholderText(QCoreApplication.translate("login", u"Enter Your name", None))
        self.submit_btn.setText(QCoreApplication.translate("login", u"Submit", None))
    # retranslateUi

