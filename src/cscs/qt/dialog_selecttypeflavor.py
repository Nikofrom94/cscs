# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_selecttypeflavor.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDialog,
    QDialogButtonBox, QFormLayout, QLabel, QSizePolicy,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 137)
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(40, 90, 341, 32))
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.formLayoutWidget = QWidget(Dialog)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 10, 381, 61))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.typeLabel = QLabel(self.formLayoutWidget)
        self.typeLabel.setObjectName(u"typeLabel")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.typeLabel)

        self.typeComboBox = QComboBox(self.formLayoutWidget)
        self.typeComboBox.setObjectName(u"typeComboBox")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.typeComboBox)

        self.flavorLabel = QLabel(self.formLayoutWidget)
        self.flavorLabel.setObjectName(u"flavorLabel")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.flavorLabel)

        self.flavorComboBox = QComboBox(self.formLayoutWidget)
        self.flavorComboBox.setObjectName(u"flavorComboBox")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.flavorComboBox)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.typeLabel.setText(QCoreApplication.translate("Dialog", u"Type", None))
        self.flavorLabel.setText(QCoreApplication.translate("Dialog", u"Flavor", None))
    # retranslateUi

