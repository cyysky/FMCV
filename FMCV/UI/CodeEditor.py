# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CodeEditor.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QPlainTextEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_TextEditor(object):
    def setupUi(self, TextEditor):
        if not TextEditor.objectName():
            TextEditor.setObjectName(u"TextEditor")
        TextEditor.resize(698, 562)
        self.horizontalLayout = QHBoxLayout(TextEditor)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.textEdit = QPlainTextEdit(TextEditor)
        self.textEdit.setObjectName(u"textEdit")

        self.horizontalLayout.addWidget(self.textEdit)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.saveButton = QPushButton(TextEditor)
        self.saveButton.setObjectName(u"saveButton")

        self.verticalLayout.addWidget(self.saveButton)

        self.run_allButton = QPushButton(TextEditor)
        self.run_allButton.setObjectName(u"run_allButton")

        self.verticalLayout.addWidget(self.run_allButton)

        self.run_stepButton = QPushButton(TextEditor)
        self.run_stepButton.setObjectName(u"run_stepButton")

        self.verticalLayout.addWidget(self.run_stepButton)

        self.toolComboBox = QComboBox(TextEditor)
        self.toolComboBox.setObjectName(u"toolComboBox")

        self.verticalLayout.addWidget(self.toolComboBox)

        self.InsertButton = QPushButton(TextEditor)
        self.InsertButton.setObjectName(u"InsertButton")

        self.verticalLayout.addWidget(self.InsertButton)

        self.frame = QFrame(TextEditor)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.frame)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.horizontalLayout.setStretch(0, 8)
        self.horizontalLayout.setStretch(1, 1)

        self.retranslateUi(TextEditor)

        QMetaObject.connectSlotsByName(TextEditor)
    # setupUi

    def retranslateUi(self, TextEditor):
        TextEditor.setWindowTitle(QCoreApplication.translate("TextEditor", u"Form", None))
        self.saveButton.setText(QCoreApplication.translate("TextEditor", u"Save", None))
        self.run_allButton.setText(QCoreApplication.translate("TextEditor", u"Run All", None))
        self.run_stepButton.setText(QCoreApplication.translate("TextEditor", u"Run Step", None))
        self.InsertButton.setText(QCoreApplication.translate("TextEditor", u"Insert", None))
    # retranslateUi

