# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Сергей\Desktop\qt_quad\me\second_design_26.03.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1136, 728)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1098, 659))
        MainWindow.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.img_btn = QtWidgets.QPushButton(self.centralwidget)
        self.img_btn.setGeometry(QtCore.QRect(20, 80, 121, 81))
        self.img_btn.setMinimumSize(QtCore.QSize(121, 81))
        self.img_btn.setMaximumSize(QtCore.QSize(121, 81))
        self.img_btn.setObjectName("img_btn")
        self.img_btn_2 = QtWidgets.QPushButton(self.centralwidget)
        self.img_btn_2.setGeometry(QtCore.QRect(20, 20, 121, 41))
        self.img_btn_2.setMinimumSize(QtCore.QSize(121, 41))
        self.img_btn_2.setMaximumSize(QtCore.QSize(121, 41))
        self.img_btn_2.setObjectName("img_btn_2")
        self.img_btn_2.clicked.connect(self.On_Off_event)
        self.columnView = QtWidgets.QColumnView(self.centralwidget)
        self.columnView.setGeometry(QtCore.QRect(10, 10, 141, 591))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.columnView.sizePolicy().hasHeightForWidth())
        self.columnView.setSizePolicy(sizePolicy)
        self.columnView.setMinimumSize(QtCore.QSize(0, 0))
        self.columnView.setMaximumSize(QtCore.QSize(141, 16777215))
        self.columnView.setObjectName("columnView")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 60, 141, 20))
        self.line.setMinimumSize(QtCore.QSize(141, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(161, 11, 920, 593))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox_2 = QtWidgets.QGroupBox(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setMinimumSize(QtCore.QSize(651, 501))
        self.groupBox_2.setObjectName("groupBox_2")
        self.img_laebl = QtWidgets.QLabel(self.groupBox_2)
        self.img_laebl.setGeometry(QtCore.QRect(10, 20, 631, 471))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.img_laebl.sizePolicy().hasHeightForWidth())
        self.img_laebl.setSizePolicy(sizePolicy)
        self.img_laebl.setMinimumSize(QtCore.QSize(631, 471))
        self.img_laebl.setObjectName("img_laebl")
        self.gridLayout.addWidget(self.groupBox_2, 0, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(261, 591))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.text_label = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.text_label.sizePolicy().hasHeightForWidth())
        self.text_label.setSizePolicy(sizePolicy)
        self.text_label.setMouseTracking(False)
        self.text_label.setAutoFillBackground(False)
        self.text_label.setObjectName("text_label")
        self.verticalLayout.addWidget(self.text_label)
        self.gridLayout.addWidget(self.groupBox, 0, 1, 2, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setMinimumSize(QtCore.QSize(651, 81))
        self.groupBox_3.setSizeIncrement(QtCore.QSize(0, 0))
        self.groupBox_3.setObjectName("groupBox_3")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox_3)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 20, 631, 51))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_power_up = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_power_up.sizePolicy().hasHeightForWidth())
        self.btn_power_up.setSizePolicy(sizePolicy)
        self.btn_power_up.setObjectName("btn_power_up")
        self.horizontalLayout.addWidget(self.btn_power_up)
        self.btn_power_down = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_power_down.sizePolicy().hasHeightForWidth())
        self.btn_power_down.setSizePolicy(sizePolicy)
        self.btn_power_down.setObjectName("btn_power_down")
        self.horizontalLayout.addWidget(self.btn_power_down)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.gridLayout.addWidget(self.groupBox_3, 1, 0, 1, 1)
        self.columnView.raise_()
        self.img_btn_2.raise_()
        self.groupBox.raise_()
        self.line.raise_()
        self.img_btn.raise_()
        self.groupBox_2.raise_()
        self.groupBox_3.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1136, 25))
        self.menubar.setObjectName("menubar")
        self.menuMenu_2 = QtWidgets.QMenu(self.menubar)
        self.menuMenu_2.setObjectName("menuMenu_2")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.exit_menu = QtWidgets.QAction(MainWindow)
        self.exit_menu.setObjectName("exit_menu")
        self.change_img_menu = QtWidgets.QAction(MainWindow)
        self.change_img_menu.setObjectName("change_img_menu")
        self.actionOn_Off = QtWidgets.QAction(MainWindow)
        self.actionOn_Off.setObjectName("actionOn_Off")
        self.actionOn_Off.triggered.connect(self.On_Off_event)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionShow_Stop_Translation = QtWidgets.QAction(MainWindow)
        self.actionShow_Stop_Translation.setObjectName("actionShow_Stop_Translation")
        self.actionShow_Stop_Translation.triggered.connect(self.img_event)
        self.actionShow_Messages = QtWidgets.QAction(MainWindow)
        self.actionShow_Messages.setCheckable(True)
        self.actionShow_Messages.setChecked(True)
        self.actionShow_Messages.setObjectName("actionShow_Messages")
        self.actionShow_Messages.triggered.connect(self.show_hide_Messages_event)
        self.menuMenu_2.addAction(self.actionOn_Off)
        self.menuMenu_2.addAction(self.actionShow_Stop_Translation)
        self.menuMenu_2.addSeparator()
        self.menuMenu_2.addAction(self.actionExit)
        self.menuView.addAction(self.actionShow_Messages)
        self.menubar.addAction(self.menuMenu_2.menuAction())
        self.menubar.addAction(self.menuView.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def On_Off_event(self):
        #прописать команду на выключение системы
        #on_off_need
        print('System (should be) turned off/on')

    def img_event(self):
        #прописать функцию остановки/воспроизведения изображения
        #img_need
        print('Image (should be) hiden/played')

    def show_hide_Messages_event(self, state):
        #Messages are in groupBox element of QGroupBox class
        if state:
            self.groupBox.show()
        else:
            self.groupBox.hide()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.img_btn.setText(_translate("MainWindow", "IMG\n"
"(play/pause pic)"))
        self.img_btn_2.setText(_translate("MainWindow", "ON/OFF"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Translation"))
        self.img_laebl.setText(_translate("MainWindow", "TextLabel"))
        self.groupBox.setTitle(_translate("MainWindow", "Messages"))
        self.text_label.setText(_translate("MainWindow", "TextLabel"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Control"))
        self.btn_power_up.setText(_translate("MainWindow", "power UP"))
        self.btn_power_down.setText(_translate("MainWindow", "power DOWN"))
        self.label.setText(_translate("MainWindow", "Use WASD to control flight direction"))
        self.menuMenu_2.setTitle(_translate("MainWindow", "Menu"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.exit_menu.setText(_translate("MainWindow", "exit"))
        self.change_img_menu.setText(_translate("MainWindow", "change_img"))
        self.actionOn_Off.setText(_translate("MainWindow", "On/Off"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionShow_Stop_Translation.setText(_translate("MainWindow", "Show/Stop Translation"))
        self.actionShow_Messages.setText(_translate("MainWindow", "Show Messages"))
        
