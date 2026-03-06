from PySide6.QtCore import Slot,QEvent
from PySide6.QtWidgets import QListWidget,QWidget,QLineEdit,QSpinBox,QFormLayout,QGridLayout,QLabel,QListView
from models import CSFlavorLang,CSAbilityLang

from qt.rankedability_model import RankedAbilityModel,RankedAbility
from qt.rankedability_delegate import RankedAbilityListItemDelegate,RankedUniqueAbilityItem

from qt.flavor_tab import Ui_FlavorTab
from qt.rankedability_dialog import RankedUniqueAbilityDialog

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
    def __init__(self, flavorlang:CSFlavorLang, session, parent=None):
        super().__init__(parent)
        self.is_modified = False
        self.session = session
        self._flavorlang:CSFlavorLang = flavorlang
        self.lang_id = self._flavorlang.lang_id
        self._flavor = self._flavorlang.flavor

        self.ui = Ui_FlavorTab()
        self.ui.setupUi(self)

        self.ui.nameLineEdit.setText(self._flavorlang.name)
        self.ui.cs_pageLineEdit.setText((self._flavor.cs_page))
        self.load_abilities()

        # manage signals
        self.ui.nameLineEdit.textChanged.connect(self.name_changed)
        self.ui.cs_pageLineEdit.textChanged.connect(self.cs_page_changed)
        self.ui.addButton.clicked.connect(self.add_rankedAbility)
        self.ui.removeButton.clicked.connect(self.remove_rankedAbility)
        self.ui.saveButton.clicked.connect(self.save_flavor)


    def load_abilities(self):
        self.abilities = []
        self.ui.rankedUniqueAbilityListWidget.clear()
        self.abilities += self.get_abilities(rank=1, ability_list=self._flavor.abilities_rank1)
        self.abilities += self.get_abilities(rank=2, ability_list=self._flavor.abilities_rank2)
        self.abilities += self.get_abilities(rank=3, ability_list=self._flavor.abilities_rank3)
        self.abilities += self.get_abilities(rank=4, ability_list=self._flavor.abilities_rank4)
        self.abilities += self.get_abilities(rank=5, ability_list=self._flavor.abilities_rank5)
        self.abilities += self.get_abilities(rank=6, ability_list=self._flavor.abilities_rank6)
        self.ui.rankedUniqueAbilityListWidget.load_rankedabilities(self.abilities)


    def get_abilities(self, rank:int, ability_list):
        """Get abilities locales from the tier list"""
        ab_lang_list = []
        for ab in ability_list:
            for locale in ab.locales:
                if locale.lang_id == self.lang_id:
                    #ab_lang_list.append(FlavorAbility(ab_lang=locale,rank=rank))
                    ab_lang_list.append(RankedAbility(ab_lang=locale,rank=rank))
        return sorted(ab_lang_list, key=lambda ab : ab.name)

    def set_modified(self, is_modified:bool):
        self.is_modified = is_modified
        self.ui.saveButton.setEnabled(is_modified)

    @Slot(str)
    def name_changed(self,new_name:str):
        self._flavorlang.name = new_name
        self.set_modified(True)

    @Slot(str)
    def cs_page_changed(self,new_cs_page:str):
        self._flavor.cs_page = new_cs_page
        self.set_modified(True)

    @Slot()
    def add_rankedAbility(self) -> RankedAbility:
        dialog = RankedUniqueAbilityDialog(self.session)
        if (dialog.exec()):
            ranked_ab = dialog.ranked_ab
            self._flavor.add_ability(self.session, ranked_ab.ability, ranked_ab.rank)
            self.load_abilities()

    @Slot()
    def remove_rankedAbility(self) -> None:
        selected_items = self.ui.rankedUniqueAbilityListWidget.selectedItems()
        if selected_items is not None and len(selected_items) == 1:
            ranked_ab = selected_items[0]
            self._flavor.remove_ability(self.session, ranked_ab.ability, ranked_ab.rank)
            self.load_abilities()

    @Slot()
    def save_flavor(self):
        self._flavor.save(self.session)
        self.set_modified(False)


class CSFlavorTabWidget2(QWidget):
    def __init__(self, flavorlang:CSFlavorLang,session, parent=None):
        super().__init__(parent)
        self.session = session
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
#        self.ability_list_widget = FlavorAbilityList( self.abilities )
#        gridlayout.addWidget(self.ability_list_widget,4,0)
        rankedAbilityModel = RankedAbilityModel(rankedabilities=self.abilities,session = self.session)
        listView = QListView()
        listView.setModel(rankedAbilityModel)
        listView.setItemDelegate(RankedAbilityListItemDelegate())
        gridlayout.addWidget(listView,4,0)
        self.setLayout(gridlayout)

    def get_abilities(self, rank:int, ability_list):
        ab_lang_list = []
        for ab in ability_list:
            for locale in ab.locales:
                if locale.lang_id == self.lang_id:
                    #ab_lang_list.append(FlavorAbility(ab_lang=locale,rank=rank))
                    ab_lang_list.append(RankedAbility(ab_lang=locale,rank=rank))
        return ab_lang_list

