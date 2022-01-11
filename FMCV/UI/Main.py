# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QMdiArea, QMenu,
    QMenuBar, QPlainTextEdit, QPushButton, QSizePolicy,
    QSplitter, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1083, 683)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.actionFMCV = QAction(MainWindow)
        self.actionFMCV.setObjectName(u"actionFMCV")
        self.actionTile_Windows = QAction(MainWindow)
        self.actionTile_Windows.setObjectName(u"actionTile_Windows")
        self.actionRun_Single_Step = QAction(MainWindow)
        self.actionRun_Single_Step.setObjectName(u"actionRun_Single_Step")
        self.actionRun_All_Step = QAction(MainWindow)
        self.actionRun_All_Step.setObjectName(u"actionRun_All_Step")
        self.actionSave_Step = QAction(MainWindow)
        self.actionSave_Step.setObjectName(u"actionSave_Step")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionReload_Program = QAction(MainWindow)
        self.actionReload_Program.setObjectName(u"actionReload_Program")
        self.actionEdit_Step = QAction(MainWindow)
        self.actionEdit_Step.setObjectName(u"actionEdit_Step")
        self.actionView_Images = QAction(MainWindow)
        self.actionView_Images.setObjectName(u"actionView_Images")
        self.actionOpen_Program_Folder = QAction(MainWindow)
        self.actionOpen_Program_Folder.setObjectName(u"actionOpen_Program_Folder")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QSize(901, 0))
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Vertical)
        self.mdiArea = QMdiArea(self.splitter)
        self.mdiArea.setObjectName(u"mdiArea")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.mdiArea.sizePolicy().hasHeightForWidth())
        self.mdiArea.setSizePolicy(sizePolicy1)
        self.splitter.addWidget(self.mdiArea)
        self.horizontalLayoutWidget = QWidget(self.splitter)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.addButton = QPushButton(self.horizontalLayoutWidget)
        self.addButton.setObjectName(u"addButton")

        self.verticalLayout_3.addWidget(self.addButton)

        self.lineEdit = QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.verticalLayout_3.addWidget(self.lineEdit)

        self.clear_msgButton = QPushButton(self.horizontalLayoutWidget)
        self.clear_msgButton.setObjectName(u"clear_msgButton")

        self.verticalLayout_3.addWidget(self.clear_msgButton)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.plainTextEdit = QPlainTextEdit(self.horizontalLayoutWidget)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.horizontalLayout.addWidget(self.plainTextEdit)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.prog_nameComboBox = QComboBox(self.horizontalLayoutWidget)
        self.prog_nameComboBox.setObjectName(u"prog_nameComboBox")

        self.verticalLayout.addWidget(self.prog_nameComboBox)

        self.refresh_stepButton = QPushButton(self.horizontalLayoutWidget)
        self.refresh_stepButton.setObjectName(u"refresh_stepButton")

        self.verticalLayout.addWidget(self.refresh_stepButton)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.horizontalLayout.setStretch(1, 1)
        self.splitter.addWidget(self.horizontalLayoutWidget)

        self.verticalLayout_2.addWidget(self.splitter)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1083, 22))
        self.menuAbouts = QMenu(self.menubar)
        self.menuAbouts.setObjectName(u"menuAbouts")
        self.menuView = QMenu(self.menubar)
        self.menuView.setObjectName(u"menuView")
        self.menuProgram = QMenu(self.menubar)
        self.menuProgram.setObjectName(u"menuProgram")
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuProgram.menuAction())
        self.menubar.addAction(self.menuAbouts.menuAction())
        self.menuAbouts.addAction(self.actionFMCV)
        self.menuView.addAction(self.actionTile_Windows)
        self.menuView.addAction(self.actionView_Images)
        self.menuProgram.addAction(self.actionRun_Single_Step)
        self.menuProgram.addAction(self.actionRun_All_Step)
        self.menuProgram.addAction(self.actionEdit_Step)
        self.menuFile.addAction(self.actionOpen_Program_Folder)
        self.menuFile.addAction(self.actionReload_Program)
        self.menuFile.addAction(self.actionExit)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"FMCV AI CNN Deep Learning System", None))
        self.actionFMCV.setText(QCoreApplication.translate("MainWindow", u"FMCV", None))
        self.actionTile_Windows.setText(QCoreApplication.translate("MainWindow", u"Tile Windows", None))
        self.actionRun_Single_Step.setText(QCoreApplication.translate("MainWindow", u"Run Single Step", None))
        self.actionRun_All_Step.setText(QCoreApplication.translate("MainWindow", u"Run All Step", None))
        self.actionSave_Step.setText(QCoreApplication.translate("MainWindow", u"Save Step", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.actionReload_Program.setText(QCoreApplication.translate("MainWindow", u"Reload Program", None))
        self.actionEdit_Step.setText(QCoreApplication.translate("MainWindow", u"Edit Step", None))
        self.actionView_Images.setText(QCoreApplication.translate("MainWindow", u"View Images", None))
        self.actionOpen_Program_Folder.setText(QCoreApplication.translate("MainWindow", u"Open Program Folder", None))
        self.addButton.setText(QCoreApplication.translate("MainWindow", u"Add Program", None))
        self.clear_msgButton.setText(QCoreApplication.translate("MainWindow", u"Clear Message", None))
        self.plainTextEdit.setPlainText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Current Program : ", None))
        self.refresh_stepButton.setText(QCoreApplication.translate("MainWindow", u"Load Program", None))
        self.menuAbouts.setTitle(QCoreApplication.translate("MainWindow", u"About", None))
        self.menuView.setTitle(QCoreApplication.translate("MainWindow", u"View", None))
        self.menuProgram.setTitle(QCoreApplication.translate("MainWindow", u"Program", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

