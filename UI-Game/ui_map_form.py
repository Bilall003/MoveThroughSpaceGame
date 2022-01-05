# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'map_formzlJJGJ.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_map_window(object):
    def setupUi(self, map_window):
        if not map_window.objectName():
            map_window.setObjectName(u"map_window")
        map_window.resize(800, 915)
        map_window.setStyleSheet(u"background-color:rgb(24,24,36);\n"
"color:white;")
        self.centralwidget = QWidget(map_window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.map_frame = QFrame(self.centralwidget)
        self.map_frame.setObjectName(u"map_frame")
        self.map_frame.setFrameShape(QFrame.StyledPanel)
        self.map_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.map_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.back_btn = QPushButton(self.map_frame)
        self.back_btn.setObjectName(u"back_btn")
        self.back_btn.setMaximumSize(QSize(16777215, 40))
        font = QFont()
        font.setFamily(u"MV Boli")
        font.setPointSize(12)
        self.back_btn.setFont(font)
        self.back_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.back_btn.setStyleSheet(u"border: 2px solid rgb(230,5,64);")

        self.verticalLayout_2.addWidget(self.back_btn)

        self.map_lbl = QLabel(self.map_frame)
        self.map_lbl.setObjectName(u"map_lbl")
        font1 = QFont()
        font1.setFamily(u"Papyrus")
        font1.setPointSize(14)
        self.map_lbl.setFont(font1)
        self.map_lbl.setStyleSheet(u"border: 2px solid rgb(230,5,64);")
        self.map_lbl.setPixmap(QPixmap(u"../map.PNG"))
        self.map_lbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.map_lbl)


        self.verticalLayout.addWidget(self.map_frame)

        map_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(map_window)

        QMetaObject.connectSlotsByName(map_window)
    # setupUi

    def retranslateUi(self, map_window):
        map_window.setWindowTitle(QCoreApplication.translate("map_window", u"MainWindow", None))
        self.back_btn.setText(QCoreApplication.translate("map_window", u"Go back", None))
        self.map_lbl.setText("")
    # retranslateUi

