# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ability_form.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_AbilityForm(object):
    def setupUi(self, AbilityForm):
        if not AbilityForm.objectName():
            AbilityForm.setObjectName(u"AbilityForm")
        AbilityForm.resize(616, 337)
        self.saveButton = QPushButton(AbilityForm)
        self.saveButton.setObjectName(u"saveButton")
        self.saveButton.setEnabled(False)
        self.saveButton.setGeometry(QRect(510, 270, 94, 25))
        self.layoutWidget = QWidget(AbilityForm)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, -1, 611, 252))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(9, 0, 0, 0)
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.nameLabel = QLabel(self.layoutWidget)
        self.nameLabel.setObjectName(u"nameLabel")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.nameLabel)

        self.nameLineEdit = QLineEdit(self.layoutWidget)
        self.nameLineEdit.setObjectName(u"nameLineEdit")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.nameLineEdit)

        self.statLabel = QLabel(self.layoutWidget)
        self.statLabel.setObjectName(u"statLabel")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.statLabel)

        self.statLineEdit = QLineEdit(self.layoutWidget)
        self.statLineEdit.setObjectName(u"statLineEdit")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.statLineEdit)

        self.tierLabel = QLabel(self.layoutWidget)
        self.tierLabel.setObjectName(u"tierLabel")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.tierLabel)

        self.tierComboBox = QComboBox(self.layoutWidget)
        self.tierComboBox.setObjectName(u"tierComboBox")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.tierComboBox)

        self.cSPageLabel = QLabel(self.layoutWidget)
        self.cSPageLabel.setObjectName(u"cSPageLabel")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.cSPageLabel)

        self.cSPageLineEdit = QLineEdit(self.layoutWidget)
        self.cSPageLineEdit.setObjectName(u"cSPageLineEdit")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.cSPageLineEdit)


        self.verticalLayout.addLayout(self.formLayout)

        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.descriptionEdit = QTextEdit(self.layoutWidget)
        self.descriptionEdit.setObjectName(u"descriptionEdit")

        self.verticalLayout.addWidget(self.descriptionEdit)


        self.retranslateUi(AbilityForm)

        QMetaObject.connectSlotsByName(AbilityForm)
    # setupUi

    def retranslateUi(self, AbilityForm):
        AbilityForm.setWindowTitle(qtTrId(u""))
        self.saveButton.setText(qtTrId(u""))
        self.nameLabel.setText(qtTrId(u""))
        self.statLabel.setText(qtTrId(u""))
        self.tierLabel.setText(qtTrId(u""))
        self.cSPageLabel.setText(qtTrId(u""))
        self.label.setText(qtTrId(u""))
    # retranslateUi

