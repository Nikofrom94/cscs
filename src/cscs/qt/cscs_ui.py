from models import CSAbility,Language,CSAbilityLang,CSFocusLang
from PySide6.QtWidgets import QWidget,QGridLayout, QLineEdit, QFormLayout, QTextEdit,QLabel,QListWidget,QListWidgetItem,QTreeWidgetItem,QTreeWidget,QTabWidget,QListView
from PySide6.QtWidgets import QVBoxLayout,QPushButton
from qt.modelviews import FocusAbilityListModel,FocusAbilitiesItem,FocusAbilityListItemDelegate

class CSAbilityView:
    def __init__(self,ability:CSAbility, language:Language):
        self._ability = ability
        self.name_en = ability.name


class FocusAbilityListWidget(QListWidget):
    def __init__(self,focus_lang:CSFocusLang,parent=None):
        super(FocusAbilityListWidget,self).__init__(parent)
        self._focus_lang:CSAbilityLang = focus_lang
        self.lang_id = self._focus_lang.lang_id
        self._focus = self._focus_lang.focus
        for rank in range(1,7):
            if rank==1: focusability = self._focus.abilities_tier1
            elif rank==2: focusability = self._focus.abilities_tier2
            elif rank==3: focusability = self._focus.abilities_tier3
            elif rank==4: focusability = self._focus.abilities_tier4
            elif rank==5: focusability = self._focus.abilities_tier5
            elif rank==6: focusability = self._focus.abilities_tier6
            prefix = self.tr(f"Rank {rank}: ")
            prefix_to_choose = self.tr(f"Rank {rank}: Choose between ")
            if focusability is not None:
                for ab in focusability.abilities:
                    ab_lang = None
                    for locale in ab.locales:
                        if locale.lang_id == self.lang_id:
                            ab_lang = locale
                    if ab_lang is not None:
                        self.addAbilities([ab_lang],prefix)
                if len(focusability.abilities_to_choose) > 0:
                    abilities_to_choose = []
                    for ab in focusability.abilities_to_choose:
                        ab_lang = None
                        for locale in ab.locales:
                            if locale.lang_id == self.lang_id:
                                ab_lang = locale
                        if ab_lang is not None:
                            abilities_to_choose.append(ab_lang)
                    self.addAbilities(abilities_to_choose,prefix_to_choose)

    def addAbilities(self, ab_lang_list,prefix):
        #newListItem = QListWidgetItem(self)
        for ab_lang in ab_lang_list:
            self.addItem(ab_lang.name)
        # self.addItem(newListItem)
        # self.setItemWidget(newListItem, FocusAbilitiesWidgetItem(ab_lang_list,prefix))



class CSAbilityTabWidget(QWidget):
    def __init__(self, abilitylang:CSAbilityLang):
        super().__init__()
        self._abilitylang:CSAbilityLang = abilitylang
        self._ability = self._abilitylang.ability
        gridlayout = QGridLayout()
        self.name = QLineEdit(self._abilitylang.name)
        self.description = QTextEdit(self._abilitylang.description)
        self.stat = QLineEdit(self._abilitylang.stat)
        self.cs_page = QLineEdit(self._ability.cs_page)
        self.tier = QLineEdit(self._ability.tier)

        form = QFormLayout()
        form.addRow(self.tr("&Name"), self.name)
        form.addRow(self.tr("&Stat"), self.stat)
        form.addRow(self.tr("&Tier"), self.tier)
        form.addRow(self.tr("&cs_page"), self.cs_page)
        gridlayout.addLayout(form,0,0)
        gridlayout.addWidget(QLabel(self.tr("Description")),1,0)
        gridlayout.addWidget(self.description,2,0)

        self.setLayout(gridlayout)


