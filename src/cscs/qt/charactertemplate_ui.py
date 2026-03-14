from PySide6.QtCore import Slot,QEvent
from PySide6.QtWidgets import QListWidget,QWidget,QLineEdit,QSpinBox,QFormLayout,QGridLayout,QLabel,QListView
from models import CSCharacterTemplate,CSCharacterTemplateLang,CSCharacterTemplateTypeFlavor


from qt.charactertemplate_form import Ui_ChararacterTemplateTab

from cscs_db import CSCGDB

class CSCharacterTemplateTabWidget(QWidget):
    def __init__(self, charactertemplateLang:CSCharacterTemplateLang, session, parent=None):
        super().__init__(parent)
        self.is_modified = False
        self.session = session
        self._charactertemplateLang:CSCharacterTemplateLang = charactertemplateLang
        self._charactertemplate:CSCharacterTemplate = self._charactertemplateLang.charactertemplate
        self.lang_id = self._charactertemplateLang.lang_id
        self.charactertemplatefoci = self._charactertemplate.charactertemplatefoci

        self.ui = Ui_ChararacterTemplateTab()
        self.ui.setupUi(self)

        self.ui.typeflavorListView.load(session, self._charactertemplate.charactertemplatetypeflavor)

        self.ui.nameLineEdit.setText(self._charactertemplate.name)
        self.ui.descriptionTextEdit.setText((self._charactertemplateLang.description))

        # manage signals
        self.ui.nameLineEdit.textChanged.connect(self.name_changed)
        self.ui.descriptionTextEdit.textChanged.connect(self.description_changed)
        self.ui.addTypeFlavorButton.clicked.connect(self.addTypeFlavor)
        self.ui.saveButton.clicked.connect(self.save_charactertemplate)

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

    @Slot()
    def addTypeFlavor(self):
        first_charactertype = CSCGDB.get_firsttype(self.session).charactertype
        print(f"first_charactertype : {first_charactertype}")
        newTypeFlavor = CSCharacterTemplateTypeFlavor(self._charactertemplate,first_charactertype)
        self.ui.typeflavorListView.model().addLine(newTypeFlavor)
