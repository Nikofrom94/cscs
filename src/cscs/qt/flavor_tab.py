# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'flavor_tab.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QGridLayout, QHBoxLayout,
    QLabel, QLayout, QLineEdit, QListWidgetItem,
    QPushButton, QSizePolicy, QSpacerItem, QWidget)

from qt.rankedability_delegate import RankedUniqueAbilityListWidget

class Ui_FlavorTab(object):
    def setupUi(self, FlavorTab):
        if not FlavorTab.objectName():
            FlavorTab.setObjectName(u"FlavorTab")
        FlavorTab.resize(585, 536)
        self.gridLayout_2 = QGridLayout(FlavorTab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(9, -1, -1, -1)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.saveButton = QPushButton(FlavorTab)
        self.saveButton.setObjectName(u"saveButton")
        self.saveButton.setEnabled(False)

        self.horizontalLayout.addWidget(self.saveButton)


        self.gridLayout_2.addLayout(self.horizontalLayout, 6, 0, 1, 1)

        self.rankedUniqueAbilityListWidget = RankedUniqueAbilityListWidget(FlavorTab)
        self.rankedUniqueAbilityListWidget.setObjectName(u"rankedUniqueAbilityListWidget")

        self.gridLayout_2.addWidget(self.rankedUniqueAbilityListWidget, 4, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 1, 1, 1)

        self.addButton = QPushButton(FlavorTab)
        self.addButton.setObjectName(u"addButton")
        self.addButton.setBaseSize(QSize(0, 0))

        self.gridLayout.addWidget(self.addButton, 0, 2, 1, 1)

        self.removeButton = QPushButton(FlavorTab)
        self.removeButton.setObjectName(u"removeButton")

        self.gridLayout.addWidget(self.removeButton, 0, 3, 1, 1)

        self.label = QLabel(FlavorTab)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 3, 0, 1, 1)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetMaximumSize)
        self.nameLabel = QLabel(FlavorTab)
        self.nameLabel.setObjectName(u"nameLabel")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.LabelRole, self.nameLabel)

        self.nameLineEdit = QLineEdit(FlavorTab)
        self.nameLineEdit.setObjectName(u"nameLineEdit")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.FieldRole, self.nameLineEdit)

        self.cs_pageLabel = QLabel(FlavorTab)
        self.cs_pageLabel.setObjectName(u"cs_pageLabel")

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.LabelRole, self.cs_pageLabel)

        self.cs_pageLineEdit = QLineEdit(FlavorTab)
        self.cs_pageLineEdit.setObjectName(u"cs_pageLineEdit")

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.FieldRole, self.cs_pageLineEdit)


        self.gridLayout_2.addLayout(self.formLayout_2, 0, 0, 1, 1)

        self.gridLayout_2.setRowMinimumHeight(0, 25)

        self.retranslateUi(FlavorTab)

        QMetaObject.connectSlotsByName(FlavorTab)
    # setupUi

    def retranslateUi(self, FlavorTab):
        FlavorTab.setWindowTitle(QCoreApplication.translate("FlavorTab", u"Form", None))
        self.saveButton.setText(QCoreApplication.translate("FlavorTab", u"Save", None))
        self.addButton.setText(QCoreApplication.translate("FlavorTab", u"Add", None))
        self.removeButton.setText(QCoreApplication.translate("FlavorTab", u"Remove", None))
        self.label.setText(QCoreApplication.translate("FlavorTab", u"Abilities", None))
        self.nameLabel.setText(QCoreApplication.translate("FlavorTab", u"Name", None))
        self.cs_pageLabel.setText(QCoreApplication.translate("FlavorTab", u"CS Page", None))
    # retranslateUi

