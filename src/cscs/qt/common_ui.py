""" Common UI classes
"""


from PySide6.QtWidgets import QComboBox
from PySide6.QtCore import Slot

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
