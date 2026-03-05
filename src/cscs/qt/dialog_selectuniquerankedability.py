# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_selectuniquerankedability.ui'
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
    QHBoxLayout, QLabel, QListWidgetItem, QSizePolicy,
    QSpinBox, QWidget)

from qt.ability_widgets import AbilityListWidget

class Ui_SelectUniqueRankedAbilityDialog(object):
    def setupUi(self, SelectUniqueRankedAbilityDialog):
        if not SelectUniqueRankedAbilityDialog.objectName():
            SelectUniqueRankedAbilityDialog.setObjectName(u"SelectUniqueRankedAbilityDialog")
        SelectUniqueRankedAbilityDialog.resize(397, 404)
        self.buttonBox = QDialogButtonBox(SelectUniqueRankedAbilityDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(190, 350, 181, 32))
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.abilityListWidget = AbilityListWidget(SelectUniqueRankedAbilityDialog)
        self.abilityListWidget.setObjectName(u"abilityListWidget")
        self.abilityListWidget.setGeometry(QRect(10, 60, 361, 261))
        self.horizontalLayoutWidget = QWidget(SelectUniqueRankedAbilityDialog)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(30, 10, 160, 31))
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


        self.retranslateUi(SelectUniqueRankedAbilityDialog)
        self.buttonBox.accepted.connect(SelectUniqueRankedAbilityDialog.accept)
        self.buttonBox.rejected.connect(SelectUniqueRankedAbilityDialog.reject)

        QMetaObject.connectSlotsByName(SelectUniqueRankedAbilityDialog)
    # setupUi

    def retranslateUi(self, SelectUniqueRankedAbilityDialog):
        SelectUniqueRankedAbilityDialog.setWindowTitle(QCoreApplication.translate("SelectUniqueRankedAbilityDialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("SelectUniqueRankedAbilityDialog", u"Rank", None))
    # retranslateUi

