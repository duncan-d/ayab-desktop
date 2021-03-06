# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/main/python/ayab/ayab_gui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1008, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.image_side_panel = QtWidgets.QVBoxLayout()
        self.image_side_panel.setSpacing(6)
        self.image_side_panel.setObjectName("image_side_panel")
        self.image_pattern_view = QtWidgets.QGraphicsView(self.centralwidget)
        self.image_pattern_view.setObjectName("image_pattern_view")
        self.image_side_panel.addWidget(self.image_pattern_view)
        self.progressLayout = QtWidgets.QHBoxLayout()
        self.progressLayout.setSpacing(2)
        self.progressLayout.setObjectName("progressLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_current_color = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.label_current_color.setFont(font)
        self.label_current_color.setObjectName("label_current_color")
        self.horizontalLayout.addWidget(self.label_current_color, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.progressLayout.addLayout(self.horizontalLayout)
        self.label_current_line = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_current_line.setFont(font)
        self.label_current_line.setObjectName("label_current_line")
        self.progressLayout.addWidget(self.label_current_line, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.image_side_panel.addLayout(self.progressLayout)
        self.label_notifications = QtWidgets.QLabel(self.centralwidget)
        self.label_notifications.setAlignment(QtCore.Qt.AlignCenter)
        self.label_notifications.setObjectName("label_notifications")
        self.image_side_panel.addWidget(self.label_notifications)
        self.gridLayout.addLayout(self.image_side_panel, 0, 0, 3, 1)
        self.assistant_dock = QtWidgets.QScrollArea(self.centralwidget)
        self.assistant_dock.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.assistant_dock.sizePolicy().hasHeightForWidth())
        self.assistant_dock.setSizePolicy(sizePolicy)
        self.assistant_dock.setMinimumSize(QtCore.QSize(280, 0))
        self.assistant_dock.setMaximumSize(QtCore.QSize(540, 16777215))
        self.assistant_dock.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.assistant_dock.setFrameShadow(QtWidgets.QFrame.Plain)
        self.assistant_dock.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.assistant_dock.setWidgetResizable(False)
        self.assistant_dock.setObjectName("assistant_dock")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setGeometry(QtCore.QRect(0, 0, 500, 700))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidgetContents.sizePolicy().hasHeightForWidth())
        self.dockWidgetContents.setSizePolicy(sizePolicy)
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_5.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.widget_imgload = QtWidgets.QVBoxLayout()
        self.widget_imgload.setObjectName("widget_imgload")
        self.horizontal_layout = QtWidgets.QHBoxLayout()
        self.horizontal_layout.setObjectName("horizontal_layout")
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontal_layout.addItem(spacerItem)
        self.filename_lineedit = QtWidgets.QLineEdit(self.dockWidgetContents)
        self.filename_lineedit.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filename_lineedit.sizePolicy().hasHeightForWidth())
        self.filename_lineedit.setSizePolicy(sizePolicy)
        self.filename_lineedit.setText("")
        self.filename_lineedit.setObjectName("filename_lineedit")
        self.horizontal_layout.addWidget(self.filename_lineedit)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontal_layout.addItem(spacerItem1)
        self.widget_imgload.addLayout(self.horizontal_layout)
        self.load_file_button = QtWidgets.QPushButton(self.dockWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.load_file_button.sizePolicy().hasHeightForWidth())
        self.load_file_button.setSizePolicy(sizePolicy)
        self.load_file_button.setObjectName("load_file_button")
        self.widget_imgload.addWidget(self.load_file_button, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_5.addLayout(self.widget_imgload)
        self.widget_optionsdock = QtWidgets.QWidget(self.dockWidgetContents)
        self.widget_optionsdock.setEnabled(False)
        self.widget_optionsdock.setObjectName("widget_optionsdock")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_optionsdock)
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.line = QtWidgets.QFrame(self.widget_optionsdock)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.knitting_options_dock = QtWidgets.QDockWidget(self.widget_optionsdock)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.knitting_options_dock.sizePolicy().hasHeightForWidth())
        self.knitting_options_dock.setSizePolicy(sizePolicy)
        self.knitting_options_dock.setObjectName("knitting_options_dock")
        self.dockWidgetContents_2 = QtWidgets.QWidget()
        self.dockWidgetContents_2.setObjectName("dockWidgetContents_2")
        self.knitting_options_dock.setWidget(self.dockWidgetContents_2)
        self.verticalLayout_2.addWidget(self.knitting_options_dock)
        self.verticalLayout_5.addWidget(self.widget_optionsdock, 0, QtCore.Qt.AlignHCenter)
        self.line_2 = QtWidgets.QFrame(self.dockWidgetContents)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_5.addWidget(self.line_2)
        self.widget_knitcontrol = QtWidgets.QWidget(self.dockWidgetContents)
        self.widget_knitcontrol.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_knitcontrol.sizePolicy().hasHeightForWidth())
        self.widget_knitcontrol.setSizePolicy(sizePolicy)
        self.widget_knitcontrol.setObjectName("widget_knitcontrol")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_knitcontrol)
        self.verticalLayout_3.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.knit_button = QtWidgets.QPushButton(self.widget_knitcontrol)
        self.knit_button.setEnabled(False)
        self.knit_button.setObjectName("knit_button")
        self.verticalLayout_3.addWidget(self.knit_button)
        self.cancel_button = QtWidgets.QPushButton(self.widget_knitcontrol)
        self.cancel_button.setEnabled(False)
        self.cancel_button.setObjectName("cancel_button")
        self.verticalLayout_3.addWidget(self.cancel_button)
        self.verticalLayout_5.addWidget(self.widget_knitcontrol, 0, QtCore.Qt.AlignHCenter)
        self.assistant_dock.setWidget(self.dockWidgetContents)
        self.gridLayout.addWidget(self.assistant_dock, 0, 1, 3, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1008, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuTools = QtWidgets.QMenu(self.menubar)
        self.menuTools.setObjectName("menuTools")
        self.menuImage_Actions = QtWidgets.QMenu(self.menubar)
        self.menuImage_Actions.setEnabled(False)
        self.menuImage_Actions.setObjectName("menuImage_Actions")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionLoad_AYAB_Firmware = QtWidgets.QAction(MainWindow)
        self.actionLoad_AYAB_Firmware.setObjectName("actionLoad_AYAB_Firmware")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionOpen_Knitting_Project = QtWidgets.QAction(MainWindow)
        self.actionOpen_Knitting_Project.setObjectName("actionOpen_Knitting_Project")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.actionInvert = QtWidgets.QAction(MainWindow)
        self.actionInvert.setObjectName("actionInvert")
        self.actionRepeat = QtWidgets.QAction(MainWindow)
        self.actionRepeat.setObjectName("actionRepeat")
        self.actionMirror = QtWidgets.QAction(MainWindow)
        self.actionMirror.setObjectName("actionMirror")
        self.actionRotate_Left = QtWidgets.QAction(MainWindow)
        self.actionRotate_Left.setObjectName("actionRotate_Left")
        self.actionRotate_Right = QtWidgets.QAction(MainWindow)
        self.actionRotate_Right.setObjectName("actionRotate_Right")
        self.actionSmart_Resize = QtWidgets.QAction(MainWindow)
        self.actionSmart_Resize.setObjectName("actionSmart_Resize")
        self.actionVertical_Flip = QtWidgets.QAction(MainWindow)
        self.actionVertical_Flip.setObjectName("actionVertical_Flip")
        self.menuFile.addAction(self.actionQuit)
        self.menuHelp.addAction(self.actionAbout)
        self.menuTools.addAction(self.actionLoad_AYAB_Firmware)
        self.menuImage_Actions.addAction(self.actionInvert)
        self.menuImage_Actions.addAction(self.actionRepeat)
        self.menuImage_Actions.addSeparator()
        self.menuImage_Actions.addAction(self.actionVertical_Flip)
        self.menuImage_Actions.addAction(self.actionMirror)
        self.menuImage_Actions.addSeparator()
        self.menuImage_Actions.addAction(self.actionRotate_Left)
        self.menuImage_Actions.addAction(self.actionRotate_Right)
        self.menuImage_Actions.addSeparator()
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuImage_Actions.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "All Yarns Are Beautiful"))
        self.label_current_color.setText(_translate("MainWindow", "label_current_color"))
        self.label_current_line.setText(_translate("MainWindow", "label_current_line"))
        self.label_notifications.setText(_translate("MainWindow", "label_notifications"))
        self.assistant_dock.setWindowTitle(_translate("MainWindow", "Asistant"))
        self.load_file_button.setText(_translate("MainWindow", "1. Load Image File"))
        self.load_file_button.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.knitting_options_dock.setWindowTitle(_translate("MainWindow", "Knitting Options"))
        self.knit_button.setText(_translate("MainWindow", "3. Knit!"))
        self.knit_button.setShortcut(_translate("MainWindow", "Ctrl+Return"))
        self.cancel_button.setText(_translate("MainWindow", "Cancel Knitting"))
        self.cancel_button.setShortcut(_translate("MainWindow", "Esc"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuTools.setTitle(_translate("MainWindow", "Tools"))
        self.menuImage_Actions.setTitle(_translate("MainWindow", "Image Actions"))
        self.actionLoad_AYAB_Firmware.setText(_translate("MainWindow", "Load AYAB Firmware"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionQuit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionOpen_Knitting_Project.setText(_translate("MainWindow", "Open Knitting Project"))
        self.actionAbout.setText(_translate("MainWindow", "Help - About"))
        self.actionHelp.setText(_translate("MainWindow", "Help"))
        self.actionInvert.setText(_translate("MainWindow", "Invert"))
        self.actionInvert.setShortcut(_translate("MainWindow", "Ctrl+I"))
        self.actionRepeat.setText(_translate("MainWindow", "Repeat"))
        self.actionRepeat.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.actionMirror.setText(_translate("MainWindow", "Mirror"))
        self.actionMirror.setShortcut(_translate("MainWindow", "Ctrl+Up"))
        self.actionRotate_Left.setText(_translate("MainWindow", "Rotate Left"))
        self.actionRotate_Left.setShortcut(_translate("MainWindow", "Ctrl+Left"))
        self.actionRotate_Right.setText(_translate("MainWindow", "Rotate Right"))
        self.actionRotate_Right.setShortcut(_translate("MainWindow", "Ctrl+Right"))
        self.actionSmart_Resize.setText(_translate("MainWindow", "Smart Resize"))
        self.actionVertical_Flip.setText(_translate("MainWindow", "Vertical Flip"))
        self.actionVertical_Flip.setShortcut(_translate("MainWindow", "Ctrl+Down"))