class CSFocusTabWidget2(QWidget):
    def __init__(self, focuslang:CSFocusLang):
        super().__init__()
        self._focuslang:CSAbilityLang = focuslang
        self.lang_id = self._focuslang.lang_id
        self._focus = self._focuslang.focus
        gridlayout = QGridLayout()
        self.name = QLineEdit(self._focuslang.name)
        self.description = QTextEdit(self._focuslang.description)
        self.cs_page = QLineEdit(self._focus.cs_page)

        form = QFormLayout()
        form.addRow(self.tr("&Name"), self.name)
        form.addRow(self.tr("&cs_page"), self.cs_page)
        gridlayout.addLayout(form,0,0)
        gridlayout.addWidget(QLabel(self.tr("Description")),1,0)
        gridlayout.addWidget(self.description,2,0)
        gridlayout.addWidget(QLabel(self.tr("Abilities")),3,0)
        listWidget = FocusAbilityListWidget(self._focuslang)
        gridlayout.addWidget(listWidget,3,0)
        # listWidget = QListWidget()
        # current_grid_row = 3
        # for rank in range(1,7):
        #     current_grid_row = self.display_abilities(rank,listWidget,current_grid_row)
        # gridlayout.addWidget(listWidget,3,0)
        self.setLayout(gridlayout)

class CSFocusTabWidget(QWidget):
    def __init__(self, focuslang:CSFocusLang):
        super().__init__()
        self._focuslang:CSAbilityLang = focuslang
        self.lang_id = self._focuslang.lang_id
        self._focus = self._focuslang.focus
        gridlayout = QGridLayout()
        self.name = QLineEdit(self._focuslang.name)
        self.description = QTextEdit(self._focuslang.description)
        self.cs_page = QLineEdit(self._focus.cs_page)

        form = QFormLayout()
        form.addRow(self.tr("&Name"), self.name)
        form.addRow(self.tr("&cs_page"), self.cs_page)
        gridlayout.addLayout(form,0,0)
        gridlayout.addWidget(QLabel(self.tr("Description")),1,0)
        gridlayout.addWidget(self.description,2,0)
        gridlayout.addWidget(QLabel(self.tr("Abilities")),3,0)
        focusabilitiesModel = FocusAbilityListModel(abilities=self.get_focusabilities())
        listView = QListView()
        listView.setModel(focusabilitiesModel)
        listView.setItemDelegate(FocusAbilityListItemDelegate())
        gridlayout.addWidget(listView,4,0)
        # listWidget = QListWidget()
        # current_grid_row = 3
        # for rank in range(1,7):
        #     current_grid_row = self.display_abilities(rank,listWidget,current_grid_row)
        # gridlayout.addWidget(listWidget,3,0)
        self.setLayout(gridlayout)


    def get_focusabilities(self):
        focus_abilities = []
        for rank in range(1,7):
            if rank==1: focusability = self._focus.abilities_tier1
            elif rank==2: focusability = self._focus.abilities_tier2
            elif rank==3: focusability = self._focus.abilities_tier3
            elif rank==4: focusability = self._focus.abilities_tier4
            elif rank==5: focusability = self._focus.abilities_tier5
            elif rank==6: focusability = self._focus.abilities_tier6
            if focusability is not None:
                for ab in focusability.abilities:
                    ab_lang = None
                    for locale in ab.locales:
                        if locale.lang_id == self.lang_id:
                            ab_lang = locale
                    if ab_lang is not None:
                        focus_abilities.append(FocusAbilitiesItem(rank,[ab_lang]))
                if len(focusability.abilities_to_choose) > 0:
                    abilities_to_choose = []
                    for ab in focusability.abilities_to_choose:
                        ab_lang = None
                        for locale in ab.locales:
                            if locale.lang_id == self.lang_id:
                                ab_lang = locale
                        if ab_lang is not None:
                            abilities_to_choose.append(ab_lang)
                    focus_abilities.append(FocusAbilitiesItem(rank,abilities_to_choose))
        return focus_abilities

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

class CSBrowserWidget(QTreeWidget):
    AB_ROW_INDEX = 0
    TY_ROW_INDEX = 1
    FO_ROW_INDEX = 2
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

    def fill_browser(self, target_tab, session):
        self._target_tab = target_tab
        self.root_ab = self.topLevelItem(CSBrowserWidget.AB_ROW_INDEX)
        for item in session.get_abilities(2):
            node = CSBrowserWidgetItem(item)
            self.root_ab.addChild(node)
        # root_types = self.topLevelItem(1)
        # for item in csdb.get_types():
        #     node = CSBrowserWidgetItem(item)
        #     root_types.addChild(node)
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

