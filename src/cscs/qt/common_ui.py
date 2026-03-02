""" Common UI classes
"""


from PySide6.QtWidgets import QComboBox
from PySide6.QtCore import Slot, Qt
from PySide6.QtCore import QAbstractTableModel

from models import CSAbilityLang

class TierComboBox(QComboBox):
    def __init__(self,parent=None,value=None):
        super().__init__(parent)
        self.TIERS = [
            ("L", self.tr("Low")),
            ("M", self.tr("Medium")),
            ("H", self.tr("High"))
        ]
        for key, label in self.TIERS:
            self.addItem(label,key)
        self.activated[int].connect(self.tier_changed)

    @Slot(int)
    def tier_changed(self, index):
        self.parentWidget().set_tier(self.TIERS[index][0])

class AbilityLangRank:
    def __init__(self, ab_lang:CSAbilityLang, rank:int):
        self.ab_lang = ab_lang
        self.rank = rank

class AbilityLangRankTableModel(QAbstractTableModel):
    def __init__(self, ab_list:list[AbilityLangRank], parent=None):
        super().__init__(parent)
        self._ab_list = ab_list

    def rowCount(self, parent=None):
        return len(self._ab_list)

    def columnCount(self, parent=None):
        return 2

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        if not index.isValid():
            return None

        if role == Qt.ItemDataRole.DisplayRole:
            ab_lang_rank = self._ab_list[index.row()]
            column = index.column()
            if column == 0:
                return ab_lang_rank.rank
            elif column == 1:
                return ab_lang_rank.ab_lang
            else:
                return None
        return None

