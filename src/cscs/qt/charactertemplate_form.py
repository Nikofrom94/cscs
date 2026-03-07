# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'charactertemplate_form.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QTextEdit, QWidget)

class Ui_ChararacterTemplateTab(object):
    def setupUi(self, ChararacterTemplateTab):
        if not ChararacterTemplateTab.objectName():
            ChararacterTemplateTab.setObjectName(u"ChararacterTemplateTab")
        ChararacterTemplateTab.resize(499, 425)
        self.gridLayout_2 = QGridLayout(ChararacterTemplateTab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.saveButton = QPushButton(ChararacterTemplateTab)
        self.saveButton.setObjectName(u"saveButton")

        self.horizontalLayout.addWidget(self.saveButton)


        self.gridLayout_2.addLayout(self.horizontalLayout, 5, 0, 1, 1)

        self.label = QLabel(ChararacterTemplateTab)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 2, 0, 1, 1)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.nameLabel = QLabel(ChararacterTemplateTab)
        self.nameLabel.setObjectName(u"nameLabel")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.nameLabel)

        self.nameLineEdit = QLineEdit(ChararacterTemplateTab)
        self.nameLineEdit.setObjectName(u"nameLineEdit")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.nameLineEdit)

        self.genreLabel = QLabel(ChararacterTemplateTab)
        self.genreLabel.setObjectName(u"genreLabel")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.genreLabel)

        self.genreLineEdit = QLineEdit(ChararacterTemplateTab)
        self.genreLineEdit.setObjectName(u"genreLineEdit")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.genreLineEdit)


        self.gridLayout_2.addLayout(self.formLayout, 0, 0, 1, 1)

        self.descriptionTextEdit = QTextEdit(ChararacterTemplateTab)
        self.descriptionTextEdit.setObjectName(u"descriptionTextEdit")

        self.gridLayout_2.addWidget(self.descriptionTextEdit, 3, 0, 1, 1)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.typeLabel = QLabel(ChararacterTemplateTab)
        self.typeLabel.setObjectName(u"typeLabel")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.LabelRole, self.typeLabel)

        self.typeComboBox = QComboBox(ChararacterTemplateTab)
        self.typeComboBox.setObjectName(u"typeComboBox")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.FieldRole, self.typeComboBox)

        self.flavorLabel = QLabel(ChararacterTemplateTab)
        self.flavorLabel.setObjectName(u"flavorLabel")

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.LabelRole, self.flavorLabel)

        self.flavorComboBox = QComboBox(ChararacterTemplateTab)
        self.flavorComboBox.setObjectName(u"flavorComboBox")

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.FieldRole, self.flavorComboBox)

        self.focusLabel = QLabel(ChararacterTemplateTab)
        self.focusLabel.setObjectName(u"focusLabel")

        self.formLayout_2.setWidget(2, QFormLayout.ItemRole.LabelRole, self.focusLabel)

        self.focusComboBox = QComboBox(ChararacterTemplateTab)
        self.focusComboBox.setObjectName(u"focusComboBox")

        self.formLayout_2.setWidget(2, QFormLayout.ItemRole.FieldRole, self.focusComboBox)


        self.gridLayout_2.addLayout(self.formLayout_2, 1, 0, 1, 1)


        self.retranslateUi(ChararacterTemplateTab)

        QMetaObject.connectSlotsByName(ChararacterTemplateTab)
    # setupUi

    def retranslateUi(self, ChararacterTemplateTab):
        ChararacterTemplateTab.setWindowTitle(QCoreApplication.translate("ChararacterTemplateTab", u"Form", None))
        self.saveButton.setText(QCoreApplication.translate("ChararacterTemplateTab", u"PushButton", None))
        self.label.setText(QCoreApplication.translate("ChararacterTemplateTab", u"Description", None))
        self.nameLabel.setText(QCoreApplication.translate("ChararacterTemplateTab", u"Name", None))
        self.genreLabel.setText(QCoreApplication.translate("ChararacterTemplateTab", u"Genre", None))
        self.typeLabel.setText(QCoreApplication.translate("ChararacterTemplateTab", u"Type", None))
        self.flavorLabel.setText(QCoreApplication.translate("ChararacterTemplateTab", u"Flavor", None))
        self.focusLabel.setText(QCoreApplication.translate("ChararacterTemplateTab", u"Focus", None))
    # retranslateUi

