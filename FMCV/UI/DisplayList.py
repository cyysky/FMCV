# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DisplayList.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QListView, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_DisplayList(object):
    def setupUi(self, DisplayList):
        if not DisplayList.objectName():
            DisplayList.setObjectName(u"DisplayList")
        DisplayList.resize(695, 462)
        self.horizontalLayout = QHBoxLayout(DisplayList)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.listView = QListView(DisplayList)
        self.listView.setObjectName(u"listView")

        self.horizontalLayout.addWidget(self.listView)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.roiButton = QPushButton(DisplayList)
        self.roiButton.setObjectName(u"roiButton")

        self.verticalLayout.addWidget(self.roiButton)

        self.label = QLabel(DisplayList)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.update_dirButton = QPushButton(DisplayList)
        self.update_dirButton.setObjectName(u"update_dirButton")

        self.verticalLayout.addWidget(self.update_dirButton)

        self.label_2 = QLabel(DisplayList)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.first_dircomboBox = QComboBox(DisplayList)
        self.first_dircomboBox.setObjectName(u"first_dircomboBox")

        self.verticalLayout.addWidget(self.first_dircomboBox)

        self.label_3 = QLabel(DisplayList)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.second_dircomboBox = QComboBox(DisplayList)
        self.second_dircomboBox.setObjectName(u"second_dircomboBox")

        self.verticalLayout.addWidget(self.second_dircomboBox)

        self.label_5 = QLabel(DisplayList)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout.addWidget(self.label_5)

        self.file_typecomboBox = QComboBox(DisplayList)
        self.file_typecomboBox.setObjectName(u"file_typecomboBox")

        self.verticalLayout.addWidget(self.file_typecomboBox)

        self.label_4 = QLabel(DisplayList)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.lineEdit = QLineEdit(DisplayList)
        self.lineEdit.setObjectName(u"lineEdit")

        self.verticalLayout.addWidget(self.lineEdit)

        self.saveButton = QPushButton(DisplayList)
        self.saveButton.setObjectName(u"saveButton")

        self.verticalLayout.addWidget(self.saveButton)

        self.save_roiButton = QPushButton(DisplayList)
        self.save_roiButton.setObjectName(u"save_roiButton")

        self.verticalLayout.addWidget(self.save_roiButton)

        self.file_explorerButton = QPushButton(DisplayList)
        self.file_explorerButton.setObjectName(u"file_explorerButton")

        self.verticalLayout.addWidget(self.file_explorerButton)

        self.frame = QFrame(DisplayList)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.frame)

        self.verticalLayout.setStretch(14, 1)

        self.horizontalLayout.addLayout(self.verticalLayout)

        self.horizontalLayout.setStretch(0, 5)
        self.horizontalLayout.setStretch(1, 2)

        self.retranslateUi(DisplayList)

        QMetaObject.connectSlotsByName(DisplayList)
    # setupUi

    def retranslateUi(self, DisplayList):
        DisplayList.setWindowTitle(QCoreApplication.translate("DisplayList", u"Steps Images Display Lists", None))
        self.roiButton.setText(QCoreApplication.translate("DisplayList", u"Select Roi", None))
        self.label.setText(QCoreApplication.translate("DisplayList", u"TextLabel", None))
        self.update_dirButton.setText(QCoreApplication.translate("DisplayList", u"Refresh Folders", None))
        self.label_2.setText(QCoreApplication.translate("DisplayList", u"Folder First Level", None))
        self.label_3.setText(QCoreApplication.translate("DisplayList", u"Folder Second Level", None))
        self.label_5.setText(QCoreApplication.translate("DisplayList", u"File Type", None))
        self.label_4.setText(QCoreApplication.translate("DisplayList", u"File Name", None))
        self.saveButton.setText(QCoreApplication.translate("DisplayList", u"Save Image", None))
        self.save_roiButton.setText(QCoreApplication.translate("DisplayList", u"Save ROI Image", None))
        self.file_explorerButton.setText(QCoreApplication.translate("DisplayList", u"Explore Folder", None))
    # retranslateUi

