# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainRgjoCT.ui'
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
from ui_files import resource


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
"QScrollBar{\n"
"	background-color: #3b3838;\n"
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
"QHeaderView::section{\n"
"	background-color: #262424 ;\n"
"	border-left: 1px solid black;\n"
"}\n"
"\n"
"QTableWidget{\n"
"	border: 1px solid #3b3838;\n"
"	background-color: #3b3838;\n"
"}\n"
"\n"
"QTableCornerButton::section{\n"
"	background-color: black;\n"
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
"#content_bar .QF"
                        "rame{\n"
"	background-color: #262424;\n"
"	border: 1px solid transparent;\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
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
"QLineEdit:hover{\n"
"	border: 2px solid #35404c;\n"
"	background-color: #35404c;\n"
"}\n"
"\n"
"QProgressBar {\n"
"	text-align:center;\n"
"	border: 1px solid transparent;\n"
"	border-radius: 5px;\n"
"	background-color: #262424;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"	background-color: qlineargradient( x1: 0, y1: 0, x2: 0, y2: 1,\n"
"	stop: 0 #0883d9, stop: 1 #0370c8);\n"
"	border-radius: 5px;\n"
"}\n"
""
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
"\n"
"#frame_fly #btn_start {\n"
"	border-radius: 15px;\n"
"	border: 1px solid transparent;\n"
"	background-color: qlineargradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #0883d9, stop: 1 #0370c8);\n"
"}\n"
"\n"
"#frame_fly #btn_start:hover { \n"
"	border: 2px solid #0988e3;\n"
"	background-color: #0988e3;\n"
"}\n"
"\n"
"#frame_fly #btn_start:pressed {\n"
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
        self.horizontalLayout_3.setSpacing(9)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(5, 0, 0, 0)
        self.logo = QLabel(self.frame_title)
        self.logo.setObjectName(u"logo")
        self.logo.setMinimumSize(QSize(26, 26))
        self.logo.setMaximumSize(QSize(26, 26))
        self.logo.setPixmap(QPixmap(u":/icons/assets/ico.png"))
        self.logo.setScaledContents(True)

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
        icon1 = QIcon()
        icon1.addFile(u"bin/assets/minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_minimize.setIcon(icon1)
        self.btn_minimize.setIconSize(QSize(18, 18))

        self.horizontalLayout_2.addWidget(self.btn_minimize)

        self.btn_maximaze = QPushButton(self.frame_btns)
        self.btn_maximaze.setObjectName(u"btn_maximaze")
        sizePolicy.setHeightForWidth(self.btn_maximaze.sizePolicy().hasHeightForWidth())
        self.btn_maximaze.setSizePolicy(sizePolicy)
        self.btn_maximaze.setMinimumSize(QSize(40, 15))
        self.btn_maximaze.setMaximumSize(QSize(40, 30))
        icon2 = QIcon()
        icon2.addFile(u"bin/assets/maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_maximaze.setIcon(icon2)
        self.btn_maximaze.setIconSize(QSize(18, 18))

        self.horizontalLayout_2.addWidget(self.btn_maximaze)

        self.btn_close = QPushButton(self.frame_btns)
        self.btn_close.setObjectName(u"btn_close")
        sizePolicy.setHeightForWidth(self.btn_close.sizePolicy().hasHeightForWidth())
        self.btn_close.setSizePolicy(sizePolicy)
        self.btn_close.setMinimumSize(QSize(40, 15))
        self.btn_close.setMaximumSize(QSize(30, 30))
        self.btn_close.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u"bin/assets/close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_close.setIcon(icon3)
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
        self.gridLayout.setSpacing(9)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_start = QFrame(self.frame_fly)
        self.frame_start.setObjectName(u"frame_start")
        self.frame_start.setMinimumSize(QSize(0, 75))
        self.frame_start.setMaximumSize(QSize(16777215, 75))
        self.frame_start.setFrameShape(QFrame.StyledPanel)
        self.frame_start.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_start)
        self.gridLayout_4.setSpacing(9)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.lbl_condition = QLabel(self.frame_start)
        self.lbl_condition.setObjectName(u"lbl_condition")

        self.gridLayout_4.addWidget(self.lbl_condition, 0, 0, 1, 1)

        self.btn_start = QPushButton(self.frame_start)
        self.btn_start.setObjectName(u"btn_start")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_start.sizePolicy().hasHeightForWidth())
        self.btn_start.setSizePolicy(sizePolicy1)
        self.btn_start.setMinimumSize(QSize(55, 55))
        self.btn_start.setMaximumSize(QSize(55, 55))
        self.btn_start.setCursor(QCursor(Qt.ArrowCursor))
        self.btn_start.setLayoutDirection(Qt.RightToLeft)
        self.btn_start.setStyleSheet(u"")
        icon4 = QIcon()
        icon4.addFile(u"bin/assets/start.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_start.setIcon(icon4)
        self.btn_start.setIconSize(QSize(45, 45))

        self.gridLayout_4.addWidget(self.btn_start, 0, 1, 2, 1)

        self.progressBar = QProgressBar(self.frame_start)
        self.progressBar.setObjectName(u"progressBar")
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setMinimumSize(QSize(0, 20))
        self.progressBar.setValue(0)

        self.gridLayout_4.addWidget(self.progressBar, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.frame_start, 4, 0, 1, 2)

        self.verticalSpacer = QSpacerItem(200, 10, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 3, 0, 1, 2)

        self.lbl_fly = QLabel(self.frame_fly)
        self.lbl_fly.setObjectName(u"lbl_fly")

        self.gridLayout.addWidget(self.lbl_fly, 0, 0, 1, 1)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(9)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_rect = QFrame(self.frame_fly)
        self.frame_rect.setObjectName(u"frame_rect")
        self.frame_rect.setMinimumSize(QSize(0, 155))
        self.frame_rect.setMaximumSize(QSize(16777215, 155))
        self.frame_rect.setFrameShape(QFrame.StyledPanel)
        self.frame_rect.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_rect)
        self.verticalLayout_3.setSpacing(9)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(9, 9, 9, 9)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(11)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lbl_rect = QLabel(self.frame_rect)
        self.lbl_rect.setObjectName(u"lbl_rect")

        self.horizontalLayout_5.addWidget(self.lbl_rect)

        self.toggle_rect = SwitchControl(bg_color="#262424", circle_color="#3b3838", active_color="#0370c8")
        self.toggle_rect.setObjectName(u"toggle_rect")
        self.toggle_rect.setAutoExclusive(False)

        self.horizontalLayout_5.addWidget(self.toggle_rect)

        self.horizontalLayout_5.setStretch(0, 10)
        self.horizontalLayout_5.setStretch(1, 1)

        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setSpacing(9)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.ico_height = QLabel(self.frame_rect)
        self.ico_height.setObjectName(u"ico_height")
        self.ico_height.setMaximumSize(QSize(32, 32))
        self.ico_height.setPixmap(QPixmap(u":/icons/assets/height.png"))
        self.ico_height.setScaledContents(True)

        self.gridLayout_3.addWidget(self.ico_height, 0, 0, 1, 1)

        self.ico_width = QLabel(self.frame_rect)
        self.ico_width.setObjectName(u"ico_width")
        self.ico_width.setMaximumSize(QSize(32, 32))
        self.ico_width.setPixmap(QPixmap(u":/icons/assets/width.png"))
        self.ico_width.setScaledContents(True)

        self.gridLayout_3.addWidget(self.ico_width, 1, 0, 1, 1)

        self.line_rect_a = QLineEdit(self.frame_rect)
        self.line_rect_a.setObjectName(u"line_rect_a")
        sizePolicy.setHeightForWidth(self.line_rect_a.sizePolicy().hasHeightForWidth())
        self.line_rect_a.setSizePolicy(sizePolicy)
        self.line_rect_a.setMinimumSize(QSize(0, 45))
        self.line_rect_a.setMaximumSize(QSize(16777215, 45))
        self.line_rect_a.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.line_rect_a, 0, 1, 1, 1)

        self.line_rect_b = QLineEdit(self.frame_rect)
        self.line_rect_b.setObjectName(u"line_rect_b")
        sizePolicy.setHeightForWidth(self.line_rect_b.sizePolicy().hasHeightForWidth())
        self.line_rect_b.setSizePolicy(sizePolicy)
        self.line_rect_b.setMinimumSize(QSize(0, 45))
        self.line_rect_b.setMaximumSize(QSize(16777215, 45))
        self.line_rect_b.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.line_rect_b, 1, 1, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout_3)

        self.verticalLayout_3.setStretch(1, 10)

        self.verticalLayout_4.addWidget(self.frame_rect)

        self.frame_log = QFrame(self.frame_fly)
        self.frame_log.setObjectName(u"frame_log")
        self.frame_log.setMinimumSize(QSize(0, 200))
        self.frame_log.setMaximumSize(QSize(16777215, 600))
        self.frame_log.setFrameShape(QFrame.StyledPanel)
        self.frame_log.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_log)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.lbl_log = QLabel(self.frame_log)
        self.lbl_log.setObjectName(u"lbl_log")

        self.verticalLayout_5.addWidget(self.lbl_log)

        self.table_log = QTableWidget(self.frame_log)
        if (self.table_log.columnCount() < 1):
            self.table_log.setColumnCount(2)
        self.table_log.horizontalHeader().resizeSection(0, 60)
        self.table_log.horizontalHeader().resizeSection(1, 200)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_log.setHorizontalHeaderItem(0, __qtablewidgetitem)
        self.table_log.setObjectName(u"table_log")
        self.table_log.setShowGrid(False)
        self.table_log.horizontalHeader().setVisible(False)
        self.table_log.verticalHeader().setVisible(False)
        self.table_log.verticalHeader().setDefaultSectionSize(25)

        self.verticalLayout_5.addWidget(self.table_log)


        self.verticalLayout_4.addWidget(self.frame_log)


        self.gridLayout.addLayout(self.verticalLayout_4, 2, 1, 1, 1)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_circle = QFrame(self.frame_fly)
        self.frame_circle.setObjectName(u"frame_circle")
        self.frame_circle.setMinimumSize(QSize(0, 227))
        self.frame_circle.setMaximumSize(QSize(16777215, 227))
        self.frame_circle.setFrameShape(QFrame.StyledPanel)
        self.frame_circle.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_circle)
        self.gridLayout_2.setSpacing(9)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.lbl_helix = QLabel(self.frame_circle)
        self.lbl_helix.setObjectName(u"lbl_helix")

        self.horizontalLayout_9.addWidget(self.lbl_helix)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_5)

        self.toggle_helix = SwitchControl(bg_color="#262424", circle_color="#3b3838", active_color="#0370c8")
        self.toggle_helix.setObjectName(u"toggle_helix")
        self.toggle_helix.setAutoExclusive(False)

        self.horizontalLayout_9.addWidget(self.toggle_helix)

        self.horizontalLayout_9.setStretch(0, 1)

        self.gridLayout_2.addLayout(self.horizontalLayout_9, 4, 0, 1, 1)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.ico_radius_2 = QLabel(self.frame_circle)
        self.ico_radius_2.setObjectName(u"ico_radius_2")
        self.ico_radius_2.setMaximumSize(QSize(32, 32))
        self.ico_radius_2.setPixmap(QPixmap(u":/icons/assets/circle.png"))
        self.ico_radius_2.setScaledContents(True)

        self.horizontalLayout_15.addWidget(self.ico_radius_2)

        self.line_radius = QLineEdit(self.frame_circle)
        self.line_radius.setObjectName(u"line_radius")
        sizePolicy.setHeightForWidth(self.line_radius.sizePolicy().hasHeightForWidth())
        self.line_radius.setSizePolicy(sizePolicy)
        self.line_radius.setMinimumSize(QSize(0, 45))
        self.line_radius.setMaximumSize(QSize(16777215, 45))
        self.line_radius.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_15.addWidget(self.line_radius)


        self.gridLayout_2.addLayout(self.horizontalLayout_15, 1, 0, 1, 1)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.ico_num_point = QLabel(self.frame_circle)
        self.ico_num_point.setObjectName(u"ico_num_point")
        self.ico_num_point.setMaximumSize(QSize(32, 32))
        self.ico_num_point.setPixmap(QPixmap(u":/icons/assets/points.png"))
        self.ico_num_point.setScaledContents(True)

        self.horizontalLayout_16.addWidget(self.ico_num_point)

        self.line_points = QLineEdit(self.frame_circle)
        self.line_points.setObjectName(u"line_points")
        sizePolicy.setHeightForWidth(self.line_points.sizePolicy().hasHeightForWidth())
        self.line_points.setSizePolicy(sizePolicy)
        self.line_points.setMinimumSize(QSize(0, 45))
        self.line_points.setMaximumSize(QSize(16777215, 45))
        self.line_points.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_16.addWidget(self.line_points)


        self.gridLayout_2.addLayout(self.horizontalLayout_16, 2, 0, 1, 1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(11)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.lbl_circle = QLabel(self.frame_circle)
        self.lbl_circle.setObjectName(u"lbl_circle")

        self.horizontalLayout_8.addWidget(self.lbl_circle)

        self.toggle_circle = SwitchControl(bg_color="#262424", circle_color="#3b3838", active_color="#0370c8")
        self.toggle_circle.setObjectName(u"toggle_circle")
        self.toggle_circle.setAutoExclusive(False)

        self.horizontalLayout_8.addWidget(self.toggle_circle)

        self.horizontalLayout_8.setStretch(0, 10)
        self.horizontalLayout_8.setStretch(1, 1)

        self.gridLayout_2.addLayout(self.horizontalLayout_8, 0, 0, 1, 1)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.lbl_reverse_helix = QLabel(self.frame_circle)
        self.lbl_reverse_helix.setObjectName(u"lbl_reverse_helix")

        self.horizontalLayout_11.addWidget(self.lbl_reverse_helix)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_4)

        self.toggle_reverse_helix = SwitchControl(bg_color="#262424", circle_color="#3b3838", active_color="#0370c8")
        self.toggle_reverse_helix.setObjectName(u"toggle_reverse_helix")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.toggle_reverse_helix.sizePolicy().hasHeightForWidth())
        self.toggle_reverse_helix.setSizePolicy(sizePolicy2)
        self.toggle_reverse_helix.setAutoExclusive(False)

        self.horizontalLayout_11.addWidget(self.toggle_reverse_helix)

        self.horizontalLayout_11.setStretch(0, 1)

        self.gridLayout_2.addLayout(self.horizontalLayout_11, 5, 0, 1, 1)

        self.gridLayout_2.setRowStretch(0, 1)
        self.gridLayout_2.setRowStretch(1, 2)
        self.gridLayout_2.setRowStretch(2, 2)
        self.gridLayout_2.setRowStretch(3, 1)
        self.gridLayout_2.setRowStretch(4, 1)
        self.gridLayout_2.setRowStretch(5, 1)

        self.verticalLayout_6.addWidget(self.frame_circle)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_2)


        self.gridLayout.addLayout(self.verticalLayout_6, 2, 0, 1, 1)

        self.frame_param = QFrame(self.frame_fly)
        self.frame_param.setObjectName(u"frame_param")
        self.frame_param.setMinimumSize(QSize(0, 0))
        self.frame_param.setMaximumSize(QSize(16777215, 16777215))
        self.frame_param.setFrameShape(QFrame.StyledPanel)
        self.frame_param.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_param)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setSpacing(5)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.ico_y0 = QLabel(self.frame_param)
        self.ico_y0.setObjectName(u"ico_y0")
        self.ico_y0.setMaximumSize(QSize(32, 32))
        self.ico_y0.setPixmap(QPixmap(u":/icons/assets/cord.png"))
        self.ico_y0.setScaledContents(True)

        self.horizontalLayout_13.addWidget(self.ico_y0)

        self.line_y0 = QLineEdit(self.frame_param)
        self.line_y0.setObjectName(u"line_y0")
        sizePolicy.setHeightForWidth(self.line_y0.sizePolicy().hasHeightForWidth())
        self.line_y0.setSizePolicy(sizePolicy)
        self.line_y0.setMaximumSize(QSize(16777215, 45))
        self.line_y0.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.line_y0)


        self.gridLayout_5.addLayout(self.horizontalLayout_13, 1, 1, 1, 1)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setSpacing(5)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.ico_z = QLabel(self.frame_param)
        self.ico_z.setObjectName(u"ico_z")
        self.ico_z.setMaximumSize(QSize(32, 32))
        self.ico_z.setPixmap(QPixmap(u":/icons/assets/quadro.png"))
        self.ico_z.setScaledContents(True)

        self.horizontalLayout_14.addWidget(self.ico_z)

        self.line_z = QLineEdit(self.frame_param)
        self.line_z.setObjectName(u"line_z")
        sizePolicy.setHeightForWidth(self.line_z.sizePolicy().hasHeightForWidth())
        self.line_z.setSizePolicy(sizePolicy)
        self.line_z.setMinimumSize(QSize(0, 45))
        self.line_z.setMaximumSize(QSize(16777215, 45))
        self.line_z.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.line_z)


        self.gridLayout_5.addLayout(self.horizontalLayout_14, 1, 2, 1, 1)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setSpacing(5)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.ico_x0 = QLabel(self.frame_param)
        self.ico_x0.setObjectName(u"ico_x0")
        self.ico_x0.setMaximumSize(QSize(32, 32))
        self.ico_x0.setPixmap(QPixmap(u":/icons/assets/cord.png"))
        self.ico_x0.setScaledContents(True)

        self.horizontalLayout_12.addWidget(self.ico_x0)

        self.line_x0 = QLineEdit(self.frame_param)
        self.line_x0.setObjectName(u"line_x0")
        sizePolicy.setHeightForWidth(self.line_x0.sizePolicy().hasHeightForWidth())
        self.line_x0.setSizePolicy(sizePolicy)
        self.line_x0.setMaximumSize(QSize(16777215, 45))
        self.line_x0.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.line_x0)

        self.horizontalLayout_12.setStretch(1, 10)

        self.gridLayout_5.addLayout(self.horizontalLayout_12, 1, 0, 1, 1)

        self.lbl_params = QLabel(self.frame_param)
        self.lbl_params.setObjectName(u"lbl_params")

        self.gridLayout_5.addWidget(self.lbl_params, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.frame_param, 1, 0, 1, 2)

        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(1, 10)
        self.gridLayout.setRowStretch(2, 100)
        self.gridLayout.setRowStretch(3, 40)
        self.gridLayout.setRowStretch(4, 1)
        self.gridLayout.setColumnStretch(0, 1)

        self.horizontalLayout_4.addWidget(self.frame_fly)

        self.frame_visual = QFrame(self.content_bar)
        self.frame_visual.setObjectName(u"frame_visual")
        self.frame_visual.setFrameShape(QFrame.StyledPanel)
        self.frame_visual.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_visual)
        self.verticalLayout_2.setSpacing(9)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lbl_visual = QLabel(self.frame_visual)
        self.lbl_visual.setObjectName(u"lbl_visual")

        self.verticalLayout_2.addWidget(self.lbl_visual)

        self.web = QWebEngineView(self.frame_visual)
        self.web.setObjectName(u"web")

        self.verticalLayout_2.addWidget(self.web)
        self.verticalLayout_2.setStretch(1, 10)

        self.horizontalLayout_4.addWidget(self.frame_visual)

        self.horizontalLayout_4.setStretch(0, 1)
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
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Registrator", None))
        self.logo.setText("")
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
        self.lbl_condition.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0441\u0442\u043e\u044f\u043d\u0438\u0435", None))
        self.btn_start.setText("")
        self.lbl_fly.setText(QCoreApplication.translate("MainWindow", u"\u0410\u043b\u0433\u043e\u0440\u0438\u0442\u043c\u044b \u043e\u0431\u043b\u0435\u0442\u0430", None))
        self.lbl_rect.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u044f\u043c\u043e\u0443\u0433\u043e\u043b\u044c\u043d\u0438\u043a", None))
        self.toggle_rect.setText("")
        self.ico_height.setText("")
        self.ico_width.setText("")
        self.line_rect_a.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0441\u043e\u0442\u0430", None))
        self.line_rect_b.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0428\u0438\u0440\u0438\u043d\u0430", None))
        self.lbl_log.setText(QCoreApplication.translate("MainWindow", u"\u041b\u043e\u0433", None))
        self.lbl_helix.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0438\u0440\u0430\u043b\u044c", None))
        self.toggle_helix.setText("")
        self.ico_radius_2.setText("")
        self.line_radius.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0434\u0438\u0443\u0441", None))
        self.ico_num_point.setText("")
        self.line_points.setText("")
        self.line_points.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0442\u043e\u0447\u0435\u043a", None))
        self.lbl_circle.setText(QCoreApplication.translate("MainWindow", u"\u041e\u043a\u0440\u0443\u0436\u043d\u043e\u0441\u0442\u044c", None))
        self.toggle_circle.setText("")
        self.lbl_reverse_helix.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0440\u0430\u0442\u043d\u0430\u044f \u0441\u043f\u0438\u0440\u0430\u043b\u044c", None))
        self.toggle_reverse_helix.setText("")
        self.ico_y0.setText("")
        self.line_y0.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043e\u0440\u0434\u0438\u043d\u0430\u0442\u0430 y0", None))
        self.ico_z.setText("")
        self.line_z.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0441\u043e\u0442\u0430 \u043f\u043e\u043b\u0435\u0442\u0430", None))
        self.ico_x0.setText("")
        self.line_x0.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043e\u0440\u0434\u0438\u043d\u0430\u0442\u0430 x0", None))
        self.lbl_params.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0449\u0438\u0435 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b", None))
        self.lbl_visual.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0438\u0437\u0443\u0430\u043b\u0438\u0437\u0430\u0446\u0438\u044f \u043f\u043e\u043b\u0435\u0442\u0430", None))
        self.label_global_err.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0448\u0438\u0431\u043a\u0438", None))
    # retranslateUi

