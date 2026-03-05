from PySide6.QtCore import QAbstractListModel,QModelIndex,Qt,QSize,QEnum
from enum import IntEnum
from models import CSAbilityLan

from ability_model import AbilityModel

class RankedAbility:
    rank:int
    def __init__(self,ab_lang:CSAbilityLang, rank:int):
        self._ab_lang = ab_lang
        self.rank = rank

    @property
    def name(self) -> str:
        return self._ab_lang.name

    @name.setter(self,value:str) -> None:
        self._ab_lang.name = value

    @property
    def cs_page(self) -> str:
        return self._ab_lang.cs_page

    @cs_page.setter(self,value:str) -> None:
        self._ab_lang.cs_page = value

    @property
    def stat(self) -> str:
        return self._ab_lang.stat

    @stat.setter(self,value:str) -> None:
        self._ab_lang.stat = value

    @property
    def tier(self) -> str:
        return self._ab_lang.tier

    @tier.setter(self,value:str) -> None:
        self._ab_lang.tier = value

    @property
    def description(self) -> str:
        return self._ab_lang.description

    @description.setter(self,value:str) -> None:
        self._ab_lang.description = value

class RankedAbilityModel(AbilityModel):
    @QEnum
    class RankedAbilityRole(AbilityModel.AbilityRole):
        RankRole = Qt.ItemDataRole.UserRole + 4


    def __init__(self, parent_item,session, rankedabilities:list[RankedAbility]=None, parent=None):
        super().__init__(parent)
        self._rankedabilities = rankedabilities or []

    def rowCount(self, parent) -> int:
        return len(self._rankedabilities)

    # https://doc.qt.io/qtforpython-6/PySide6/QtCore/QAbstractItemModel.html#PySide6.QtCore.QAbstractItemModel.data
    def data(self, index:QModelIndex, role:int):
        parent_data = super().data(index, role)
        if parent is None :
            row = index.row()
            if row < self.rowCount():
                ranked_ab = self._rankedabilities[row]
                if role == RankedAbilityModel.RankedAbilityRole.RankRole:
                    return ranked_ab.rank
        return None

    def roleNames(self):
        roles = super().roleNames()
        roles[RankedAbilityModel.RankedAbilityRole.RankRole] = QByteArray(b"rank")
        return roles
