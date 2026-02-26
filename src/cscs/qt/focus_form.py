# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'focus_form.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QGroupBox, QLabel,
    QLineEdit, QListView, QPushButton, QSizePolicy,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_FocusForm(object):
    def setupUi(self, FocusForm):
        if not FocusForm.objectName():
            FocusForm.setObjectName(u"FocusForm")
        FocusForm.resize(617, 475)
        self.verticalLayoutWidget = QWidget(FocusForm)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 591, 421))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.nameLabel = QLabel(self.verticalLayoutWidget)
        self.nameLabel.setObjectName(u"nameLabel")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.nameLabel)

        self.nameLineEdit = QLineEdit(self.verticalLayoutWidget)
        self.nameLineEdit.setObjectName(u"nameLineEdit")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.nameLineEdit)

        self.cSPageLabel = QLabel(self.verticalLayoutWidget)
        self.cSPageLabel.setObjectName(u"cSPageLabel")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.cSPageLabel)

        self.cSPageLineEdit = QLineEdit(self.verticalLayoutWidget)
        self.cSPageLineEdit.setObjectName(u"cSPageLineEdit")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.cSPageLineEdit)

        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label)


        self.verticalLayout.addLayout(self.formLayout)

        self.descriptionEdit = QTextEdit(self.verticalLayoutWidget)
        self.descriptionEdit.setObjectName(u"descriptionEdit")

        self.verticalLayout.addWidget(self.descriptionEdit)

        self.groupBox = QGroupBox(self.verticalLayoutWidget)
        self.groupBox.setObjectName(u"groupBox")
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 10, 66, 17))
        self.addAbilityBtn = QPushButton(self.groupBox)
        self.addAbilityBtn.setObjectName(u"addAbilityBtn")
        self.addAbilityBtn.setGeometry(QRect(540, 10, 21, 25))
        self.delAbilityBtn = QPushButton(self.groupBox)
        self.delAbilityBtn.setObjectName(u"delAbilityBtn")
        self.delAbilityBtn.setGeometry(QRect(560, 10, 21, 25))

        self.verticalLayout.addWidget(self.groupBox)

        self.abilityList = QListView(self.verticalLayoutWidget)
        self.abilityList.setObjectName(u"abilityList")

        self.verticalLayout.addWidget(self.abilityList)

        self.pushButton = QPushButton(FocusForm)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setEnabled(False)
        self.pushButton.setGeometry(QRect(500, 440, 94, 25))

        self.retranslateUi(FocusForm)

        QMetaObject.connectSlotsByName(FocusForm)
    # setupUi

    def retranslateUi(self, FocusForm):
        FocusForm.setWindowTitle(QCoreApplication.translate("FocusForm", u"Form", None))
        self.nameLabel.setText(QCoreApplication.translate("FocusForm", u"Name", None))
        self.cSPageLabel.setText(QCoreApplication.translate("FocusForm", u"CS Page", None))
        self.label.setText(QCoreApplication.translate("FocusForm", u"Description", None))
        self.groupBox.setTitle("")
        self.label_2.setText(QCoreApplication.translate("FocusForm", u"Abilities", None))
        self.addAbilityBtn.setText(QCoreApplication.translate("FocusForm", u"+", None))
        self.delAbilityBtn.setText(QCoreApplication.translate("FocusForm", u"-", None))
        self.pushButton.setText(QCoreApplication.translate("FocusForm", u"Save", None))
    # retranslateUi

