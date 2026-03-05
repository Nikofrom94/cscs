from PySide6.QtCore import Qt
from PySide6.QtWidgets import (QDialog, QLabel, QTextEdit, QLineEdit,
                               QDialogButtonBox, QGridLayout,
                               QVBoxLayout,QListWidget,QListWidgetItem,
                               QPushButton)

import settings
from cscs_db import CSCGDB
from models import CSAbilityLang
from qt.common_ui import AbilityLangRank

class CSAbilityListWidgetItem(QListWidgetItem):
    def __init__(self,ab_lang:CSAbilityLang,parent=None):
        super().__init__(parent)
        self._ab_lang = ab_lang
        self.setText(self._ab_lang.name)

class CSAbilityRankDialog(Qdialog):
    def __init__(self, session, ab_lang_list:list[AbilityLangRank],parent=None):
        super().__init__(parent)

        gridLayout = QGridLayout()

        self.filterEdit = QLineEdit(self.tr(""))
        self.filterEdit.textChanged.connect(self.filter_abilities)

        gridLayout.addWidget(self.filterEdit, 0,0)

        self.leftList = QListWidget()
        for ab_lang in session.get_abilities():
            self.leftList.addItem(CSAbilityListWidgetItem(ab_lang))
        gridLayout.addWidget(self.leftList,1,0)

        middleLayout = QVBoxLayout()
        self.removeButton = QPushButton("<<")
        self.addButton = QPushButton(">>")
        middleLayout.addWidget(self.removeButton)
        middleLayout.addWidget(self.addButton)
        gridLayout.addWidget(middleLayout,1,1)

        self.rightList = QListWidget()

        self.setLayout(gridLayout)

    def filter_abilities(self, text):
            pass
