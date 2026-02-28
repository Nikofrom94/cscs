from PySide6.QtWidgets import QWidget,QLineEdit,QFormLayout,QGridLayout,QPushButton,QTextEdit,QLabel
from models import CSAbilityLang
from qt.common_ui import TierComboBox



class CSAbilityTabWidget(QWidget):
    def __init__(self, abilitylang:CSAbilityLang,parent=None):
        super().__init__(parent)
        self._abilitylang:CSAbilityLang = abilitylang
        self.lang_id = self._abilitylang.lang_id
        self._ability = self._abilitylang.ability
        self.has_changed = False
        gridlayout = QGridLayout()
        self.nameEdit = QLineEdit(self._abilitylang.name)
        self.statEdit = QLineEdit(self._abilitylang.stat)
        self.cs_pageEdit = QLineEdit(self._ability.cs_page)
        self.descriptionEdit = QTextEdit(self._abilitylang.description)

        form = QFormLayout()
        form.addRow(self.tr("Name"), self.nameEdit)
        form.addRow(self.tr("stat"), self.statEdit)
        form.addRow(self.tr("cs_page"), self.cs_pageEdit)
        gridlayout.addLayout(form,0,0)
        gridlayout.addWidget(QLabel(self.tr("Description")),1,0)
        gridlayout.addWidget(self.descriptionEdit,2,0)


        self.saveButton = QPushButton(self.tr("Save"))
        self.saveButton.setEnabled(False)
        gridlayout.addWidget(self.saveButton,4,0)

        self.setLayout(gridlayout)


    def enable_save(self):
        self.saveButton.setEnabled(True)

    def disable_save(self):
        self.saveButton.setEnabled(False)
