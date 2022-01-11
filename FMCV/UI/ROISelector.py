# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ROISelector.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGraphicsView,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_ROISelector(object):
    def setupUi(self, ROISelector):
        if not ROISelector.objectName():
            ROISelector.setObjectName(u"ROISelector")
        ROISelector.resize(749, 504)
        self.verticalLayout = QVBoxLayout(ROISelector)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(ROISelector)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.lineEdit = QLineEdit(ROISelector)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_2.addWidget(self.lineEdit)

        self.save_imageButton = QPushButton(ROISelector)
        self.save_imageButton.setObjectName(u"save_imageButton")

        self.horizontalLayout_2.addWidget(self.save_imageButton)

        self.save_roiButton = QPushButton(ROISelector)
        self.save_roiButton.setObjectName(u"save_roiButton")

        self.horizontalLayout_2.addWidget(self.save_roiButton)

        self.horizontalLayout_2.setStretch(0, 10)
        self.horizontalLayout_2.setStretch(1, 3)
        self.horizontalLayout_2.setStretch(3, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.graphicsView = QGraphicsView(ROISelector)
        self.graphicsView.setObjectName(u"graphicsView")

        self.horizontalLayout.addWidget(self.graphicsView)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.comboBox = QComboBox(ROISelector)
        self.comboBox.setObjectName(u"comboBox")

        self.verticalLayout_2.addWidget(self.comboBox)

        self.cameraButton = QPushButton(ROISelector)
        self.cameraButton.setObjectName(u"cameraButton")

        self.verticalLayout_2.addWidget(self.cameraButton)

        self.clipboardButton = QPushButton(ROISelector)
        self.clipboardButton.setObjectName(u"clipboardButton")

        self.verticalLayout_2.addWidget(self.clipboardButton)

        self.file_explorerButton = QPushButton(ROISelector)
        self.file_explorerButton.setObjectName(u"file_explorerButton")

        self.verticalLayout_2.addWidget(self.file_explorerButton)

        self.frame = QFrame(ROISelector)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout_2.addWidget(self.frame)

        self.verticalLayout_2.setStretch(3, 2)

        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(ROISelector)

        QMetaObject.connectSlotsByName(ROISelector)
    # setupUi

    def retranslateUi(self, ROISelector):
        ROISelector.setWindowTitle(QCoreApplication.translate("ROISelector", u"ROI Selector", None))
        self.label.setText(QCoreApplication.translate("ROISelector", u"ROI", None))
        self.save_imageButton.setText(QCoreApplication.translate("ROISelector", u"Save Image", None))
        self.save_roiButton.setText(QCoreApplication.translate("ROISelector", u"Save ROI To Image", None))
        self.cameraButton.setText(QCoreApplication.translate("ROISelector", u"Camera", None))
        self.clipboardButton.setText(QCoreApplication.translate("ROISelector", u"Copy ROI", None))
        self.file_explorerButton.setText(QCoreApplication.translate("ROISelector", u"File Explorer", None))
    # retranslateUi

