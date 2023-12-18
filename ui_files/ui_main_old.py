# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainQFawJj.ui'
##
## Created by: Qt User Interface Compiler version 6.1.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
from QSwitchControl import SwitchControl


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 745)
        icon = QIcon()
        icon.addFile(u"icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QWidget{\n"
"	color: white;\n"
"	font: 500 10pt \"Google Sans Medium\";\n"
"}\n"
"\n"
"#drop_shadow_frame{\n"
"	background-color: #262424;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"#content_bar{\n"
"	background-color: #3b3838;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"#content_bar .QFrame{\n"
"	background-color: #262424;\n"
"	border: 1px solid transparent;\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"#frame_title QPushButton{\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"#frame_title QPushButton:hover{ \n"
"}\n"
"\n"
"#frame_btns QPushButton{\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"#frame_btns QPushButton:hover{\n"
"	border: 2px solid #5e5a5a;\n"
"	background-color: #5e5a5a;\n"
"}\n"
"\n"
"#frame_fly .QFrame{\n"
"	background-color: #3b3838;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"#frame_btns #btn_close:hover{\n"
"	border: 2px solid #FF3333;\n"
"	background-color: #FF3333;\n"
"}\n"
"\n"
"QLineEdit{\n"
"	border-radius: 15px;\n"
"	border: 1px solid transparent;\n"
"	background-color: #262424;\n"
"}\n"
"\n"
"QLin"
                        "eEdit:hover{\n"
"	border: 2px solid #35404c;\n"
"	background-color: #35404c;\n"
"}\n"
"\n"
"QScrollBar{\n"
"	background-color: #262424;\n"
"	height: 8px;\n"
"	width:  8px;\n"
"}\n"
"\n"
"QScrollBar::handle{\n"
"	background: #aaaaaa;\n"
"	border: 1px solid #aaaaaa;\n"
"	border-radius: 4px;\n"
"	min-width: 6px;\n"
"	min-height: 6px;\n"
"}\n"
"\n"
"QScrollBar::add-line, QScrollBar::sub-line {\n"
"	background-color: none;\n"
"	border: 1px solid transparent;\n"
"}\n"
"\n"
"QScrollBar::add-page, QScrollBar::sub-page {\n"
"	background-color: none;\n"
"}\n"
"\n"
"#lbl_fly, #lbl_visual {\n"
"	font: 12pt \"Google Sans\";\n"
"}\n"
"\n"
"#label_global_err {\n"
"	font: 500 8pt \"Google Sans Medium\";\n"
"	color: #FF3333;\n"
"}\n"
"\n"
"#label_title {\n"
"	font: 500 12pt \"Google Sans Medium\";\n"
"}\n"
"\n"
"#btn_start {\n"
"	border-radius: 15px;\n"
"	border: 1px solid transparent;\n"
"	background-color: qlineargradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #0883d9, stop: 1 #0370c8);\n"
"}\n"
"\n"
"#btn_start:hover { \n"
"	"
                        "border: 2px solid #0988e3;\n"
"	background-color: #0988e3;\n"
"}\n"
"\n"
"#btn_start:pressed {\n"
"	border: 2px solid #4fc7ff;\n"
"	background-color: #4fc7ff;\n"
"}\n"
"")
        MainWindow.setIconSize(QSize(256, 256))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.drop_shadow_layout = QGridLayout(self.centralwidget)
        self.drop_shadow_layout.setObjectName(u"drop_shadow_layout")
        self.drop_shadow_layout.setContentsMargins(10, 10, 10, 10)
        self.drop_shadow_frame = QFrame(self.centralwidget)
        self.drop_shadow_frame.setObjectName(u"drop_shadow_frame")
        self.drop_shadow_frame.setStyleSheet(u"")
        self.drop_shadow_frame.setFrameShape(QFrame.NoFrame)
        self.drop_shadow_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.drop_shadow_frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.title_bar = QFrame(self.drop_shadow_frame)
        self.title_bar.setObjectName(u"title_bar")
        self.title_bar.setMinimumSize(QSize(0, 40))
        self.title_bar.setMaximumSize(QSize(16777215, 40))
        self.title_bar.setStyleSheet(u"")
        self.title_bar.setFrameShape(QFrame.NoFrame)
        self.title_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.title_bar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_title = QFrame(self.title_bar)
        self.frame_title.setObjectName(u"frame_title")
        self.frame_title.setEnabled(True)
        font = QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.frame_title.setFont(font)
        self.frame_title.setCursor(QCursor(Qt.ArrowCursor))
        self.frame_title.setLayoutDirection(Qt.LeftToRight)
        self.frame_title.setAutoFillBackground(False)
        self.frame_title.setStyleSheet(u"")
        self.frame_title.setFrameShape(QFrame.NoFrame)
        self.frame_title.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_title)
        self.horizontalLayout_3.setSpacing(1)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(2, 2, 0, 0)
        self.logo = QPushButton(self.frame_title)
        self.logo.setObjectName(u"logo")
        icon1 = QIcon()
        icon1.addFile(u"bin/assets/ico.png", QSize(), QIcon.Normal, QIcon.Off)
        self.logo.setIcon(icon1)
        self.logo.setIconSize(QSize(25, 25))

        self.horizontalLayout_3.addWidget(self.logo)

        self.label_title = QLabel(self.frame_title)
        self.label_title.setObjectName(u"label_title")

        self.horizontalLayout_3.addWidget(self.label_title)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)


        self.horizontalLayout.addWidget(self.frame_title)

        self.frame_btns = QFrame(self.title_bar)
        self.frame_btns.setObjectName(u"frame_btns")
        self.frame_btns.setMaximumSize(QSize(200, 16777215))
        self.frame_btns.setCursor(QCursor(Qt.ArrowCursor))
        self.frame_btns.setStyleSheet(u"")
        self.frame_btns.setFrameShape(QFrame.StyledPanel)
        self.frame_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_btns)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 5, 0)
        self.btn_minimize = QPushButton(self.frame_btns)
        self.btn_minimize.setObjectName(u"btn_minimize")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_minimize.sizePolicy().hasHeightForWidth())
        self.btn_minimize.setSizePolicy(sizePolicy)
        self.btn_minimize.setMinimumSize(QSize(40, 15))
        self.btn_minimize.setMaximumSize(QSize(30, 30))
        icon2 = QIcon()
        icon2.addFile(u"bin/assets/minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_minimize.setIcon(icon2)
        self.btn_minimize.setIconSize(QSize(18, 18))

        self.horizontalLayout_2.addWidget(self.btn_minimize)

        self.btn_maximaze = QPushButton(self.frame_btns)
        self.btn_maximaze.setObjectName(u"btn_maximaze")
        sizePolicy.setHeightForWidth(self.btn_maximaze.sizePolicy().hasHeightForWidth())
        self.btn_maximaze.setSizePolicy(sizePolicy)
        self.btn_maximaze.setMinimumSize(QSize(40, 15))
        self.btn_maximaze.setMaximumSize(QSize(40, 30))
        icon3 = QIcon()
        icon3.addFile(u"bin/assets/maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_maximaze.setIcon(icon3)
        self.btn_maximaze.setIconSize(QSize(18, 18))

        self.horizontalLayout_2.addWidget(self.btn_maximaze)

        self.btn_close = QPushButton(self.frame_btns)
        self.btn_close.setObjectName(u"btn_close")
        sizePolicy.setHeightForWidth(self.btn_close.sizePolicy().hasHeightForWidth())
        self.btn_close.setSizePolicy(sizePolicy)
        self.btn_close.setMinimumSize(QSize(40, 15))
        self.btn_close.setMaximumSize(QSize(30, 30))
        self.btn_close.setStyleSheet(u"")
        icon4 = QIcon()
        icon4.addFile(u"bin/assets/close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_close.setIcon(icon4)
        self.btn_close.setIconSize(QSize(18, 18))

        self.horizontalLayout_2.addWidget(self.btn_close)


        self.horizontalLayout.addWidget(self.frame_btns)

        self.horizontalLayout.setStretch(0, 10)
        self.horizontalLayout.setStretch(1, 1)

        self.verticalLayout.addWidget(self.title_bar)

        self.content_bar = QFrame(self.drop_shadow_frame)
        self.content_bar.setObjectName(u"content_bar")
        self.content_bar.setStyleSheet(u"")
        self.content_bar.setFrameShape(QFrame.NoFrame)
        self.content_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.content_bar)
        self.horizontalLayout_7.setSpacing(11)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(11)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.frame_fly = QFrame(self.content_bar)
        self.frame_fly.setObjectName(u"frame_fly")
        self.frame_fly.setMaximumSize(QSize(600, 16777215))
        self.frame_fly.setFrameShape(QFrame.StyledPanel)
        self.frame_fly.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_fly)
        self.gridLayout.setSpacing(11)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(11, 11, 11, 11)
        self.frame_helix = QFrame(self.frame_fly)
        self.frame_helix.setObjectName(u"frame_helix")
        self.frame_helix.setMinimumSize(QSize(0, 250))
        self.frame_helix.setMaximumSize(QSize(16777215, 250))
        self.frame_helix.setFrameShape(QFrame.StyledPanel)
        self.frame_helix.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_helix)
        self.gridLayout_2.setSpacing(11)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(11, 11, 11, 11)
        self.line_helix_y0 = QLineEdit(self.frame_helix)
        self.line_helix_y0.setObjectName(u"line_helix_y0")
        sizePolicy.setHeightForWidth(self.line_helix_y0.sizePolicy().hasHeightForWidth())
        self.line_helix_y0.setSizePolicy(sizePolicy)
        self.line_helix_y0.setMaximumSize(QSize(16777215, 55))
        self.line_helix_y0.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.line_helix_y0, 1, 1, 1, 1)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(11)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.lbl_helix = QLabel(self.frame_helix)
        self.lbl_helix.setObjectName(u"lbl_helix")

        self.horizontalLayout_9.addWidget(self.lbl_helix)

        self.toggle_helix = SwitchControl(bg_color="#262424", circle_color="#3b3838", active_color="#0370c8")
        self.toggle_helix.setObjectName(u"toggle_helix")

        self.horizontalLayout_9.addWidget(self.toggle_helix)

        self.horizontalLayout_9.setStretch(0, 10)
        self.horizontalLayout_9.setStretch(1, 1)

        self.gridLayout_2.addLayout(self.horizontalLayout_9, 0, 0, 1, 2)

        self.line_helix_x0 = QLineEdit(self.frame_helix)
        self.line_helix_x0.setObjectName(u"line_helix_x0")
        sizePolicy.setHeightForWidth(self.line_helix_x0.sizePolicy().hasHeightForWidth())
        self.line_helix_x0.setSizePolicy(sizePolicy)
        self.line_helix_x0.setMaximumSize(QSize(16777215, 55))
        self.line_helix_x0.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.line_helix_x0, 1, 0, 1, 1)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setSpacing(11)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.lbl_reverse_helix = QLabel(self.frame_helix)
        self.lbl_reverse_helix.setObjectName(u"lbl_reverse_helix")

        self.horizontalLayout_11.addWidget(self.lbl_reverse_helix)

        self.toggle_reverse_helix = SwitchControl(bg_color="#262424", circle_color="#3b3838", active_color="#0370c8")
        self.toggle_reverse_helix.setObjectName(u"toggle_reverse_helix")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.toggle_reverse_helix.sizePolicy().hasHeightForWidth())
        self.toggle_reverse_helix.setSizePolicy(sizePolicy1)

        self.horizontalLayout_11.addWidget(self.toggle_reverse_helix)

        self.horizontalLayout_11.setStretch(0, 10)
        self.horizontalLayout_11.setStretch(1, 1)

        self.gridLayout_2.addLayout(self.horizontalLayout_11, 4, 0, 1, 2)

        self.line_helix_radius = QLineEdit(self.frame_helix)
        self.line_helix_radius.setObjectName(u"line_helix_radius")
        sizePolicy.setHeightForWidth(self.line_helix_radius.sizePolicy().hasHeightForWidth())
        self.line_helix_radius.setSizePolicy(sizePolicy)
        self.line_helix_radius.setMaximumSize(QSize(16777215, 55))
        self.line_helix_radius.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.line_helix_radius, 2, 0, 1, 2)

        self.line_helix_step = QLineEdit(self.frame_helix)
        self.line_helix_step.setObjectName(u"line_helix_step")
        sizePolicy.setHeightForWidth(self.line_helix_step.sizePolicy().hasHeightForWidth())
        self.line_helix_step.setSizePolicy(sizePolicy)
        self.line_helix_step.setMaximumSize(QSize(16777215, 55))
        self.line_helix_step.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.line_helix_step, 3, 0, 1, 2)

        self.gridLayout_2.setRowStretch(0, 1)
        self.gridLayout_2.setRowStretch(1, 2)
        self.gridLayout_2.setRowStretch(2, 2)
        self.gridLayout_2.setRowStretch(3, 2)
        self.gridLayout_2.setRowStretch(4, 1)

        self.gridLayout.addWidget(self.frame_helix, 2, 0, 1, 1)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.lbl_fly = QLabel(self.frame_fly)
        self.lbl_fly.setObjectName(u"lbl_fly")

        self.horizontalLayout_10.addWidget(self.lbl_fly)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_2)

        self.lbl_snake = QLabel(self.frame_fly)
        self.lbl_snake.setObjectName(u"lbl_snake")

        self.horizontalLayout_10.addWidget(self.lbl_snake)

        self.toggle_snake = SwitchControl(bg_color="#3b3838", circle_color="#262424", active_color="#0370c8")
        self.toggle_snake.setObjectName(u"toggle_snake")

        self.horizontalLayout_10.addWidget(self.toggle_snake)


        self.gridLayout.addLayout(self.horizontalLayout_10, 0, 0, 1, 2)

        self.frame_circle = QFrame(self.frame_fly)
        self.frame_circle.setObjectName(u"frame_circle")
        self.frame_circle.setMinimumSize(QSize(0, 200))
        self.frame_circle.setMaximumSize(QSize(16777215, 200))
        self.frame_circle.setFrameShape(QFrame.StyledPanel)
        self.frame_circle.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_circle)
        self.verticalLayout_4.setSpacing(11)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(11)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.lbl_circle = QLabel(self.frame_circle)
        self.lbl_circle.setObjectName(u"lbl_circle")

        self.horizontalLayout_8.addWidget(self.lbl_circle)

        self.toggle_circle = SwitchControl(bg_color="#262424", circle_color="#3b3838", active_color="#0370c8")
        self.toggle_circle.setObjectName(u"toggle_circle")

        self.horizontalLayout_8.addWidget(self.toggle_circle)

        self.horizontalLayout_8.setStretch(0, 10)
        self.horizontalLayout_8.setStretch(1, 1)

        self.verticalLayout_4.addLayout(self.horizontalLayout_8)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setSpacing(11)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.line_circle_x0 = QLineEdit(self.frame_circle)
        self.line_circle_x0.setObjectName(u"line_circle_x0")
        sizePolicy.setHeightForWidth(self.line_circle_x0.sizePolicy().hasHeightForWidth())
        self.line_circle_x0.setSizePolicy(sizePolicy)
        self.line_circle_x0.setMaximumSize(QSize(16777215, 55))
        self.line_circle_x0.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.line_circle_x0, 0, 0, 1, 1)

        self.line_circle_y0 = QLineEdit(self.frame_circle)
        self.line_circle_y0.setObjectName(u"line_circle_y0")
        sizePolicy.setHeightForWidth(self.line_circle_y0.sizePolicy().hasHeightForWidth())
        self.line_circle_y0.setSizePolicy(sizePolicy)
        self.line_circle_y0.setMaximumSize(QSize(16777215, 55))
        self.line_circle_y0.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.line_circle_y0, 0, 1, 1, 1)

        self.line_circle_radius = QLineEdit(self.frame_circle)
        self.line_circle_radius.setObjectName(u"line_circle_radius")
        sizePolicy.setHeightForWidth(self.line_circle_radius.sizePolicy().hasHeightForWidth())
        self.line_circle_radius.setSizePolicy(sizePolicy)
        self.line_circle_radius.setMaximumSize(QSize(16777215, 55))
        self.line_circle_radius.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.line_circle_radius, 1, 0, 1, 2)

        self.line_circle_points = QLineEdit(self.frame_circle)
        self.line_circle_points.setObjectName(u"line_circle_points")
        sizePolicy.setHeightForWidth(self.line_circle_points.sizePolicy().hasHeightForWidth())
        self.line_circle_points.setSizePolicy(sizePolicy)
        self.line_circle_points.setMaximumSize(QSize(16777215, 55))
        self.line_circle_points.setAlignment(Qt.AlignCenter)

        self.gridLayout_5.addWidget(self.line_circle_points, 2, 0, 1, 2)


        self.verticalLayout_4.addLayout(self.gridLayout_5)


        self.gridLayout.addWidget(self.frame_circle, 1, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 3, 0, 1, 2)

        self.frame_rect = QFrame(self.frame_fly)
        self.frame_rect.setObjectName(u"frame_rect")
        self.frame_rect.setMinimumSize(QSize(0, 200))
        self.frame_rect.setMaximumSize(QSize(16777215, 200))
        self.frame_rect.setFrameShape(QFrame.StyledPanel)
        self.frame_rect.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_rect)
        self.verticalLayout_3.setSpacing(11)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(11)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lbl_rect = QLabel(self.frame_rect)
        self.lbl_rect.setObjectName(u"lbl_rect")

        self.horizontalLayout_5.addWidget(self.lbl_rect)

        self.toggle_rect = SwitchControl(bg_color="#262424", circle_color="#3b3838", active_color="#0370c8")
        self.toggle_rect.setObjectName(u"toggle_rect")

        self.horizontalLayout_5.addWidget(self.toggle_rect)

        self.horizontalLayout_5.setStretch(0, 10)
        self.horizontalLayout_5.setStretch(1, 1)

        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setSpacing(11)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.line_rect_b = QLineEdit(self.frame_rect)
        self.line_rect_b.setObjectName(u"line_rect_b")
        sizePolicy.setHeightForWidth(self.line_rect_b.sizePolicy().hasHeightForWidth())
        self.line_rect_b.setSizePolicy(sizePolicy)
        self.line_rect_b.setMaximumSize(QSize(16777215, 55))
        self.line_rect_b.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.line_rect_b, 1, 1, 1, 1)

        self.line_rect_a = QLineEdit(self.frame_rect)
        self.line_rect_a.setObjectName(u"line_rect_a")
        sizePolicy.setHeightForWidth(self.line_rect_a.sizePolicy().hasHeightForWidth())
        self.line_rect_a.setSizePolicy(sizePolicy)
        self.line_rect_a.setMaximumSize(QSize(16777215, 55))
        self.line_rect_a.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.line_rect_a, 0, 1, 1, 1)

        self.line_rect_step = QLineEdit(self.frame_rect)
        self.line_rect_step.setObjectName(u"line_rect_step")
        sizePolicy.setHeightForWidth(self.line_rect_step.sizePolicy().hasHeightForWidth())
        self.line_rect_step.setSizePolicy(sizePolicy)
        self.line_rect_step.setMaximumSize(QSize(16777215, 55))
        self.line_rect_step.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.line_rect_step, 2, 1, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout_3)


        self.gridLayout.addWidget(self.frame_rect, 1, 0, 1, 1)

        self.frame_start = QFrame(self.frame_fly)
        self.frame_start.setObjectName(u"frame_start")
        self.frame_start.setMinimumSize(QSize(0, 69))
        self.frame_start.setMaximumSize(QSize(16777215, 69))
        self.frame_start.setFrameShape(QFrame.StyledPanel)
        self.frame_start.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_start)
        self.horizontalLayout_14.setSpacing(11)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(11, 11, 11, 11)
        self.line_z = QLineEdit(self.frame_start)
        self.line_z.setObjectName(u"line_z")
        sizePolicy.setHeightForWidth(self.line_z.sizePolicy().hasHeightForWidth())
        self.line_z.setSizePolicy(sizePolicy)
        self.line_z.setMinimumSize(QSize(0, 45))
        self.line_z.setMaximumSize(QSize(16777215, 45))
        self.line_z.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.line_z)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_4)

        self.lbl_start = QLabel(self.frame_start)
        self.lbl_start.setObjectName(u"lbl_start")

        self.horizontalLayout_14.addWidget(self.lbl_start)

        self.btn_start = QPushButton(self.frame_start)
        self.btn_start.setObjectName(u"btn_start")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_start.sizePolicy().hasHeightForWidth())
        self.btn_start.setSizePolicy(sizePolicy2)
        self.btn_start.setMinimumSize(QSize(45, 45))
        self.btn_start.setMaximumSize(QSize(45, 45))
        self.btn_start.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_start.setLayoutDirection(Qt.RightToLeft)
        self.btn_start.setStyleSheet(u"")
        icon5 = QIcon()
        icon5.addFile(u"bin/assets/start.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_start.setIcon(icon5)
        self.btn_start.setIconSize(QSize(35, 35))

        self.horizontalLayout_14.addWidget(self.btn_start)


        self.gridLayout.addWidget(self.frame_start, 4, 0, 1, 2)


        self.horizontalLayout_4.addWidget(self.frame_fly)

        self.frame_visual = QFrame(self.content_bar)
        self.frame_visual.setObjectName(u"frame_visual")
        self.frame_visual.setFrameShape(QFrame.StyledPanel)
        self.frame_visual.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_visual)
        self.verticalLayout_2.setSpacing(11)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.lbl_visual = QLabel(self.frame_visual)
        self.lbl_visual.setObjectName(u"lbl_visual")

        self.verticalLayout_2.addWidget(self.lbl_visual)

        self.web = QWebEngineView(self.frame_visual)
        self.web.setObjectName(u"web")

        self.verticalLayout_2.addWidget(self.web)
        self.verticalLayout_2.setStretch(1, 10)

        self.horizontalLayout_4.addWidget(self.frame_visual)

        self.horizontalLayout_4.setStretch(1, 1)

        self.horizontalLayout_7.addLayout(self.horizontalLayout_4)


        self.verticalLayout.addWidget(self.content_bar)

        self.status_bar = QFrame(self.drop_shadow_frame)
        self.status_bar.setObjectName(u"status_bar")
        self.status_bar.setMinimumSize(QSize(0, 30))
        self.status_bar.setMaximumSize(QSize(16777215, 30))
        self.status_bar.setStyleSheet(u"")
        self.status_bar.setFrameShape(QFrame.NoFrame)
        self.status_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.status_bar)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(11, 0, 11, 0)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)

        self.label_global_err = QLabel(self.status_bar)
        self.label_global_err.setObjectName(u"label_global_err")
        self.label_global_err.setMinimumSize(QSize(0, 30))
        self.label_global_err.setMaximumSize(QSize(16777215, 30))
        font1 = QFont()
        font1.setPointSize(8)
        font1.setBold(False)
        font1.setItalic(False)
        self.label_global_err.setFont(font1)
        self.label_global_err.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_global_err)


        self.verticalLayout.addWidget(self.status_bar)


        self.drop_shadow_layout.addWidget(self.drop_shadow_frame, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Uav Tech", None))
        self.logo.setText("")
#if QT_CONFIG(shortcut)
        self.logo.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+R", None))
#endif // QT_CONFIG(shortcut)
        self.label_title.setText(QCoreApplication.translate("MainWindow", u"Gubkin UAV Tech", None))
#if QT_CONFIG(tooltip)
        self.btn_minimize.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_minimize.setText("")
#if QT_CONFIG(tooltip)
        self.btn_maximaze.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_maximaze.setText("")
#if QT_CONFIG(tooltip)
        self.btn_close.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.btn_close.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.btn_close.setText("")
#if QT_CONFIG(shortcut)
        self.btn_close.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.line_helix_y0.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043e\u0440\u0434\u0438\u043d\u0430\u0442\u044b y0", None))
        self.lbl_helix.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0438\u0440\u0430\u043b\u044c", None))
        self.toggle_helix.setText("")
        self.line_helix_x0.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043e\u0440\u0434\u0438\u043d\u0430\u0442\u044b x0", None))
        self.lbl_reverse_helix.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0440\u0430\u0442\u043d\u0430\u044f \u0441\u043f\u0438\u0440\u0430\u043b\u044c", None))
        self.toggle_reverse_helix.setText("")
        self.line_helix_radius.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0434\u0438\u0443\u0441", None))
        self.line_helix_step.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0428\u0430\u0433 \u0441\u043f\u0438\u0440\u0430\u043b\u0438", None))
        self.lbl_fly.setText(QCoreApplication.translate("MainWindow", u"\u0410\u043b\u0433\u043e\u0440\u0438\u0442\u043c\u044b \u043e\u0431\u043b\u0435\u0442\u0430", None))
        self.lbl_snake.setText(QCoreApplication.translate("MainWindow", u"\u0417\u043c\u0435\u0439\u043a\u0430", None))
        self.toggle_snake.setText("")
        self.lbl_circle.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043a\u0440\u0443\u0436\u043d\u043e\u0441\u0442\u044c", None))
        self.toggle_circle.setText("")
        self.line_circle_x0.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043e\u0440\u0434\u0438\u043d\u0430\u0442\u0430 x0", None))
        self.line_circle_y0.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043e\u0440\u0434\u0438\u043d\u0430\u0442\u0430 y0", None))
        self.line_circle_radius.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0434\u0438\u0443\u0441", None))
        self.line_circle_points.setText("")
        self.line_circle_points.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0442\u043e\u0447\u0435\u043a", None))
        self.lbl_rect.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u044f\u043c\u043e\u0443\u0433\u043e\u043b\u044c\u043d\u0438\u043a", None))
        self.toggle_rect.setText("")
        self.line_rect_b.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0428\u0438\u0440\u0438\u043d\u0430", None))
        self.line_rect_a.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0441\u043e\u0442\u0430", None))
        self.line_rect_step.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0428\u0430\u0433 \u0437\u043c\u0435\u0439\u043a\u0438", None))
        self.line_z.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0441\u043e\u0442\u0430 \u043f\u043e\u043b\u0435\u0442\u0430", None))
        self.lbl_start.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0440\u0442 -> ", None))
        self.btn_start.setText("")
        self.lbl_visual.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0438\u0437\u0443\u0430\u043b\u0438\u0437\u0430\u0446\u0438\u044f \u043f\u043e\u043b\u0435\u0442\u0430", None))
        self.label_global_err.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0448\u0438\u0431\u043a\u0438", None))
    # retranslateUi

