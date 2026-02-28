from PySide6.QtWidgets import QWidget,QAbstractItemDelegate,QListWidgetItem,QLabel,QPushButton,QStyleOptionProgressBar,QApplication,QStyle,QStyledItemDelegate,QApplication,QStyleOptionButton
from PySide6.QtCore import QAbstractListModel,QModelIndex,Qt,QSize

class FocusAbilitiesItem:
    def __init__(self,rank:int,ab_lang_list):
        self.rank = rank
        self.ab_lang_list=  ab_lang_list
        if len(self.ab_lang_list) == 1:
            self.prefix = self.tr(f"Rank {rank}: ")
        else:
            self.prefix = self.tr(f"Rank {rank}: Choose between ")

    def tr(self,s):
        return s

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
        print(f"ab_lang.name:{ab_lang.name}")
        print(f"parent type {type(self.parent)}")

class FocusAbilityListItemDelegate(QAbstractItemDelegate):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.lineWidth = 500
        self.lineHeigth = 25

    def paint(self, painter, option,index):
        if index.column() == 0:
            if option.widget is not None:
                style = option.widget.style()
            else:
                style = QApplication.style()
            focusabilitiesitem = index.data(Qt.DisplayRole)
            ab_lang_list = focusabilitiesitem.ab_lang_list
                # self.textQVBoxLayout = QVBoxLayout()
            prefix = focusabilitiesitem.prefix
            style.drawItemText(
                painter,
                option.rect,
                option.displayAlignment,
                option.palette,
                True,
                prefix)
            option.rect.moveRight(
                option.rect.right()
                + painter.fontMetrics().size(Qt.TextSingleLine,prefix).width()
                )
            num_ab = 0
            buttons = []
            for ab_lang in ab_lang_list:
                num_ab += 1
                nameButton = QPushButton(ab_lang.name)
                nameButton.flat = True
                nameButton.setToolTip(ab_lang.get_shortdescription())
                optionButton = QStyleOptionButton()
                optionButton.initFrom(nameButton)
                buttons.append(nameButton)
                style.drawControl(
                    QStyle.ControlElement.CE_PushButton,
                    optionButton,
                    painter)
                break
                if num_ab < len(ab_lang_list):
                    separator = self.tr(" or ")
                    option.rect.moveRight(
                        option.rect.right()
                        + nameButton.width()
                        )
                    style.drawItemText(
                        painter, option.rect,
                        option.displayAlignment,
                        option.palette,
                        True,
                        separator
                        )
                    option.rect.moveRight(
                        option.rect.right()
                        + painter.fontMetrics().size(Qt.TextSingleLine,separator).width()
                        )
            #painter.restore()
        else:
            QStyledItemDelegate.paint(painter, option, index)

    def sizeHint(self, option ,index):
        return QSize(self.lineWidth,self.lineHeigth)

class FocusAbilityListModel(QAbstractListModel):
    def __init__(self, abilities, parent=None):
        super().__init__(parent)
        self._abilities = abilities or []

    def rowCount(self, parent) -> int:
        return len(self._abilities)

    # https://doc.qt.io/qtforpython-6/PySide6/QtCore/QAbstractItemModel.html#PySide6.QtCore.QAbstractItemModel.data
    def data(self, index:QModelIndex, role:int):
        if role == Qt.DisplayRole:
            ab = self._abilities[index.row()]

        if not index.isValid():
            return None

        if index.row() >= len(self._abilities):
            return None

        if role != Qt.DisplayRole:
            return None
        return self._abilities[index.row()]

