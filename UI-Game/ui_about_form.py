# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'about_formxKBPnM.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_About_window(object):
    def setupUi(self, About_window):
        if not About_window.objectName():
            About_window.setObjectName(u"About_window")
        About_window.resize(800, 494)
        About_window.setStyleSheet(u"background-color:rgb(24,24,36);\n"
"color:white;")
        self.centralwidget = QWidget(About_window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.info_frame = QFrame(self.centralwidget)
        self.info_frame.setObjectName(u"info_frame")
        self.info_frame.setFrameShape(QFrame.StyledPanel)
        self.info_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.info_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.back_btn = QPushButton(self.info_frame)
        self.back_btn.setObjectName(u"back_btn")
        self.back_btn.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setFamily(u"MV Boli")
        font.setPointSize(12)
        self.back_btn.setFont(font)
        self.back_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.back_btn.setStyleSheet(u"border: 2px solid rgb(230,5,64);")

        self.verticalLayout_2.addWidget(self.back_btn)

        self.info_b = QLabel(self.info_frame)
        self.info_b.setObjectName(u"info_b")
        font1 = QFont()
        font1.setFamily(u"Papyrus")
        font1.setPointSize(14)
        self.info_b.setFont(font1)
        self.info_b.setStyleSheet(u"border: 2px solid rgb(230,5,64);")
        self.info_b.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.info_b)


        self.verticalLayout.addWidget(self.info_frame)

        About_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(About_window)

        QMetaObject.connectSlotsByName(About_window)
    # setupUi

    def retranslateUi(self, About_window):
        About_window.setWindowTitle(QCoreApplication.translate("About_window", u"MainWindow", None))
        self.back_btn.setText(QCoreApplication.translate("About_window", u"Go Back", None))
        self.info_b.setText(QCoreApplication.translate("About_window", u"You are in the home where you can get energy by spending some money\n"
"also, you can enter home in the evening to have a rest and leaving will be a NEW DAY.\n"
"Your money value 30 and you have 30 energy.\n"
" Money and energy gets changed for taking items or services.\n"
"You can go through other buildings to earn more money and energy.\n"
"You have to earn AT LEAST 300 ENERGY to win the game", None))
    # retranslateUi

