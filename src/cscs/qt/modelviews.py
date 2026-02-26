from PySide6.QtWidgets import QWidget,QStyledItemDelegate,QListWidgetItem,QLabel,QPushButton
from PySide6.QtCore import QAbstractListModel,QModelIndex,Qt

class FocusAbilitiesItem(QWidget):
    def __init__(self,rank:int,ab_lang_list):
        self.rank = rank
        self.ab_lang_list=  ab_lang_list
        if len(self.ab_lang_list) == 1:
            self.prefix = self.tr(f"Rank {rank}: ")
        else:
            self.prefix_to_choose = self.tr(f"Rank {rank}: Choose between ")

class FocusAbilitiesWidgetItem(QListWidgetItem):
    def __init__(self,focusabilitiesitem:FocusAbilitiesItem,parent=None):
        super(FocusAbilitiesWidgetItem, self).__init__(parent)
        self._ab_lang_list = focusabilitiesitem.ab_lang_list
        # self.textQVBoxLayout = QVBoxLayout()
        self.prefixLabel = QLabel(focusabilitiesitem.prefix)
        self.textQVBoxLayout.addWidget(self.prefixLabel)
        self.buttons = []
        num_ab = 0
        for ab_lang in self._ab_lang_list:
            num_ab += 1
            print(ab_lang.name)
            nameButton = QPushButton(ab_lang.name)
            nameButton.flat = True
            nameButton.setToolTip(ab_lang.description)
            #nameButton.clicked.connect(self.show_ab(ab_lang))
            self.buttons.append(nameButton)
            self.textQVBoxLayout.addWidget(nameButton)
            if num_ab < len(self._ab_lang_list):
                self.textQVBoxLayout.addWidget(QLabel(self.tr("or")))
        self.setLayout(self.textQVBoxLayout)

    def show_ab(self,ab_lang):
        print(ab_lang.name)
        print(f"parent type {type(self.parent)}")

class FocusAbilityListItemDelegate(QStyledItemDelegate):
    def __init__(self, parent=None):
        super().__init__(parent)

    def createEditor(self, parentView,option,index:QModelIndex)-> QWidget:
        abililities:FocusAbilitiesItem = parentView.data(index,Qt.DisplayRole)
        return FocusAbilitiesWidgetItem(abililities)


class FocusAbilityListModel(QAbstractListModel):
    def __init__(self, abilities, parent=None):
        super().__init__(parent)
        self._abilities = abilities or []

    def rowCount(self, parent) -> int:
        return len(self._abilities)

    # https://doc.qt.io/qtforpython-6/PySide6/QtCore/QAbstractItemModel.html#PySide6.QtCore.QAbstractItemModel.data
    def data(self, index:QModelIndex, role:int):
        if not index.isValid():
            return None

        if index.row() >= len(self._abilities):
            return None

        if role != Qt.DisplayRole:
            return None
        return self._abilities[index.row()]

