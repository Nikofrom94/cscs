from PySide6.QtWidgets import QListWidget,QWidget,QLineEdit,QSpinBox,QFormLayout,QGridLayout,QPushButton,QTextEdit,QLabel
from models import CSDescriptorLang
from qt.common_ui import TierComboBox

class CSDescriptorTabWidget(QWidget):
    def __init__(self, descriptorlang:CSDescriptorLang,parent=None):
        super().__init__(parent)
        self._descriptorlang:CSDescriptorLang = descriptorlang
        self.lang_id = self._descriptorlang.lang_id
        self._descriptor = self._descriptorlang.descriptor
        self.has_changed = False
        gridlayout = QGridLayout()
        self.nameEdit = QLineEdit(self._descriptorlang.name)
        self.descriptionEdit = QTextEdit(self._descriptorlang.description)
        self.cs_pageEdit = QLineEdit(self._descriptor.cs_page)

        form = QFormLayout()
        form.addRow(self.tr("Name"), self.nameEdit)
        form.addRow(self.tr("cs_page"), self.cs_pageEdit)
        gridlayout.addLayout(form,0,0)

        gridlayout.addWidget(QLabel(self.tr("Description")),1,0)
        gridlayout.addWidget(self.descriptionEdit,2,0)

        self.characteristicList = QListWidget()
        for char in self._descriptor.characteristics:
            for charLang in char.locales:
                if charLang.lang_id == self.lang_id:
                    self.characteristicList.addItem( charLang.name + " : " + charLang.description )
        gridlayout.addWidget(self.characteristicList,3,0)

        gridlayout.addWidget(QLabel(self.tr("Initial Links")),4,0)
        self.initialLinksList = QListWidget()
        link_index = 0
        for link in self._descriptor.initiallinks:
            for link_lang in link.locales:
                if link_lang.lang_id == self.lang_id:
                    link_index += 1
                    self.initialLinksList.addItem( f"{link_index} : {link_lang.description}" )
        gridlayout.addWidget(self.initialLinksList,5,0)

        self.saveButton = QPushButton(self.tr("Save"))
        self.saveButton.setEnabled(False)
        gridlayout.addWidget(self.saveButton,6,0)

        self.setLayout(gridlayout)


    def enable_save(self):
        self.saveButton.setEnabled(True)

    def disable_save(self):
        self.saveButton.setEnabled(False)
