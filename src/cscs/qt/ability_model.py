from PySide6.QtCore import QAbstractListModel,QModelIndex,Qt,QSize,QEnum,QByteArray
from enum import IntEnum
from models import CSAbilityLang


@QEnum
class AbilityRole(IntEnum):
    NameRole = Qt.ItemDataRole.DisplayRole
    ToolTipRole = Qt.ItemDataRole.ToolTipRole
    CSPageRole = Qt.ItemDataRole.UserRole
    StatRole = Qt.ItemDataRole.UserRole + 1
    TierRole = Qt.ItemDataRole.UserRole + 2
    DescriptionRole = Qt.ItemDataRole.UserRole + 3

class AbilityListModel(QAbstractListModel):
    def __init__(self, session, abilities:list[CSAbilityLang]=None, parent=None):
        super().__init__(parent)
        self.session = session
        self._abilities = abilities or []

    def rowCount(self, parent) -> int:
        return len(self._abilities)

    # https://doc.qt.io/qtforpython-6/PySide6/QtCore/QAbstractItemModel.html#PySide6.QtCore.QAbstractItemModel.data
    def data(self, index:QModelIndex, role:int):
        row = index.row()
        if row < self.rowCount():
            ab_lang = self._abilities[row]
            if role == AbilityRole.NameRole:
                return ab_lang.name
            if role == AbilityRole.ToolTipRole:
                description = ab_lang.description
                if len(description) < 200:
                    return description
                else:
                    return description[0:200]
            if role == AbilityRole.CSPageRole:
                return ab_lang.cs_page
            if role == AbilityRole.StatRole:
                return ab_lang.stat
            if role == AbilityRole.TierRole:
                return ab_lang.tier
            if role == AbilityRole.DescriptionRole:
                return ab_lang.description
        return None

    def roleNames(self):
        roles = super().roleNames()
        roles[AbilityRole.NameRole] = QByteArray(b"ab_name")
        roles[AbilityRole.ToolTipRole] = QByteArray(b"description_tooltip")
        roles[AbilityRole.CSPageRole] = QByteArray(b"cs_page")
        roles[AbilityRole.StatRole] = QByteArray(b"stat")
        roles[AbilityRole.TierRole] = QByteArray(b"tier")
        roles[AbilityRole.DescriptionRole] = QByteArray(b"description")
        return roles

