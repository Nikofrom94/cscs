from enum import IntEnum
from PySide6.QtCore import QEnum

@QEnum
class AbilityRole(IntEnum):
    NameRole = Qt.ItemDataRole.DisplayRole
    ToolTipRole = Qt.ItemDataRole.ToolTipRole
    CSPageRole = Qt.ItemDataRole.UserRole
    StatRole = Qt.ItemDataRole.UserRole + 1
    TierRole = Qt.ItemDataRole.UserRole + 2
    DescriptionRole = Qt.ItemDataRole.UserRole + 3
