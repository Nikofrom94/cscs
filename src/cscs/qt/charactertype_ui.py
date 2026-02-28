from PySide6.QtWidgets import QListWidget,QWidget,QLineEdit,QSpinBox,QFormLayout,QGridLayout,QLabel
from models import CSCharacterTypeLang,CSAbilityLang

class CharacterTypeAbilityList(QListWidget):
    def __init__(self, abilities,parent=None):
        super().__init__(parent)
        for ab in abilities:
            prefix = self.tr(f"Rank {ab.rank} : ")
            self.addItem(prefix + ab.ab_lang.name)

class CharacterTypeAbility:
    def __init__(self, ab_lang:CSAbilityLang, rank:int):
        self.rank = rank
        self.ab_lang = ab_lang

class CSCharacterTypeTabWidget(QWidget):
    def __init__(self, typelang:CSCharacterTypeLang):
        super().__init__()
        self._typelang:CSCharacterTypeLang = typelang
        self.lang_id = self._typelang.lang_id
        self._type = self._typelang.charactertype
        gridlayout = QGridLayout()
        self.name = QLineEdit(self._typelang.name)
        self.cs_page = QLineEdit(self._type.cs_page)
        self.might_start = QSpinBox()
        self.might_start.setValue(self._type.might_start)
        self.might_edge_start = QSpinBox()
        self.might_edge_start.setValue(self._type.might_edge_start)
        self.speed_start = QSpinBox()
        self.speed_start.setValue(self._type.speed_start)
        self.speed_edge_start = QSpinBox()
        self.speed_edge_start.setValue(self._type.speed_edge_start)
        self.intellect_start = QSpinBox()
        self.intellect_start.setValue(self._type.intellect_start)
        self.intellect_edge_start = QSpinBox()
        self.intellect_edge_start.setValue(self._type.intellect_edge_start)

        form = QFormLayout()
        form.addRow(self.tr("&Name"), self.name)
        form.addRow(self.tr("&cs_page"), self.cs_page)
        gridlayout.addLayout(form,0,0)
        form.addRow(self.tr("&Might"), self.might_start)
        form.addRow(self.tr("&Speed"), self.speed_start)
        form.addRow(self.tr("&Intellect"), self.intellect_start)
        gridlayout.addWidget(QLabel(self.tr("Abilities")),3,0)
        self.abilities = []
        self.abilities += self.get_abilities(rank=1, ability_list=self._type.abilities_rank1)
        self.abilities += self.get_abilities(rank=2, ability_list=self._type.abilities_rank2)
        self.abilities += self.get_abilities(rank=3, ability_list=self._type.abilities_rank3)
        self.abilities += self.get_abilities(rank=4, ability_list=self._type.abilities_rank4)
        self.abilities += self.get_abilities(rank=5, ability_list=self._type.abilities_rank5)
        self.abilities += self.get_abilities(rank=6, ability_list=self._type.abilities_rank6)
        self.ability_list_widget = CharacterTypeAbilityList( self.abilities )
        gridlayout.addWidget(self.ability_list_widget,4,0)
        self.setLayout(gridlayout)

    def get_abilities(self, rank:int, ability_list):
        ab_lang_list = []
        for ab in ability_list:
            for locale in ab.locales:
                if locale.lang_id == self.lang_id:
                    ab_lang_list.append(CharacterTypeAbility(ab_lang=locale,rank=rank))
        return ab_lang_list
