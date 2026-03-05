from PySide6.QtCore import QAbstractItemModel,QModelIndex,Qt,QSize,QEnum
from enum import IntEnum
from models import CSAbilityLang
from roles_model import AbilityRole
from cscs_db import CSCGDB, Session

class AbilityModel(QAbstractItemModel):
    _ab_lang:CSAbilityLang=None
    session:Session = None

    def __init__(self, session, ab_lang:CSAbilityLang=None, ab_id:int=None, parent=None):
        super().__init__(parent)
        self.session = session
        if ab_id is not None:
            self._ab_lang = CSCGDB.get_ability(session,ab_id)
        elif ab_lang is not None:
            self._ab_lang = ab_lang

    def rowCount(self, parent) -> int:
        if self._ab_lang is None:
            return 0
        else:
            return 1

    # https://doc.qt.io/qtforpython-6/PySide6/QtCore/QAbstractItemModel.html#PySide6.QtCore.QAbstractItemModel.data
    def data(self, index:QModelIndex, role:int):
        row = index.row()
        if row < self.rowCount():
            ab_lang = self._ab_lang
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

