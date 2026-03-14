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
    QHBoxLayout, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QSpacerItem,
    QTextEdit, QWidget)

from qt.charactertemplatetypeflavorview import CharacterTemplateTypeFlavorView

class Ui_ChararacterTemplateTab(object):
    def setupUi(self, ChararacterTemplateTab):
        if not ChararacterTemplateTab.objectName():
            ChararacterTemplateTab.setObjectName(u"ChararacterTemplateTab")
        ChararacterTemplateTab.resize(561, 562)
        self.gridLayout_2 = QGridLayout(ChararacterTemplateTab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.saveButton = QPushButton(ChararacterTemplateTab)
        self.saveButton.setObjectName(u"saveButton")

        self.horizontalLayout.addWidget(self.saveButton)


        self.gridLayout_2.addLayout(self.horizontalLayout, 8, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(ChararacterTemplateTab)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.addFocusButton = QPushButton(ChararacterTemplateTab)
        self.addFocusButton.setObjectName(u"addFocusButton")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.ListAdd))
        self.addFocusButton.setIcon(icon)

        self.horizontalLayout_3.addWidget(self.addFocusButton)


        self.gridLayout_2.addLayout(self.horizontalLayout_3, 6, 0, 1, 1)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.nameLabel = QLabel(ChararacterTemplateTab)
        self.nameLabel.setObjectName(u"nameLabel")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.nameLabel)

        self.nameLineEdit = QLineEdit(ChararacterTemplateTab)
        self.nameLineEdit.setObjectName(u"nameLineEdit")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.nameLineEdit)

        self.settingLabel = QLabel(ChararacterTemplateTab)
        self.settingLabel.setObjectName(u"settingLabel")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.settingLabel)

        self.settingComboBox = QComboBox(ChararacterTemplateTab)
        self.settingComboBox.setObjectName(u"settingComboBox")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.settingComboBox)


        self.gridLayout_2.addLayout(self.formLayout, 0, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(ChararacterTemplateTab)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.addTypeFlavorButton = QPushButton(ChararacterTemplateTab)
        self.addTypeFlavorButton.setObjectName(u"addTypeFlavorButton")
        self.addTypeFlavorButton.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.addTypeFlavorButton)


        self.gridLayout_2.addLayout(self.horizontalLayout_2, 4, 0, 1, 1)

        self.label = QLabel(ChararacterTemplateTab)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 2, 0, 1, 1)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")

        self.gridLayout_2.addLayout(self.formLayout_2, 1, 0, 1, 1)

        self.descriptionTextEdit = QTextEdit(ChararacterTemplateTab)
        self.descriptionTextEdit.setObjectName(u"descriptionTextEdit")

        self.gridLayout_2.addWidget(self.descriptionTextEdit, 3, 0, 1, 1)

        self.fociList = QListWidget(ChararacterTemplateTab)
        self.fociList.setObjectName(u"fociList")

        self.gridLayout_2.addWidget(self.fociList, 7, 0, 1, 1)

        self.typeflavorListView = CharacterTemplateTypeFlavorView(ChararacterTemplateTab)
        self.typeflavorListView.setObjectName(u"typeflavorListView")

        self.gridLayout_2.addWidget(self.typeflavorListView, 5, 0, 1, 1)


        self.retranslateUi(ChararacterTemplateTab)

        QMetaObject.connectSlotsByName(ChararacterTemplateTab)
    # setupUi

    def retranslateUi(self, ChararacterTemplateTab):
        ChararacterTemplateTab.setWindowTitle(QCoreApplication.translate("ChararacterTemplateTab", u"Form", None))
        self.saveButton.setText(QCoreApplication.translate("ChararacterTemplateTab", u"Save", None))
        self.label_3.setText(QCoreApplication.translate("ChararacterTemplateTab", u"Foci", None))
        self.addFocusButton.setText(QCoreApplication.translate("ChararacterTemplateTab", u"Add", None))
        self.nameLabel.setText(QCoreApplication.translate("ChararacterTemplateTab", u"Name", None))
        self.settingLabel.setText(QCoreApplication.translate("ChararacterTemplateTab", u"Setting", None))
        self.label_2.setText(QCoreApplication.translate("ChararacterTemplateTab", u"Types and Flavors", None))
        self.addTypeFlavorButton.setText(QCoreApplication.translate("ChararacterTemplateTab", u"Add", None))
        self.label.setText(QCoreApplication.translate("ChararacterTemplateTab", u"Description", None))
    # retranslateUi

