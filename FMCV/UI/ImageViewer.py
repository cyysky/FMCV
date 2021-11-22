# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ImageViewer.ui'
##
## Created by: Qt User Interface Compiler version 6.2.0
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
from PySide6.QtWidgets import (QApplication, QGraphicsView, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_ImageViewer(object):
    def setupUi(self, ImageViewer):
        if not ImageViewer.objectName():
            ImageViewer.setObjectName(u"ImageViewer")
        ImageViewer.resize(672, 430)
        self.verticalLayout = QVBoxLayout(ImageViewer)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.graphicsView = QGraphicsView(ImageViewer)
        self.graphicsView.setObjectName(u"graphicsView")

        self.verticalLayout.addWidget(self.graphicsView)


        self.retranslateUi(ImageViewer)

        QMetaObject.connectSlotsByName(ImageViewer)
    # setupUi

    def retranslateUi(self, ImageViewer):
        ImageViewer.setWindowTitle(QCoreApplication.translate("ImageViewer", u"Title", None))
    # retranslateUi

