from PySide6.QtCore import QAbstractListModel,QModelIndex,Qt,QSize,QEnum,QByteArray
from enum import IntEnum
from models import CSAbilityLang


class RankedAbility:
    rank:int
    def __init__(self,ab_lang:CSAbilityLang, rank:int):
        self._ab_lang = ab_lang
        self.rank = rank

    @property
    def ability(self):
        return self._ab_lang.ability

    @property
    def name(self) -> str:
        return self._ab_lang.name

    @name.setter
    def name(self,value:str) -> None:
        self._ab_lang.name = value

    @property
    def cs_page(self) -> str:
        return self._ab_lang.cs_page

    @cs_page.setter
    def cs_page(self,value:str) -> None:
        self._ab_lang.cs_page = value

    @property
    def stat(self) -> str:
        return self._ab_lang.stat

    @stat.setter
    def stat(self,value:str) -> None:
        self._ab_lang.stat = value

    @property
    def tier(self) -> str:
        return self._ab_lang.tier

    @tier.setter
    def tier(self,value:str) -> None:
        self._ab_lang.tier = value

    @property
    def description(self) -> str:
        return self._ab_lang.description

    @description.setter
    def description(self,value:str) -> None:
        self._ab_lang.description = value

    def get_shortdescription(self) -> str:
        description:str = self.description
        if description is not None:
            if len(description) < 200:
                return description
            else:
                return description[:200]
        else:
            return None

    def __repr__(self) -> str:
        return f"{self.name}"

class RankedAbilityToChoose:
    def __init__(self, ab_lang_list:list[CSAbilityLang], rank:int):
        self.ab_list:list[RankedAbility] = [RankedAbility(ab_lang,rank) for ab_lang in ab_lang_list]
        self.rank = rank

    def ab_count(self) -> int:
        return len(self.ab_list)

    def add_ab(self, ab_lang:CSAbilityLang):
        self.ab_list.append(ab_lang)

    def get_ab(self, position:int):
        if position < 0 and position >= self.ab_count():
            return None
        else:
            return self.ab_list[position]

    def set_ab(self, position:int, ab_lang:CSAbilityLang) -> bool:
        if position  < 0 and position > self.ab_count():
            return False
        else:
            self.ab_list[position] = ab_lang

    def __repr__(self) -> str:
        ab_names = [ f"{ab}" for ab in self.ab_list ]
        return f"Rank {self.rank} : {' or '.join(ab_names)}"

@QEnum
class RankedAbilityRole(IntEnum):
    NameRole = Qt.ItemDataRole.DisplayRole
    ToolTipRole = Qt.ItemDataRole.ToolTipRole
    CSPageRole = Qt.ItemDataRole.UserRole
    StatRole = Qt.ItemDataRole.UserRole + 1
    TierRole = Qt.ItemDataRole.UserRole + 2
    DescriptionRole = Qt.ItemDataRole.UserRole + 3
    RankRole = Qt.ItemDataRole.UserRole + 4


class RankedAbilityModel(QAbstractListModel):
    def __init__(self, session, rankedabilities:list[RankedAbility]=None, parent=None):
        super().__init__(parent)
        self.session = session
        self._rankedabilities = rankedabilities or []

    def rowCount(self, parent) -> int:
        return len(self._rankedabilities)

    # https://doc.qt.io/qtforpython-6/PySide6/QtCore/QAbstractItemModel.html#PySide6.QtCore.QAbstractItemModel.data
    def data(self, index:QModelIndex, role:int):
        row = index.row()
        if row < self.rowCount():
            ranked_ab = self._rankedabilities[row]
            print(ranked_ab)
            if role == RankedAbilityRole.NameRole:
                return ranked_ab.name
            if role == RankedAbilityRole.ToolTipRole:
                description = ranked_ab.description
                if len(description) < 200:
                    return description
                else:
                    return description[0:200]
            if role == RankedAbilityRole.CSPageRole:
                return ranked_ab.cs_page
            if role == RankedAbilityRole.StatRole:
                return ranked_ab.stat
            if role == RankedAbilityRole.TierRole:
                return ranked_ab.tier
            if role == RankedAbilityRole.DescriptionRole:
                return ranked_ab.description
            if role == RankedAbilityRole.RankRole:
                return ranked_ab.rank
        return None

    def roleNames(self):
        roles = super().roleNames()
        roles[RankedAbilityRole.NameRole] = QByteArray(b"ab_name")
        roles[RankedAbilityRole.ToolTipRole] = QByteArray(b"description_tooltip")
        roles[RankedAbilityRole.CSPageRole] = QByteArray(b"cs_page")
        roles[RankedAbilityRole.StatRole] = QByteArray(b"stat")
        roles[RankedAbilityRole.TierRole] = QByteArray(b"tier")
        roles[RankedAbilityRole.DescriptionRole] = QByteArray(b"description")
        roles[RankedAbilityRole.RankRole] = QByteArray(b"rank")
        return roles



class RankedAbilityToChooseModel(QAbstractListModel):
    def __init__(self, session, rankedabilitytochoose:list[RankedAbilityToChoose]=None, parent=None):
        super().__init__(parent)
        self.session = session
        self._rankedabilitytochoose = rankedabilitytochoose or []

    def rowCount(self, parent=None) -> int:
        return len(self._rankedabilitytochoose)

    # https://doc.qt.io/qtforpython-6/PySide6/QtCore/QAbstractItemModel.html#PySide6.QtCore.QAbstractItemModel.data
    def data(self, index:QModelIndex, role:int):
        row = index.row()
        if row < self.rowCount():
            ranked_ab_to_choose = self._rankedabilitytochoose[row]
            if role == RankedAbilityRole.NameRole:
                return ranked_ab_to_choose
        return None

    # def roleNames(self):
    #     roles = super().roleNames()
    #     roles[RankedAbilityRole.NameRole] = QByteArray(b"ab_name")
    #     roles[RankedAbilityRole.ToolTipRole] = QByteArray(b"description_tooltip")
    #     roles[RankedAbilityRole.CSPageRole] = QByteArray(b"cs_page")
    #     roles[RankedAbilityRole.StatRole] = QByteArray(b"stat")
    #     roles[RankedAbilityRole.TierRole] = QByteArray(b"tier")
    #     roles[RankedAbilityRole.DescriptionRole] = QByteArray(b"description")
    #     roles[RankedAbilityRole.RankRole] = QByteArray(b"rank")
    #     return roles


