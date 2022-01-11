# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SliderWidget.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QSizePolicy,
    QSlider, QVBoxLayout, QWidget)

class Ui_SliderWidget(object):
    def setupUi(self, SliderWidget):
        if not SliderWidget.objectName():
            SliderWidget.setObjectName(u"SliderWidget")
        SliderWidget.resize(334, 79)
        self.verticalLayout_2 = QVBoxLayout(SliderWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_min = QLabel(SliderWidget)
        self.label_min.setObjectName(u"label_min")

        self.horizontalLayout.addWidget(self.label_min)

        self.label_value = QLabel(SliderWidget)
        self.label_value.setObjectName(u"label_value")
        self.label_value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_value)

        self.label_max = QLabel(SliderWidget)
        self.label_max.setObjectName(u"label_max")
        self.label_max.setLayoutDirection(Qt.LeftToRight)
        self.label_max.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.label_max)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalSlider = QSlider(SliderWidget)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.verticalLayout_2.addWidget(self.horizontalSlider)


        self.retranslateUi(SliderWidget)

        QMetaObject.connectSlotsByName(SliderWidget)
    # setupUi

    def retranslateUi(self, SliderWidget):
        SliderWidget.setWindowTitle(QCoreApplication.translate("SliderWidget", u"Form", None))
        self.label_min.setText(QCoreApplication.translate("SliderWidget", u"min", None))
        self.label_value.setText(QCoreApplication.translate("SliderWidget", u"value", None))
        self.label_max.setText(QCoreApplication.translate("SliderWidget", u"max", None))
    # retranslateUi

