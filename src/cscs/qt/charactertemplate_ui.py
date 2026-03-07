from PySide6.QtCore import Slot,QEvent
from PySide6.QtWidgets import QListWidget,QWidget,QLineEdit,QSpinBox,QFormLayout,QGridLayout,QLabel,QListView
from models import CSCharacterTemplate,CSCharacterTemplateLang

from qt.rankedability_model import RankedAbilityModel,RankedAbility
from qt.rankedability_delegate import RankedAbilityListItemDelegate,RankedUniqueAbilityItem

from qt.charactertemplate_form import Ui_ChararacterTemplateTab

from cscs_db import CSCGDB

class CSCharacterTemplateTabWidget(QWidget):
    def __init__(self, charactertemplateLang:CSCharacterTemplateLang, session, parent=None):
        super().__init__(parent)
        self.is_modified = False
        self.session = session
        self._charactertemplateLang:CSCharacterTemplateLang = charactertemplateLang
        self._charactertemplate = self._charactertemplateLang.charactertemplate
        self.lang_id = self._charactertemplateLang.lang_id
        self.flavor = self._charactertemplate.flavor
        self._focus = self._charactertemplate.focus
        self._charactertype = self._charactertemplate.charactertype

        self.ui = Ui_ChararacterTemplateTab()
        self.ui.setupUi(self)
        self.load_flavors()
        self.load_types()
        self.load_foci()

        self.ui.nameLineEdit.setText(self._charactertemplate.name)
        self.ui.descriptionTextEdit.setText((self._charactertemplateLang.description))

        # manage signals
        self.ui.nameLineEdit.textChanged.connect(self.name_changed)
        self.ui.descriptionTextEdit.textChanged.connect(self.description_changed)
        self.ui.flavorComboBox.currentIndexChanged.connect(self.save_flavor)
        self.ui.focusComboBox.currentIndexChanged.connect(self.save_focus)
        self.ui.typeComboBox.currentIndexChanged.connect(self.save_type)
        self.ui.saveButton.clicked.connect(self.save_charactertemplate)

    def load_types(self):
        self.types = CSCGDB.get_types(self.session)
        for type_lang in self.types:
            self.ui.typeComboBox.addItem(type_lang.name)

    def load_flavors(self):
        self.flavors = CSCGDB.get_flavors(self.session)
        for flavor_lang in self.flavors:
            self.ui.flavorComboBox.addItem(flavor_lang.name)

    def load_foci(self):
        self.foci = CSCGDB.get_foci(self.session)
        for focus_lang in self.foci:
            self.ui.focusComboBox.addItem(focus_lang.name)

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
        self._charactertemplateLang.name = new_name
        self.set_modified(True)

    @Slot(str)
    def description_changed(self,new_description:str):
        self._charactertemplatelang.description = new_description
        self.set_modified(True)

    @Slot(int)
    def save_flavor(self,index):
        selected_flavor_lang = self.flavors[index]
        self._charactertemplate.flavor = selected_flavor_lang.flavor
        self._charactertemplate.save(self.session)
        self.set_modified(False)

    @Slot(int)
    def save_focus(self,index):
        selected_focus_lang = self.foci[index]
        self._charactertemplate.focus = selected_focus_lang.focus
        self._charactertemplate.save(self.session)
        self.set_modified(False)

    @Slot(int)
    def save_type(self,index):
        selected_type_lang = self.types[index]
        self._charactertemplate.charactertype = selected_type_lang.charactertype
        self._charactertemplate.save(self.session)
        self.set_modified(False)

    @Slot()
    def save_charactertemplate(self):
        self._charactertemplate.save(self.session)
        self.set_modified(False)

