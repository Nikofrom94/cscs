import sys,sqlite3
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QGridLayout, QLCDNumber, QSizePolicy, QLayoutItem, QLabel
from PySide6.QtWidgets import QTreeWidget,QTreeWidgetItem
from PySide6.QtWidgets import QTabWidget,QFormLayout,QLineEdit,QTextEdit
from PySide6.QtWidgets import QSplitter

CSCSG_DBPATH = '/home/niko/Documents/jdr/CypherSystem/Cypher-SRD-FR/CSCG/cscgsite/db.sqlite3'

class CSItem:
    def __init__(self,row):
        self.id:str = row['id']
        self.name:str = row['name']

    @property
    def label(self) -> str:
        return self.name

class CSAbility(CSItem):
    """Wrapper for an Ability"""
    def __init__(self,row):
        super().__init__(row)
        self.name_en:str = row['name_en']
        self.description:str = row['description']
        self.cs_page:str = row["cs_page"]
        self.stat:str = row['stat']
        self.tier:str = row['tier']

    @property
    def label(self):
        return self.name_en

class CSFocus(CSItem):
    """wrapper for a Focus"""
    def __init__(self,row):
        super().__init__(row)
        self.name_en = row['name_en']


class CSAbilityTab(QWidget):
    def __init__(self, ability:CSAbility):
        super().__init__()
        self._ability = ability
        gridlayout = QGridLayout()
        self.name = QLineEdit(self._ability.name)
        self.description = QTextEdit(self._ability.description)
        self.stat = QLineEdit(self._ability.stat)
        self.cs_page = QLineEdit(self._ability.cs_page)

        form = QFormLayout()
        form.addRow(self.tr("&Name"), self.name)
        form.addRow(self.tr("&Stat"), self.stat)
        form.addRow(self.tr("&cs_page"), self.cs_page)
        gridlayout.addLayout(form,0,0)
        gridlayout.addWidget(QLabel(self.tr("D&escription")),1,0)
        gridlayout.addWidget(self.description,2,0)
        self.setLayout(gridlayout)


class CSCGDB():
    def __init__(self, db_path):
        self.con = sqlite3.connect(db_path)
        self.con.row_factory = sqlite3.Row

    def get_csitems(self, table_name, wrapper):
        query = f"SELECT * FROM {table_name} ORDER BY name_en"
        cursor = self.con.execute(query)
        items = []
        for row in cursor:
            items.append(wrapper(row))
        return items

    def get_abilities(self):
        """get all abilities (id, name, name_en)"""
        return self.get_csitems('cscg_ability', CSAbility)
    
    def get_foci(self):
        return self.get_csitems('cscg_focus', CSFocus)

    def get_types(self):
        return self.get_csitems('cscg_focus', CSItem)



class CSBrowserItem(QTreeWidgetItem):
    """Wrapper for browsing Abilities, Foci, Types & al
        add a signal to show the item in a tab"""
    def __init__(self, item):
        super(CSBrowserItem,self).__init__(None, [item.label])
        self._item = item
        self.label = item.label
        if type(self._item) == CSAbility:
            self.targetClass = CSAbilityTab



class CSBrowser(QTreeWidget):
    def __init__(self, target_tab):
        super(CSBrowser,self).__init__(None)
        self._target_tab = target_tab
        csdb = CSCGDB(CSCSG_DBPATH)
        self.setColumnCount(1)
        self.insertTopLevelItems(0, [QTreeWidgetItem(None,[self.tr("Abilities")])])
        self.insertTopLevelItems(1, [QTreeWidgetItem(None,[self.tr("Types")])])
        self.insertTopLevelItems(2, [QTreeWidgetItem(None,[self.tr("Foci")])])
        root_ab = self.topLevelItem(0)
        for item in csdb.get_abilities():
            node = CSBrowserItem(item)
            root_ab.addChild(node)
        root_types = self.topLevelItem(1)
        for item in csdb.get_types():
            node = CSBrowserItem(item)
            root_types.addChild(node)
        root_foci = self.topLevelItem(2)
        for item in csdb.get_foci():
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
