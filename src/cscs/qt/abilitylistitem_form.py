# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AbilityListItem_form.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QPushButton, QSizePolicy,
    QWidget)

class Ui_AbilityListItemForm(object):
    def setupUi(self, AbilityListItemForm):
        if not AbilityListItemForm.objectName():
            AbilityListItemForm.setObjectName(u"AbilityListItemForm")
        AbilityListItemForm.resize(326, 32)
        AbilityListItemForm.setMinimumSize(QSize(0, 25))
        AbilityListItemForm.setBaseSize(QSize(0, 25))
        self.horizontalLayoutWidget = QWidget(AbilityListItemForm)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(-1, -1, 321, 31))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.abilityButton = QPushButton(self.horizontalLayoutWidget)
        self.abilityButton.setObjectName(u"abilityButton")
        self.abilityButton.setMinimumSize(QSize(0, 25))
        font = QFont()
        font.setUnderline(True)
        self.abilityButton.setFont(font)
        self.abilityButton.setFlat(True)

        self.horizontalLayout.addWidget(self.abilityButton)

        self.deleteButton = QPushButton(self.horizontalLayoutWidget)
        self.deleteButton.setObjectName(u"deleteButton")
        self.deleteButton.setEnabled(False)
        self.deleteButton.setMinimumSize(QSize(25, 25))
        self.deleteButton.setMaximumSize(QSize(25, 25))
        self.deleteButton.setBaseSize(QSize(25, 25))
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.EditDelete))
        self.deleteButton.setIcon(icon)

        self.horizontalLayout.addWidget(self.deleteButton)


        self.retranslateUi(AbilityListItemForm)

        QMetaObject.connectSlotsByName(AbilityListItemForm)
    # setupUi

    def retranslateUi(self, AbilityListItemForm):
        AbilityListItemForm.setWindowTitle(QCoreApplication.translate("AbilityListItemForm", u"Form", None))
        self.abilityButton.setText(QCoreApplication.translate("AbilityListItemForm", u"Ability", None))
        self.deleteButton.setText("")
    # retranslateUi

