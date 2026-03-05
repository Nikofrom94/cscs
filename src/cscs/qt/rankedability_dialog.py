
from PySide6 import QtWidgets

from qt.dialog_selectuniquerankedability import Ui_SelectUniqueRankedAbilityDialog

from cscs_db import Session,CSCGDB
from qt.rankedability_model import RankedAbility

class RankedUniqueAbilityDialog(QtWidgets.QDialog):
    def __init__(self,session:Session,parent=None):
        super().__init__(parent)
        self.session = session
        self.ui = Ui_SelectUniqueRankedAbilityDialog()
        self.ui.setupUi(self)
        abilities = CSCGDB.get_abilities(self.session)
        self.ui.abilityListWidget.load_abilities(abilities)
        self.ui.buttonBox.accepted.connect(self.accept)
        self.ui.buttonBox.rejected.connect(self.reject)

    @property
    def ranked_ab(self):
        selected_items = self.ui.abilityListWidget.selectedItems()
        if selected_items is None:
            return None
        return RankedAbility(selected_items[0],self.ui.rankSpinBox.value())

