# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_selectrankedability.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QHBoxLayout, QLabel, QListWidget, QListWidgetItem,
    QPushButton, QSizePolicy, QSpinBox, QWidget)

class Ui_SelectRankedAbilityDialog(object):
    def setupUi(self, SelectRankedAbilityDialog):
        if not SelectRankedAbilityDialog.objectName():
            SelectRankedAbilityDialog.setObjectName(u"SelectRankedAbilityDialog")
        SelectRankedAbilityDialog.resize(574, 605)
        self.buttonBox = QDialogButtonBox(SelectRankedAbilityDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(320, 500, 181, 32))
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.abilityListWidget = QListWidget(SelectRankedAbilityDialog)
        self.abilityListWidget.setObjectName(u"abilityListWidget")
        self.abilityListWidget.setGeometry(QRect(10, 60, 201, 511))
        self.rankedAbilityListWidget = QListWidget(SelectRankedAbilityDialog)
        self.rankedAbilityListWidget.setObjectName(u"rankedAbilityListWidget")
        self.rankedAbilityListWidget.setGeometry(QRect(330, 180, 211, 251))
        self.horizontalLayoutWidget = QWidget(SelectRankedAbilityDialog)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(350, 120, 160, 31))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.rankSpinBox = QSpinBox(self.horizontalLayoutWidget)
        self.rankSpinBox.setObjectName(u"rankSpinBox")
        self.rankSpinBox.setMinimum(1)
        self.rankSpinBox.setMaximum(6)

        self.horizontalLayout.addWidget(self.rankSpinBox)

        self.addButton = QPushButton(SelectRankedAbilityDialog)
        self.addButton.setObjectName(u"addButton")
        self.addButton.setGeometry(QRect(220, 210, 94, 25))
        self.removeButton = QPushButton(SelectRankedAbilityDialog)
        self.removeButton.setObjectName(u"removeButton")
        self.removeButton.setGeometry(QRect(220, 250, 94, 25))

        self.retranslateUi(SelectRankedAbilityDialog)
        self.buttonBox.accepted.connect(SelectRankedAbilityDialog.accept)
        self.buttonBox.rejected.connect(SelectRankedAbilityDialog.reject)

        QMetaObject.connectSlotsByName(SelectRankedAbilityDialog)
    # setupUi

    def retranslateUi(self, SelectRankedAbilityDialog):
        SelectRankedAbilityDialog.setWindowTitle(QCoreApplication.translate("SelectRankedAbilityDialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("SelectRankedAbilityDialog", u"Rank", None))
        self.addButton.setText(QCoreApplication.translate("SelectRankedAbilityDialog", u">>", None))
        self.removeButton.setText(QCoreApplication.translate("SelectRankedAbilityDialog", u"<<", None))
    # retranslateUi

