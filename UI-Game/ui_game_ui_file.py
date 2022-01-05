# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'game_ui_filebAbQyD.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import icons_rc

class Ui_GameWindow(object):
    def setupUi(self, GameWindow):
        if not GameWindow.objectName():
            GameWindow.setObjectName(u"GameWindow")
        GameWindow.resize(779, 626)
        GameWindow.setStyleSheet(u"*{\n"
"border:none;\n"
"}")
        self.centralwidget = QWidget(GameWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color:rgb(24,24,36);\n"
"color:white;")
        self.horizontalLayout_8 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.sidebar_frame = QFrame(self.centralwidget)
        self.sidebar_frame.setObjectName(u"sidebar_frame")
        self.sidebar_frame.setEnabled(True)
        self.sidebar_frame.setMinimumSize(QSize(270, 0))
        self.sidebar_frame.setMaximumSize(QSize(0, 16777215))
        self.sidebar_frame.setFrameShape(QFrame.StyledPanel)
        self.sidebar_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.sidebar_frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.slide_frame = QFrame(self.sidebar_frame)
        self.slide_frame.setObjectName(u"slide_frame")
        self.slide_frame.setMinimumSize(QSize(196, 0))
        self.slide_frame.setStyleSheet(u"background-color:rgb(9,9,13);")
        self.slide_frame.setFrameShape(QFrame.StyledPanel)
        self.slide_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.slide_frame)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.slide_header = QFrame(self.slide_frame)
        self.slide_header.setObjectName(u"slide_header")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.slide_header.sizePolicy().hasHeightForWidth())
        self.slide_header.setSizePolicy(sizePolicy)
        self.slide_header.setMaximumSize(QSize(270, 50))
        self.slide_header.setFrameShape(QFrame.StyledPanel)
        self.slide_header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.slide_header)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.mainlogo_lbl = QLabel(self.slide_header)
        self.mainlogo_lbl.setObjectName(u"mainlogo_lbl")
        font = QFont()
        font.setFamily(u"Pristina")
        font.setPointSize(24)
        font.setItalic(False)
        self.mainlogo_lbl.setFont(font)

        self.horizontalLayout_5.addWidget(self.mainlogo_lbl)


        self.verticalLayout_5.addWidget(self.slide_header)

        self.slide_body_frame = QFrame(self.slide_frame)
        self.slide_body_frame.setObjectName(u"slide_body_frame")
        self.slide_body_frame.setFrameShape(QFrame.StyledPanel)
        self.slide_body_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.slide_body_frame)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.spaced_lbl = QLabel(self.slide_body_frame)
        self.spaced_lbl.setObjectName(u"spaced_lbl")

        self.verticalLayout_6.addWidget(self.spaced_lbl)

        self.spacer_lbl_9 = QLabel(self.slide_body_frame)
        self.spacer_lbl_9.setObjectName(u"spacer_lbl_9")

        self.verticalLayout_6.addWidget(self.spacer_lbl_9)

        self.playerStatus_lbl = QLabel(self.slide_body_frame)
        self.playerStatus_lbl.setObjectName(u"playerStatus_lbl")
        font1 = QFont()
        font1.setFamily(u"Pristina")
        font1.setPointSize(20)
        self.playerStatus_lbl.setFont(font1)

        self.verticalLayout_6.addWidget(self.playerStatus_lbl)

        self.label_3 = QLabel(self.slide_body_frame)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_6.addWidget(self.label_3)

        self.money_lbl = QLabel(self.slide_body_frame)
        self.money_lbl.setObjectName(u"money_lbl")
        font2 = QFont()
        font2.setFamily(u"MV Boli")
        font2.setPointSize(12)
        self.money_lbl.setFont(font2)

        self.verticalLayout_6.addWidget(self.money_lbl)

        self.label_4 = QLabel(self.slide_body_frame)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_6.addWidget(self.label_4)

        self.energy_lbl = QLabel(self.slide_body_frame)
        self.energy_lbl.setObjectName(u"energy_lbl")
        self.energy_lbl.setFont(font2)

        self.verticalLayout_6.addWidget(self.energy_lbl)

        self.label_7 = QLabel(self.slide_body_frame)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_6.addWidget(self.label_7)

        self.label_5 = QLabel(self.slide_body_frame)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_6.addWidget(self.label_5)

        self.label_8 = QLabel(self.slide_body_frame)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_6.addWidget(self.label_8)

        self.label_6 = QLabel(self.slide_body_frame)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_6.addWidget(self.label_6)


        self.verticalLayout_5.addWidget(self.slide_body_frame, 0, Qt.AlignTop)

        self.availableOptions_lbl = QLabel(self.slide_frame)
        self.availableOptions_lbl.setObjectName(u"availableOptions_lbl")
        self.availableOptions_lbl.setFont(font1)

        self.verticalLayout_5.addWidget(self.availableOptions_lbl)

        self.east_lbl = QLabel(self.slide_frame)
        self.east_lbl.setObjectName(u"east_lbl")
        self.east_lbl.setFont(font2)

        self.verticalLayout_5.addWidget(self.east_lbl)

        self.west_lbl = QLabel(self.slide_frame)
        self.west_lbl.setObjectName(u"west_lbl")
        self.west_lbl.setFont(font2)

        self.verticalLayout_5.addWidget(self.west_lbl)

        self.north_lbl = QLabel(self.slide_frame)
        self.north_lbl.setObjectName(u"north_lbl")
        self.north_lbl.setFont(font2)

        self.verticalLayout_5.addWidget(self.north_lbl)

        self.south_lbl = QLabel(self.slide_frame)
        self.south_lbl.setObjectName(u"south_lbl")
        self.south_lbl.setFont(font2)

        self.verticalLayout_5.addWidget(self.south_lbl)

        self.label_10 = QLabel(self.slide_frame)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_5.addWidget(self.label_10)

        self.label_9 = QLabel(self.slide_frame)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_5.addWidget(self.label_9)

        self.slide_footer = QFrame(self.slide_frame)
        self.slide_footer.setObjectName(u"slide_footer")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(4)
        sizePolicy1.setHeightForWidth(self.slide_footer.sizePolicy().hasHeightForWidth())
        self.slide_footer.setSizePolicy(sizePolicy1)
        self.slide_footer.setMaximumSize(QSize(250, 35))
        self.slide_footer.setFrameShape(QFrame.StyledPanel)
        self.slide_footer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.slide_footer)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.map_btn = QPushButton(self.slide_footer)
        self.map_btn.setObjectName(u"map_btn")
        font3 = QFont()
        font3.setFamily(u"MV Boli")
        font3.setPointSize(11)
        self.map_btn.setFont(font3)
        self.map_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/icons/book-open.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.map_btn.setIcon(icon)

        self.horizontalLayout_4.addWidget(self.map_btn)

        self.about_btn = QPushButton(self.slide_footer)
        self.about_btn.setObjectName(u"about_btn")
        self.about_btn.setFont(font3)
        self.about_btn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/help-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.about_btn.setIcon(icon1)

        self.horizontalLayout_4.addWidget(self.about_btn)


        self.verticalLayout_5.addWidget(self.slide_footer)


        self.verticalLayout_2.addWidget(self.slide_frame)


        self.horizontalLayout_8.addWidget(self.sidebar_frame)

        self.main_frame = QFrame(self.centralwidget)
        self.main_frame.setObjectName(u"main_frame")
        sizePolicy2 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.main_frame.sizePolicy().hasHeightForWidth())
        self.main_frame.setSizePolicy(sizePolicy2)
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.main_frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.main_body_frame = QFrame(self.main_frame)
        self.main_body_frame.setObjectName(u"main_body_frame")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.main_body_frame.sizePolicy().hasHeightForWidth())
        self.main_body_frame.setSizePolicy(sizePolicy3)
        self.main_body_frame.setFrameShape(QFrame.StyledPanel)
        self.main_body_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.main_body_frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.status_frame = QFrame(self.main_body_frame)
        self.status_frame.setObjectName(u"status_frame")
        self.status_frame.setMaximumSize(QSize(16777215, 300))
        self.status_frame.setFrameShape(QFrame.StyledPanel)
        self.status_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.status_frame)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.player_name_lbl = QLabel(self.status_frame)
        self.player_name_lbl.setObjectName(u"player_name_lbl")
        self.player_name_lbl.setFont(font2)

        self.verticalLayout_9.addWidget(self.player_name_lbl)

        self.currentLocation_lbl = QLabel(self.status_frame)
        self.currentLocation_lbl.setObjectName(u"currentLocation_lbl")
        self.currentLocation_lbl.setFont(font2)

        self.verticalLayout_9.addWidget(self.currentLocation_lbl)


        self.verticalLayout_3.addWidget(self.status_frame)

        self.actionbuttons_frame = QFrame(self.main_body_frame)
        self.actionbuttons_frame.setObjectName(u"actionbuttons_frame")
        self.actionbuttons_frame.setMaximumSize(QSize(16777215, 16777215))
        self.actionbuttons_frame.setFrameShape(QFrame.StyledPanel)
        self.actionbuttons_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.actionbuttons_frame)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.action_txt = QLineEdit(self.actionbuttons_frame)
        self.action_txt.setObjectName(u"action_txt")
        self.action_txt.setMinimumSize(QSize(0, 10))
        self.action_txt.setMaximumSize(QSize(16777215, 30))
        self.action_txt.setStyleSheet(u"border: 2px solid rgb(230,5,64);")

        self.verticalLayout_7.addWidget(self.action_txt)

        self.go_btn = QPushButton(self.actionbuttons_frame)
        self.go_btn.setObjectName(u"go_btn")
        self.go_btn.setMaximumSize(QSize(16777215, 30))
        font4 = QFont()
        font4.setFamily(u"MV Boli")
        font4.setPointSize(10)
        self.go_btn.setFont(font4)
        self.go_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.go_btn.setStyleSheet(u"border: 2px solid rgb(230,5,64);")

        self.verticalLayout_7.addWidget(self.go_btn)

        self.action_btn = QPushButton(self.actionbuttons_frame)
        self.action_btn.setObjectName(u"action_btn")
        self.action_btn.setMaximumSize(QSize(16777215, 30))
        self.action_btn.setFont(font4)
        self.action_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.action_btn.setStyleSheet(u"border: 2px solid rgb(230,5,64);")

        self.verticalLayout_7.addWidget(self.action_btn)


        self.verticalLayout_3.addWidget(self.actionbuttons_frame)


        self.verticalLayout.addWidget(self.main_body_frame)

        self.footer_frame = QFrame(self.main_frame)
        self.footer_frame.setObjectName(u"footer_frame")
        self.footer_frame.setFrameShape(QFrame.StyledPanel)
        self.footer_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.footer_frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.bottom_left_frame = QFrame(self.footer_frame)
        self.bottom_left_frame.setObjectName(u"bottom_left_frame")
        self.bottom_left_frame.setFrameShape(QFrame.StyledPanel)
        self.bottom_left_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.bottom_left_frame)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_2.addWidget(self.bottom_left_frame, 0, Qt.AlignBottom)


        self.verticalLayout.addWidget(self.footer_frame)


        self.horizontalLayout_8.addWidget(self.main_frame)

        GameWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(GameWindow)

        QMetaObject.connectSlotsByName(GameWindow)
    # setupUi

    def retranslateUi(self, GameWindow):
        GameWindow.setWindowTitle(QCoreApplication.translate("GameWindow", u"MainWindow", None))
        self.mainlogo_lbl.setText(QCoreApplication.translate("GameWindow", u"Doni: Advanture Game", None))
        self.spaced_lbl.setText("")
        self.spacer_lbl_9.setText("")
        self.playerStatus_lbl.setText(QCoreApplication.translate("GameWindow", u"Player Status", None))
        self.label_3.setText("")
        self.money_lbl.setText(QCoreApplication.translate("GameWindow", u"Money: 30", None))
        self.label_4.setText("")
        self.energy_lbl.setText(QCoreApplication.translate("GameWindow", u"Energy: 30", None))
        self.label_7.setText("")
        self.label_5.setText("")
        self.label_8.setText("")
        self.label_6.setText("")
        self.availableOptions_lbl.setText(QCoreApplication.translate("GameWindow", u"Available Options", None))
        self.east_lbl.setText(QCoreApplication.translate("GameWindow", u"On East: Nothing", None))
        self.west_lbl.setText(QCoreApplication.translate("GameWindow", u"On West: Yard", None))
        self.north_lbl.setText(QCoreApplication.translate("GameWindow", u"On North: Nothing", None))
        self.south_lbl.setText(QCoreApplication.translate("GameWindow", u"On South: Nothing", None))
        self.label_10.setText("")
        self.label_9.setText("")
        self.map_btn.setText(QCoreApplication.translate("GameWindow", u"Map", None))
        self.about_btn.setText(QCoreApplication.translate("GameWindow", u"Help", None))
        self.player_name_lbl.setText(QCoreApplication.translate("GameWindow", u"Player Name:", None))
        self.currentLocation_lbl.setText(QCoreApplication.translate("GameWindow", u"Current Location: Home", None))
        self.action_txt.setPlaceholderText(QCoreApplication.translate("GameWindow", u"Enter where do you want to go", None))
        self.go_btn.setText(QCoreApplication.translate("GameWindow", u"Go", None))
        self.action_btn.setText(QCoreApplication.translate("GameWindow", u"Action", None))
    # retranslateUi

