from models import CSAbility,Language,CSAbilityLang,CSFocusLang
from PySide6.QtWidgets import QWidget,QGridLayout, QLineEdit, QFormLayout, QTextEdit,QLabel,QListWidget,QTreeWidgetItem,QTreeWidget,QTabWidget,QListView
from PySide6.QtWidgets import QPushButton,QComboBox,QSpinBox

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
        self.addItem(prefix + self.tr(' or ').join([ab_lang.name for ab_lang in ab_lang_list]))
        #for ab_lang in ab_lang_list:
        #    self.addItem(ab_lang.name)
        # self.addItem(newListItem)
        # self.setItemWidget(newListItem, FocusAbilitiesWidgetItem(ab_lang_list,prefix))


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
        listWidget = FocusAbilityListWidget(self._focuslang)
        gridlayout.addWidget(listWidget,4,0)
        # listWidget = QListWidget()
        # current_grid_row = 3
        # for rank in range(1,7):
        #     current_grid_row = self.display_abilities(rank,listWidget,current_grid_row)
        # gridlayout.addWidget(listWidget,3,0)
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
