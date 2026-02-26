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
from PySide6.QtWidgets import (QApplication, QHeaderView, QMainWindow, QMenu,
    QMenuBar, QSizePolicy, QSplitter, QStatusBar,
    QTreeWidgetItem, QWidget)

from qt.cscs_ui import (CSBrowserWidget, CSTabWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setGeometry(QRect(0, 0, 801, 551))
        self.splitter.setOrientation(Qt.Orientation.Horizontal)
        self.csItemDirectory = CSBrowserWidget(self.splitter)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.csItemDirectory.setHeaderItem(__qtreewidgetitem)
        self.csItemDirectory.setObjectName(u"csItemDirectory")
        self.csItemDirectory.setMaximumSize(QSize(300, 16777215))
        self.csItemDirectory.setBaseSize(QSize(50, 0))
        self.splitter.addWidget(self.csItemDirectory)
        self.csItemDirectory.header().setVisible(False)
        self.csItemTab = CSTabWidget(self.splitter)
        self.csItemTab.setObjectName(u"csItemTab")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.csItemTab.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.csItemTab.addTab(self.tab_2, "")
        self.splitter.addWidget(self.csItemTab)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
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
        self.csItemTab.setTabText(self.csItemTab.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.csItemTab.setTabText(self.csItemTab.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tab 2", None))
        self.menuCypher_System_Character_Sheet.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

