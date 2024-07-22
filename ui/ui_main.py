# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLayout, QMainWindow, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

from qfluentwidgets import (DisplayLabel, PlainTextEdit, PushButton)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1123, 932)
        self.action_about = QAction(MainWindow)
        self.action_about.setObjectName(u"action_about")
        font = QFont()
        font.setPointSize(12)
        self.action_about.setFont(font)
        self.action_open = QAction(MainWindow)
        self.action_open.setObjectName(u"action_open")
        self.action_open.setFont(font)
        self.action_check_update = QAction(MainWindow)
        self.action_check_update.setObjectName(u"action_check_update")
        self.action_check_update.setFont(font)
        self.action_register = QAction(MainWindow)
        self.action_register.setObjectName(u"action_register")
        self.action_register.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.lbl_temp = DisplayLabel(self.centralwidget)
        self.lbl_temp.setObjectName(u"lbl_temp")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_temp.sizePolicy().hasHeightForWidth())
        self.lbl_temp.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font1.setPointSize(20)
        font1.setBold(True)
        self.lbl_temp.setFont(font1)
        self.lbl_temp.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lbl_temp)

        self.pt_list = PlainTextEdit(self.centralwidget)
        self.pt_list.setObjectName(u"pt_list")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pt_list.sizePolicy().hasHeightForWidth())
        self.pt_list.setSizePolicy(sizePolicy1)
        font2 = QFont()
        font2.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font2.setPointSize(16)
        self.pt_list.setFont(font2)
        self.pt_list.setReadOnly(True)

        self.verticalLayout.addWidget(self.pt_list)

        self.pb_reset = PushButton(self.centralwidget)
        self.pb_reset.setObjectName(u"pb_reset")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pb_reset.sizePolicy().hasHeightForWidth())
        self.pb_reset.setSizePolicy(sizePolicy2)
        self.pb_reset.setMinimumSize(QSize(150, 30))
        self.pb_reset.setMaximumSize(QSize(65535, 65535))
        font3 = QFont()
        font3.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font3.setPointSize(20)
        self.pb_reset.setFont(font3)

        self.verticalLayout.addWidget(self.pb_reset)


        self.gridLayout_2.addLayout(self.verticalLayout, 2, 1, 2, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.lbl_9 = DisplayLabel(self.centralwidget)
        self.lbl_9.setObjectName(u"lbl_9")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.lbl_9.sizePolicy().hasHeightForWidth())
        self.lbl_9.setSizePolicy(sizePolicy3)
        font4 = QFont()
        font4.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font4.setPointSize(72)
        font4.setBold(True)
        self.lbl_9.setFont(font4)
        self.lbl_9.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lbl_9, 3, 3, 1, 1)

        self.lbl_13 = DisplayLabel(self.centralwidget)
        self.lbl_13.setObjectName(u"lbl_13")
        sizePolicy2.setHeightForWidth(self.lbl_13.sizePolicy().hasHeightForWidth())
        self.lbl_13.setSizePolicy(sizePolicy2)
        font5 = QFont()
        font5.setFamilies([u"\u6c49\u4eea\u7efc\u827a\u4f53\u7b80"])
        font5.setPointSize(20)
        self.lbl_13.setFont(font5)
        self.lbl_13.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lbl_13, 0, 1, 1, 1)

        self.lbl_10 = DisplayLabel(self.centralwidget)
        self.lbl_10.setObjectName(u"lbl_10")
        sizePolicy3.setHeightForWidth(self.lbl_10.sizePolicy().hasHeightForWidth())
        self.lbl_10.setSizePolicy(sizePolicy3)
        self.lbl_10.setFont(font4)
        self.lbl_10.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lbl_10, 4, 1, 1, 1)

        self.lbl_11 = DisplayLabel(self.centralwidget)
        self.lbl_11.setObjectName(u"lbl_11")
        sizePolicy3.setHeightForWidth(self.lbl_11.sizePolicy().hasHeightForWidth())
        self.lbl_11.setSizePolicy(sizePolicy3)
        self.lbl_11.setFont(font4)
        self.lbl_11.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lbl_11, 4, 2, 1, 1)

        self.lbl_7 = DisplayLabel(self.centralwidget)
        self.lbl_7.setObjectName(u"lbl_7")
        sizePolicy3.setHeightForWidth(self.lbl_7.sizePolicy().hasHeightForWidth())
        self.lbl_7.setSizePolicy(sizePolicy3)
        self.lbl_7.setFont(font4)
        self.lbl_7.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lbl_7, 3, 1, 1, 1)

        self.lbl_1 = DisplayLabel(self.centralwidget)
        self.lbl_1.setObjectName(u"lbl_1")
        sizePolicy3.setHeightForWidth(self.lbl_1.sizePolicy().hasHeightForWidth())
        self.lbl_1.setSizePolicy(sizePolicy3)
        self.lbl_1.setFont(font4)
        self.lbl_1.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lbl_1, 1, 1, 1, 1)

        self.lbl_15 = DisplayLabel(self.centralwidget)
        self.lbl_15.setObjectName(u"lbl_15")
        sizePolicy2.setHeightForWidth(self.lbl_15.sizePolicy().hasHeightForWidth())
        self.lbl_15.setSizePolicy(sizePolicy2)
        self.lbl_15.setFont(font5)
        self.lbl_15.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lbl_15, 1, 4, 1, 1)

        self.lbl_12 = DisplayLabel(self.centralwidget)
        self.lbl_12.setObjectName(u"lbl_12")
        sizePolicy3.setHeightForWidth(self.lbl_12.sizePolicy().hasHeightForWidth())
        self.lbl_12.setSizePolicy(sizePolicy3)
        self.lbl_12.setFont(font4)
        self.lbl_12.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lbl_12, 4, 3, 1, 1)

        self.lbl_3 = DisplayLabel(self.centralwidget)
        self.lbl_3.setObjectName(u"lbl_3")
        sizePolicy3.setHeightForWidth(self.lbl_3.sizePolicy().hasHeightForWidth())
        self.lbl_3.setSizePolicy(sizePolicy3)
        self.lbl_3.setFont(font4)
        self.lbl_3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lbl_3, 1, 3, 1, 1)

        self.lbl_14 = DisplayLabel(self.centralwidget)
        self.lbl_14.setObjectName(u"lbl_14")
        sizePolicy2.setHeightForWidth(self.lbl_14.sizePolicy().hasHeightForWidth())
        self.lbl_14.setSizePolicy(sizePolicy2)
        self.lbl_14.setFont(font5)
        self.lbl_14.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lbl_14, 1, 0, 1, 1)

        self.lbl_5 = DisplayLabel(self.centralwidget)
        self.lbl_5.setObjectName(u"lbl_5")
        sizePolicy3.setHeightForWidth(self.lbl_5.sizePolicy().hasHeightForWidth())
        self.lbl_5.setSizePolicy(sizePolicy3)
        self.lbl_5.setFont(font4)
        self.lbl_5.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lbl_5, 2, 2, 1, 1)

        self.lbl_2 = DisplayLabel(self.centralwidget)
        self.lbl_2.setObjectName(u"lbl_2")
        sizePolicy3.setHeightForWidth(self.lbl_2.sizePolicy().hasHeightForWidth())
        self.lbl_2.setSizePolicy(sizePolicy3)
        self.lbl_2.setFont(font4)
        self.lbl_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lbl_2, 1, 2, 1, 1)

        self.lbl_6 = DisplayLabel(self.centralwidget)
        self.lbl_6.setObjectName(u"lbl_6")
        sizePolicy3.setHeightForWidth(self.lbl_6.sizePolicy().hasHeightForWidth())
        self.lbl_6.setSizePolicy(sizePolicy3)
        self.lbl_6.setFont(font4)
        self.lbl_6.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lbl_6, 2, 3, 1, 1)

        self.lbl_4 = DisplayLabel(self.centralwidget)
        self.lbl_4.setObjectName(u"lbl_4")
        sizePolicy3.setHeightForWidth(self.lbl_4.sizePolicy().hasHeightForWidth())
        self.lbl_4.setSizePolicy(sizePolicy3)
        self.lbl_4.setFont(font4)
        self.lbl_4.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lbl_4, 2, 1, 1, 1)

        self.lbl_8 = DisplayLabel(self.centralwidget)
        self.lbl_8.setObjectName(u"lbl_8")
        sizePolicy3.setHeightForWidth(self.lbl_8.sizePolicy().hasHeightForWidth())
        self.lbl_8.setSizePolicy(sizePolicy3)
        self.lbl_8.setFont(font4)
        self.lbl_8.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lbl_8, 3, 2, 1, 1)

        self.lbl_16 = DisplayLabel(self.centralwidget)
        self.lbl_16.setObjectName(u"lbl_16")
        sizePolicy2.setHeightForWidth(self.lbl_16.sizePolicy().hasHeightForWidth())
        self.lbl_16.setSizePolicy(sizePolicy2)
        self.lbl_16.setFont(font5)
        self.lbl_16.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lbl_16, 5, 2, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 3, 2, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.lbl_prize_name = DisplayLabel(self.centralwidget)
        self.lbl_prize_name.setObjectName(u"lbl_prize_name")
        sizePolicy2.setHeightForWidth(self.lbl_prize_name.sizePolicy().hasHeightForWidth())
        self.lbl_prize_name.setSizePolicy(sizePolicy2)
        font6 = QFont()
        font6.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font6.setPointSize(36)
        self.lbl_prize_name.setFont(font6)
        self.lbl_prize_name.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.lbl_prize_name)

        self.verticalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_2.addItem(self.verticalSpacer_4)

        self.lbl_prize_name_2 = DisplayLabel(self.centralwidget)
        self.lbl_prize_name_2.setObjectName(u"lbl_prize_name_2")
        sizePolicy2.setHeightForWidth(self.lbl_prize_name_2.sizePolicy().hasHeightForWidth())
        self.lbl_prize_name_2.setSizePolicy(sizePolicy2)
        self.lbl_prize_name_2.setFont(font6)
        self.lbl_prize_name_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.lbl_prize_name_2)

        self.lbl_prize_pic = QLabel(self.centralwidget)
        self.lbl_prize_pic.setObjectName(u"lbl_prize_pic")
        sizePolicy1.setHeightForWidth(self.lbl_prize_pic.sizePolicy().hasHeightForWidth())
        self.lbl_prize_pic.setSizePolicy(sizePolicy1)
        font7 = QFont()
        font7.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font7.setPointSize(26)
        self.lbl_prize_pic.setFont(font7)
        self.lbl_prize_pic.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.lbl_prize_pic)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pb_start = PushButton(self.centralwidget)
        self.pb_start.setObjectName(u"pb_start")
        sizePolicy.setHeightForWidth(self.pb_start.sizePolicy().hasHeightForWidth())
        self.pb_start.setSizePolicy(sizePolicy)
        self.pb_start.setMinimumSize(QSize(150, 30))
        self.pb_start.setMaximumSize(QSize(65535, 65535))
        font8 = QFont()
        font8.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font8.setPointSize(28)
        self.pb_start.setFont(font8)

        self.horizontalLayout_2.addWidget(self.pb_start)

        self.pb_stop = PushButton(self.centralwidget)
        self.pb_stop.setObjectName(u"pb_stop")
        sizePolicy.setHeightForWidth(self.pb_stop.sizePolicy().hasHeightForWidth())
        self.pb_stop.setSizePolicy(sizePolicy)
        self.pb_stop.setMinimumSize(QSize(150, 30))
        self.pb_stop.setMaximumSize(QSize(65535, 65535))
        self.pb_stop.setFont(font8)

        self.horizontalLayout_2.addWidget(self.pb_stop)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.gridLayout_2.addLayout(self.verticalLayout_2, 2, 3, 2, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_5, 2, 0, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_4, 2, 4, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_2.addItem(self.verticalSpacer_5, 1, 0, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 80, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.gridLayout_2.addItem(self.verticalSpacer_6, 4, 0, 1, 1)

        self.lbl_awards_level = DisplayLabel(self.centralwidget)
        self.lbl_awards_level.setObjectName(u"lbl_awards_level")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.lbl_awards_level.sizePolicy().hasHeightForWidth())
        self.lbl_awards_level.setSizePolicy(sizePolicy4)
        font9 = QFont()
        font9.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font9.setPointSize(48)
        font9.setBold(True)
        self.lbl_awards_level.setFont(font9)
        self.lbl_awards_level.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lbl_awards_level, 2, 2, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pb_1 = PushButton(self.centralwidget)
        self.pb_1.setObjectName(u"pb_1")
        sizePolicy2.setHeightForWidth(self.pb_1.sizePolicy().hasHeightForWidth())
        self.pb_1.setSizePolicy(sizePolicy2)
        self.pb_1.setMinimumSize(QSize(150, 30))
        self.pb_1.setMaximumSize(QSize(65535, 65535))
        self.pb_1.setFont(font)

        self.horizontalLayout.addWidget(self.pb_1)

        self.pb_2 = PushButton(self.centralwidget)
        self.pb_2.setObjectName(u"pb_2")
        sizePolicy2.setHeightForWidth(self.pb_2.sizePolicy().hasHeightForWidth())
        self.pb_2.setSizePolicy(sizePolicy2)
        self.pb_2.setMinimumSize(QSize(150, 30))
        self.pb_2.setMaximumSize(QSize(65535, 65535))
        self.pb_2.setFont(font)

        self.horizontalLayout.addWidget(self.pb_2)

        self.pb_3 = PushButton(self.centralwidget)
        self.pb_3.setObjectName(u"pb_3")
        sizePolicy2.setHeightForWidth(self.pb_3.sizePolicy().hasHeightForWidth())
        self.pb_3.setSizePolicy(sizePolicy2)
        self.pb_3.setMinimumSize(QSize(150, 30))
        self.pb_3.setMaximumSize(QSize(65535, 65535))
        self.pb_3.setFont(font)

        self.horizontalLayout.addWidget(self.pb_3)

        self.pb_4 = PushButton(self.centralwidget)
        self.pb_4.setObjectName(u"pb_4")
        sizePolicy2.setHeightForWidth(self.pb_4.sizePolicy().hasHeightForWidth())
        self.pb_4.setSizePolicy(sizePolicy2)
        self.pb_4.setMinimumSize(QSize(150, 30))
        self.pb_4.setMaximumSize(QSize(65535, 65535))
        self.pb_4.setFont(font)

        self.horizontalLayout.addWidget(self.pb_4)


        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 5)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u62bd\u5956", None))
        self.action_about.setText(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e...", None))
        self.action_open.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00...", None))
        self.action_check_update.setText(QCoreApplication.translate("MainWindow", u"\u68c0\u67e5\u66f4\u65b0", None))
        self.action_register.setText(QCoreApplication.translate("MainWindow", u"\u6ce8\u518c...", None))
        self.lbl_temp.setText(QCoreApplication.translate("MainWindow", u"\u4e2d\u5956\u540d\u5355", None))
        self.pb_reset.setText(QCoreApplication.translate("MainWindow", u"\u91cd\u7f6e", None))
        self.lbl_9.setText("")
        self.lbl_13.setText("")
        self.lbl_10.setText("")
        self.lbl_11.setText("")
        self.lbl_7.setText("")
        self.lbl_1.setText("")
        self.lbl_15.setText("")
        self.lbl_12.setText("")
        self.lbl_3.setText("")
        self.lbl_14.setText("")
        self.lbl_5.setText("")
        self.lbl_2.setText("")
        self.lbl_6.setText("")
        self.lbl_4.setText("")
        self.lbl_8.setText("")
        self.lbl_16.setText("")
        self.lbl_prize_name.setText(QCoreApplication.translate("MainWindow", u"\u5956\u54c1\u540d\u79f0", None))
        self.lbl_prize_name_2.setText(QCoreApplication.translate("MainWindow", u"\u5956\u54c1\u540d\u79f0", None))
        self.lbl_prize_pic.setText(QCoreApplication.translate("MainWindow", u"\u5956\u54c1\u56fe\u7247", None))
        self.pb_start.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb", None))
        self.pb_stop.setText(QCoreApplication.translate("MainWindow", u"\u505c\u6b62", None))
        self.lbl_awards_level.setText(QCoreApplication.translate("MainWindow", u"\u5956\u9879\u540d\u79f0", None))
        self.pb_1.setText(QCoreApplication.translate("MainWindow", u"\u53cb\u60c5\u5956", None))
        self.pb_2.setText(QCoreApplication.translate("MainWindow", u"\u4e09\u7b49\u5956", None))
        self.pb_3.setText(QCoreApplication.translate("MainWindow", u"\u4e8c\u7b49\u5956", None))
        self.pb_4.setText(QCoreApplication.translate("MainWindow", u"\u4e00\u7b49\u5956", None))
    # retranslateUi

