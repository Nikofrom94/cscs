import sys
from cscs_db import CSCGDB
from models import CSAbilityLang, CSFocusLang
from views import CSAbilityTab,CSFocusTab
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout
from PySide6.QtWidgets import QTreeWidget,QTreeWidgetItem
from PySide6.QtWidgets import QTabWidget
from PySide6.QtWidgets import QSplitter
import gettext
# localization variables
appname = 'cscs'
localedir = './locale'
en_i18n = gettext.translation(appname, localedir, fallback=True, languages=['en-us'])
fr_i18n = gettext.translation(appname, localedir, fallback=True, languages=['fr-fr'])

# alias gettext
fr_i18n.install()
_=fr_i18n.gettext

CSCSG_DBPATH = '/home/niko/Documents/jdr/CypherSystem/Cypher-SRD-FR/CSCG/cscgsite/db.sqlite3'
CSQT_DBPATH = './db.sqlite3'

class CSBrowserItem(QTreeWidgetItem):
    """Wrapper for browsing Abilities, Foci, Types & al
        add a signal to show the item in a tab"""
    def __init__(self, item):
        super(CSBrowserItem,self).__init__(None, [item.name])
        self._item = item
        self.label = item.name
        if type(self._item) == CSAbilityLang:
            self.targetClass = CSAbilityTab
        elif type(self._item) == CSFocusLang:
            self.targetClass = CSFocusTab

class CSBrowser(QTreeWidget):
    def __init__(self, target_tab):
        super(CSBrowser,self).__init__(None)
        self._target_tab = target_tab
        csdb = CSCGDB(CSQT_DBPATH)
        self.setColumnCount(1)
        self.insertTopLevelItems(0, [QTreeWidgetItem(None,[_("Abilities")])])
        self.insertTopLevelItems(1, [QTreeWidgetItem(None,[_("Types")])])
        self.insertTopLevelItems(2, [QTreeWidgetItem(None,[_("Foci")])])
        root_ab = self.topLevelItem(0)
        for item in csdb.get_abilities(2):
            node = CSBrowserItem(item)
            root_ab.addChild(node)
        # root_types = self.topLevelItem(1)
        # for item in csdb.get_types():
        #     node = CSBrowserItem(item)
        #     root_types.addChild(node)
        root_foci = self.topLevelItem(2)
        for item in csdb.get_foci(2):
             node = CSBrowserItem(item)
             root_foci.addChild(node)
        self.itemDoubleClicked.connect(self.show_item)

    def show_item(self, item, column):
        index:int = self._target_tab.get_tab_index(item.label)
        if index >= 0 :
            self._target_tab.setCurrentIndex(index)
        else:
            item_widget = item.targetClass(item._item)
            self._target_tab.show_tab(item.label,item_widget)

class CSTab(QTabWidget):
    def __init__(self):
        super(CSTab,self).__init__()
        self.setTabsClosable(True)
        self.tabCloseRequested.connect(self.close_tab)

    def get_tab_index(self, label:str) -> int:
        for index in range(self.count()):
            if self.tabText(index) == label:
                return index
        return -1

    def show_tab(self,label:str, content:QWidget) -> None:
        # check for a tab with same name to show it
        for index in range(self.count()):
            if self.tabText(index) == label:
                self.setCurrentIndex(index)
                return
        # no tab with that name/label : add it
        index = self.addTab(content, label)
        self.setCurrentIndex(index)

    def close_tab(self,index):
        self.removeTab(index)

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cypher System Character Sheet V0.1")
        self.setWindowIcon(QIcon("icons/yes.png"))
        self.resize(500, 500)
        self.setStyleSheet("background: #333333; border: 10px solid #333333;")

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

            # l, c, h, w
        tab_grid = CSTab()
        browse_grid = QGridLayout()
        browse_tree = CSBrowser(tab_grid)
        browse_grid.addWidget(browse_tree,0,0)

        # main_grid = QGridLayout()
        #main_grid.addWidget(browse_tree, 0, 0)
        #main_grid.addWidget(tab_grid, 0,1)

        #central_widget.setLayout(main_grid)

        splitter = QSplitter()
        splitter.addWidget(browse_tree)
        splitter.addWidget(tab_grid)
        mainlayout = QGridLayout()
        mainlayout.addWidget(splitter)

        central_widget.setLayout(mainlayout)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    myWindow = MyWindow()
    myWindow.show()

    sys.exit(app.exec())
