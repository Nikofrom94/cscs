from models import CSAbility,Language,CSAbilityLang,CSFocusLang
from PySide6.QtWidgets import QWidget,QGridLayout, QLineEdit, QFormLayout, QTextEdit,QLabel,QListWidget,QListWidgetItem
from PySide6.QtWidgets import QVBoxLayout,QPushButton

class CSAbilityView:
    def __init__(self,ability:CSAbility, language:Language):
        self._ability = ability
        
        self.name_en = ability.name

class FocusAbilitiesWidgetItem(QWidget):
    def __init__(self,ab_lang_list,prefix:str,parent=None):
        super(FocusAbilitiesWidgetItem, self).__init__(parent)
        self._ab_lang_list = ab_lang_list
        self.textQVBoxLayout = QVBoxLayout()
        self.prefixLabel = QLabel(prefix)
        self.textQVBoxLayout.addWidget(self.prefixLabel)
        print(prefix)
        self.buttons = []
        num_ab = 0
        for ab_lang in ab_lang_list:
            num_ab += 1
            print(ab_lang.name)
            nameButton = QLabel(ab_lang.name)
            # nameButton = QPushButton(ab_lang.name)
            # nameButton.flat = True
            # nameButton.setToolTip(ab_lang.description)
            # #nameButton.clicked.connect(self.show_ab(ab_lang))
            # self.buttons.append(nameButton)
            self.textQVBoxLayout.addWidget(nameButton)
            if num_ab < len(ab_lang_list):
                self.textQVBoxLayout.addWidget(QLabel(self.tr("or")))
        self.setLayout(self.textQVBoxLayout)

    def show_ab(self,ab_lang):
        print(ab_lang.name)
        print(f"parent type {type(self.parent)}")
#        print(f"parent-parent type {type(self.parent.parent)}")


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
            print(ab_lang.name)
            self.addItem(ab_lang.name.strip())
        # self.addItem(newListItem)
        # self.setItemWidget(newListItem, FocusAbilitiesWidgetItem(ab_lang_list,prefix))



class CSAbilityTab(QWidget):
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


class CSFocusTab(QWidget):
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

    # def display_abilities(self,rank:int,listWidget:QListWidget,current_grid_row:int):
    #     focusability = None
    #     if rank==1: focusability = self._focus.abilities_tier1
    #     elif rank==2: focusability = self._focus.abilities_tier2
    #     elif rank==3: focusability = self._focus.abilities_tier3
    #     elif rank==4: focusability = self._focus.abilities_tier4
    #     elif rank==5: focusability = self._focus.abilities_tier5
    #     elif rank==6: focusability = self._focus.abilities_tier6
    #     prefix = self.tr(f"Rank {rank}: ")
    #     prefix_to_choose = self.tr(f"Rank {rank}: Choose between ")
    #     if focusability is not None:
    #         for ab in focusability.abilities:
    #             ab_lang = None
    #             for locale in ab.locales:
    #                 if locale.lang_id == self.lang_id:
    #                     ab_lang = locale
    #             if ab_lang is not None:
    #                 QListWidgetItem(prefix+ab_lang.name, listWidget)
    #                 current_grid_row += 1
    #         if len(focusability.abilities_to_choose) > 0:
    #             abilities_to_choose = []
    #             for ab in focusability.abilities_to_choose:
    #                 ab_lang = None
    #                 for locale in ab.locales:
    #                     if locale.lang_id == self.lang_id:
    #                         ab_lang = locale
    #                 if ab_lang is not None:
    #                     abilities_to_choose.append(ab_lang.name)
    #             QListWidgetItem(prefix_to_choose+self.tr(" or ").join(abilities_to_choose), listWidget)
    #             current_grid_row += 1
    #     return current_grid_row

