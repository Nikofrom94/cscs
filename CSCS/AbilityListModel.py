from PySide6.QtCore import QAbstractListModel,QModelIndex,Qt,QSize,QEnum
from enum import IntEnum
from models import CSAbilityLan


class AbilityListModel(QAbstractListModel):
    @QEnum
    class AbilityRole(IntEnum):
        NameRole = Qt.ItemDataRole.DisplayRole
        ToolTipRole = Qt.ItemDataRole.ToolTipRole
        CSPageRole = Qt.ItemDataRole.UserRole
        StatRole = Qt.ItemDataRole.UserRole + 1
        TierRole = Qt.ItemDataRole.UserRole + 2
        DescriptionRole = Qt.ItemDataRole.UserRole + 3

    def __init__(self, parent_item,session, abilities:list[CSAbilityLan]=None, parent=None):
        super().__init__(parent)
        self._parent_item
        self.session = session
        self._abilities = abilities or []

    def rowCount(self, parent) -> int:
        return len(self._abilities)

    # https://doc.qt.io/qtforpython-6/PySide6/QtCore/QAbstractItemModel.html#PySide6.QtCore.QAbstractItemModel.data
    def data(self, index:QModelIndex, role:int):
        row = index.row()
        if row < self.rowCount():
            ab_lang = self._abilities[row]
            if role == AbilityListModel.AbilityRole.NameRole:
                return ab_lang.name
            if role == AbilityListModel.AbilityRole.ToolTipRole:
                description = ab_lang.description
                if len(description) < 200:
                    return description
                else:
                    return description[0:200]
            if role == AbilityListModel.AbilityRole.CSPageRole:
                return ab_lang.cs_page
            if role == AbilityListModel.AbilityRole.StatRole:
                return ab_lang.stat
            if role == AbilityListModel.AbilityRole.TierRole:
                return ab_lang.tier
            if role == AbilityListModel.AbilityRole.DescriptionRole:
                return ab_lang.description
        return None

    def roleNames(self):
        roles = super().roleNames()
        roles[AbilityListModel.AbilityRole.NameRole] = QByteArray(b"ab_name")
        roles[AbilityListModel.AbilityRole.ToolTipRole] = QByteArray(b"description_tooltip")
        roles[AbilityListModel.AbilityRole.CSPageRole] = QByteArray(b"cs_page")
        roles[AbilityListModel.AbilityRole.StatRole] = QByteArray(b"stat")
        roles[AbilityListModel.AbilityRole.TierRole] = QByteArray(b"tier")
        roles[AbilityListModel.AbilityRole.DescriptionRole] = QByteArray(b"description")
        return roles

