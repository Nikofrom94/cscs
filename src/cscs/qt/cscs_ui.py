from models import CSAbility,Language,CSAbilityLang,CSFocusLang,CSCharacterTypeLang,CSDescriptorLang,CSFlavorLang
from PySide6.QtWidgets import QWidget,QGridLayout, QLineEdit, QFormLayout, QTextEdit,QLabel,QListWidget,QTreeWidgetItem,QTreeWidget,QTabWidget,QListView,QMenu
from PySide6.QtWidgets import QPushButton,QComboBox,QSpinBox
from qt.modelviews import FocusAbilityListModel,FocusAbilitiesItem,FocusAbilityListItemDelegate
from PySide6.QtCore import Slot,QPoint, Qt

from qt.ability_ui import CSAbilityTabWidget
from qt.focus_ui import CSFocusTabWidget
from qt.charactertype_ui import CSCharacterTypeTabWidget
from qt.descriptor_ui import CSDescriptorTabWidget
from qt.flavor_ui import CSFlavorTabWidget

import settings
from cscs_db import CSCGDB

class CSAbilityView:
    def __init__(self,ability:CSAbility, language:Language):
        self._ability = ability
        self.name_en = ability.name


class CSBrowserWidgetItem(QTreeWidgetItem):
    """Wrapper for browsing Abilities, Foci, Types & al
        add a signal to show the item in a tab"""
    def __init__(self, item):
        super(CSBrowserWidgetItem,self).__init__(None, [item.name])
        self._item = item
        self.label = item.name
        if type(self._item) == CSAbilityLang:
            self.targetClass = CSAbilityTabWidget
        elif type(self._item) == CSFocusLang:
            self.targetClass = CSFocusTabWidget
        elif type(self._item) == CSCharacterTypeLang:
            self.targetClass = CSCharacterTypeTabWidget
        elif type(self._item) == CSDescriptorLang:
            self.targetClass = CSDescriptorTabWidget
        elif type(self._item) == CSFlavorLang:
            self.targetClass = CSFlavorTabWidget

    def disable(self) -> None:
        """disable the item in db"""
        print(f"del(self._item) for {self._item.name}")

class CSBrowserWidget(QTreeWidget):
    AB_ROW_INDEX = 0
    TY_ROW_INDEX = 1
    FO_ROW_INDEX = 2
    DE_ROW_INDEX = 3
    FL_ROW_INDEX = 4
    def __init__(self,parent=None):
        super(CSBrowserWidget,self).__init__(parent)
        self.setColumnCount(1)
        self.insertTopLevelItems(
            CSBrowserWidget.AB_ROW_INDEX,
            [QTreeWidgetItem(None,[self.tr("Abilities")])])
        self.insertTopLevelItems(
            CSBrowserWidget.TY_ROW_INDEX,
            [QTreeWidgetItem(None,[self.tr("Types")])])
        self.insertTopLevelItems(
            CSBrowserWidget.FO_ROW_INDEX,
            [QTreeWidgetItem(None,[self.tr("Foci")])])
        self.insertTopLevelItems(
            CSBrowserWidget.DE_ROW_INDEX,
            [QTreeWidgetItem(None,[self.tr("Descriptor")])])
        self.insertTopLevelItems(
            CSBrowserWidget.FL_ROW_INDEX,
            [QTreeWidgetItem(None,[self.tr("Flavor")])])
        # manage context ModuleNotFoundError
        self.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.customContextMenuRequested.connect(self.display_context_menu)

    def fill_browser(self, target_tab, session=None):
        self._target_tab = target_tab
        # fill with ability list
        self.root_ab = self.topLevelItem(CSBrowserWidget.AB_ROW_INDEX)
        for item in CSCGDB.get_abilities(session):
            node = CSBrowserWidgetItem(item)
            self.root_ab.addChild(node)
        # fill with character type list
        self.root_types = self.topLevelItem(CSBrowserWidget.TY_ROW_INDEX)
        for item in CSCGDB.get_types(session):
            node = CSBrowserWidgetItem(item)
            self.root_types.addChild(node)
        # fill with descriptor list
        self.root_descriptors = self.topLevelItem(CSBrowserWidget.DE_ROW_INDEX)
        for item in CSCGDB.get_descriptors(session):
             node = CSBrowserWidgetItem(item)
             self.root_descriptors.addChild(node)
        self.itemDoubleClicked.connect(self.show_item)
        # fill with focus list
        self.root_foci = self.topLevelItem(CSBrowserWidget.FO_ROW_INDEX)
        for item in CSCGDB.get_foci(session):
             node = CSBrowserWidgetItem(item)
             self.root_foci.addChild(node)
        self.itemDoubleClicked.connect(self.show_item)
        # fill with flavor list
        self.root_descriptors = self.topLevelItem(CSBrowserWidget.FL_ROW_INDEX)
        for item in CSCGDB.get_flavors(session):
             node = CSBrowserWidgetItem(item)
             self.root_descriptors.addChild(node)
        self.itemDoubleClicked.connect(self.show_item)

    def show_item(self, item, column):
        index:int = self._target_tab.get_tab_index(item.label)
        if index >= 0 :
            self._target_tab.setCurrentIndex(index)
        else:
            item_widget = item.targetClass(item._item)
            self._target_tab.show_tab(item.label,item_widget)

    @Slot(QPoint)
    def display_context_menu(self, pos):
        if self.currentItem() is None:
            return
        current_item = self.currentItem()
        if type(current_item) != CSBrowserWidgetItem:
            return

        menu = QMenu(self)
        remove_pair_action = menu.addAction(self.tr("Delete"))
        chosen_action = menu.exec(self.viewport().mapToGlobal(pos))


        if chosen_action == remove_pair_action:
            self.delete_item(current_item)

    def delete_item(self, item_to_delete:CSBrowserWidgetItem) -> None:
        """Remove the item from the list, and disable it in the DB"""
        item_to_delete.disable()
        self.removeItemWidget(item_to_delete,1)


class CSTabWidget(QTabWidget):
    def __init__(self,parent=None):
        super(CSTabWidget,self).__init__(parent)
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

    def close_tab(self,index) -> None:
        self.removeTab(index)

