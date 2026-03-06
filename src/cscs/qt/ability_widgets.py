# This Python file uses the following encoding: utf-8
from PySide6 import QtCore
from PySide6 import QtWidgets


from models import CSAbilityLang

class AbilityListWidgetItem(QtWidgets.QListWidgetItem):
    def __init__(self, ab:CSAbilityLang):
        self.item = ab
        super().__init__(ab.name)

    @property
    def name(self) -> str:
        return self.item.name

    @property
    def description(self) -> str:
        return self.item.description

    @property
    def ab_lang(self) -> CSAbilityLang:
        return self.item

    @property
    def ability(self):
        return self.item.ability

class AbilityListWidget(QtWidgets.QListWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

    def load_abilities(self,ab_list:list[CSAbilityLang]):
        self.ab_list = ab_list
        for ab in ab_list:
            self.addItem( AbilityListWidgetItem(ab) )
