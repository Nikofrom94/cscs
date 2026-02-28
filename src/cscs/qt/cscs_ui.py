from models import CSAbility,Language,CSAbilityLang,CSFocusLang,CSCharacterTypeLang,CSDescriptorLang
from PySide6.QtWidgets import QWidget,QGridLayout, QLineEdit, QFormLayout, QTextEdit,QLabel,QListWidget,QTreeWidgetItem,QTreeWidget,QTabWidget,QListView
from PySide6.QtWidgets import QPushButton,QComboBox,QSpinBox
from qt.modelviews import FocusAbilityListModel,FocusAbilitiesItem,FocusAbilityListItemDelegate

from qt.ability_ui import CSAbilityTabWidget
from qt.focus_ui import CSFocusTabWidget
from qt.charactertype_ui import CSCharacterTypeTabWidget
from qt.descriptor_ui import CSDescriptorTabWidget

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

    def fill_browser(self, target_tab, session):
        self._target_tab = target_tab
        # fill with ability list
        self.root_ab = self.topLevelItem(CSBrowserWidget.AB_ROW_INDEX)
        for item in session.get_abilities(2):
            node = CSBrowserWidgetItem(item)
            self.root_ab.addChild(node)
        # fill with character type list
        self.root_types = self.topLevelItem(CSBrowserWidget.TY_ROW_INDEX)
        for item in session.get_types(2):
            node = CSBrowserWidgetItem(item)
            self.root_types.addChild(node)
        # fill with descriptor list
        self.root_descriptors = self.topLevelItem(CSBrowserWidget.DE_ROW_INDEX)
        for item in session.get_descriptors(2):
             node = CSBrowserWidgetItem(item)
             self.root_descriptors.addChild(node)
        self.itemDoubleClicked.connect(self.show_item)
        # fill with focus list
        self.root_foci = self.topLevelItem(CSBrowserWidget.FO_ROW_INDEX)
        for item in session.get_foci(2):
             node = CSBrowserWidgetItem(item)
             self.root_foci.addChild(node)
        self.itemDoubleClicked.connect(self.show_item)

    def show_item(self, item, column):
        index:int = self._target_tab.get_tab_index(item.label)
        if index >= 0 :
            self._target_tab.setCurrentIndex(index)
        else:
            item_widget = item.targetClass(item._item)
            self._target_tab.show_tab(item.label,item_widget)

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

    def close_tab(self,index):
        self.removeTab(index)

