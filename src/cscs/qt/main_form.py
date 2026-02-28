# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_form.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHeaderView, QLayout,
    QMainWindow, QMenu, QMenuBar, QSizePolicy,
    QSplitter, QStatusBar, QTreeWidgetItem, QWidget)

from qt.cscs_ui import (CSBrowserWidget, CSTabWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(643, 481)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SizeConstraint.SetMinAndMaxSize)
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setOrientation(Qt.Orientation.Horizontal)
        self.mainTree = CSBrowserWidget(self.splitter)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.mainTree.setHeaderItem(__qtreewidgetitem)
        self.mainTree.setObjectName(u"mainTree")
        sizePolicy.setHeightForWidth(self.mainTree.sizePolicy().hasHeightForWidth())
        self.mainTree.setSizePolicy(sizePolicy)
        self.mainTree.setMaximumSize(QSize(300, 16777215))
        self.mainTree.setBaseSize(QSize(50, 0))
        self.splitter.addWidget(self.mainTree)
        self.mainTree.header().setVisible(False)
        self.mainTab = CSTabWidget(self.splitter)
        self.mainTab.setObjectName(u"mainTab")
        sizePolicy.setHeightForWidth(self.mainTab.sizePolicy().hasHeightForWidth())
        self.mainTab.setSizePolicy(sizePolicy)
        self.splitter.addWidget(self.mainTab)

        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 643, 22))
        self.menuCypher_System_Character_Sheet = QMenu(self.menubar)
        self.menuCypher_System_Character_Sheet.setObjectName(u"menuCypher_System_Character_Sheet")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuCypher_System_Character_Sheet.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.menuCypher_System_Character_Sheet.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

