from PySide6.QtWidgets import QListWidget,QWidget,QLineEdit,QSpinBox,QFormLayout,QGridLayout,QLabel
from models import CSFlavorLang,CSAbilityLang

class FlavorAbilityList(QListWidget):
    def __init__(self, abilities,parent=None):
        super().__init__(parent)
        for ab in abilities:
            prefix = self.tr(f"Rank {ab.rank} : ")
            self.addItem(prefix + ab.ab_lang.name)

class FlavorAbility:
    def __init__(self, ab_lang:CSAbilityLang, rank:int):
        self.rank = rank
        self.ab_lang = ab_lang

class CSFlavorTabWidget(QWidget):
    def __init__(self, flavorlang:CSFlavorLang):
        super().__init__()
        self._flavorlang:CSFlavorLang = flavorlang
        self.lang_id = self._flavorlang.lang_id
        self._flavor = self._flavorlang.flavor
        gridlayout = QGridLayout()
        self.name = QLineEdit(self._flavorlang.name)
        self.cs_page = QLineEdit(self._flavor.cs_page)

        form = QFormLayout()
        form.addRow(self.tr("&Name"), self.name)
        form.addRow(self.tr("&cs_page"), self.cs_page)
        gridlayout.addLayout(form,0,0)
        gridlayout.addWidget(QLabel(self.tr("Abilities")),3,0)
        self.abilities = []
        self.abilities += self.get_abilities(rank=1, ability_list=self._flavor.abilities_rank1)
        self.abilities += self.get_abilities(rank=2, ability_list=self._flavor.abilities_rank2)
        self.abilities += self.get_abilities(rank=3, ability_list=self._flavor.abilities_rank3)
        self.abilities += self.get_abilities(rank=4, ability_list=self._flavor.abilities_rank4)
        self.abilities += self.get_abilities(rank=5, ability_list=self._flavor.abilities_rank5)
        self.abilities += self.get_abilities(rank=6, ability_list=self._flavor.abilities_rank6)
        self.ability_list_widget = FlavorAbilityList( self.abilities )
        gridlayout.addWidget(self.ability_list_widget,4,0)
        self.setLayout(gridlayout)

    def get_abilities(self, rank:int, ability_list):
        ab_lang_list = []
        for ab in ability_list:
            for locale in ab.locales:
                if locale.lang_id == self.lang_id:
                    ab_lang_list.append(FlavorAbility(ab_lang=locale,rank=rank))
        return ab_lang_list
