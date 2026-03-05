from PySide6.QtWidgets import (QAbstractItemDelegate,QApplication,QPushButton,QStyle,
            QStyleOptionButton,QStyledItemDelegate,QListWidget,QListWidgetItem)
from PySide6.QtCore import Qt,QSize

from qt.rankedability_model import RankedAbility


class RankedUniqueAbilityItem(QListWidgetItem):
    def __init__(self, ranked_ab:RankedAbility, label:str):
        self.ranked_ab = ranked_ab
        super().__init__(label)
        self.setToolTip(self.ranked_ab.get_shortdescription())

class RankedUniqueAbilityListWidget(QListWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

    def load_rankedabilities(self, ranked_ab_list:list[RankedAbility]):
        # clear all items in the list
        self.clear()
        # add new list
        for ab in ranked_ab_list:
            rank = ab.rank
            name = ab.name
            self.addItem(RankedUniqueAbilityItem(ab), label=self.tr("Rank: {rank} : {name}"))



class RankedAbilityListItemDelegate(QAbstractItemDelegate):
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
            rankedability_item = index.data(Qt.DisplayRole)
            # display rank as a prefix
            rank = rankedability_item.rank
            prefix = self.tr(f"Rank {rank} : ")
                # self.textQVBoxLayout = QVBoxLayout()
            style.drawItemText(
                painter,
                option.rect,
                option.displayAlignment,
                option.palette,
                True,
                prefix)
            # move after prefix
            option.rect.moveRight(
                option.rect.right()
                + painter.fontMetrics().size(Qt.TextSingleLine,prefix).width()
                )
            # display flat button showing up the ability name
            nameButton = QPushButton(rankedability_item.name)
            nameButton.flat = True
            nameButton.setToolTip(rankedability_item.get_shortdescription())
            optionButton = QStyleOptionButton()
            optionButton.initFrom(nameButton)
            style.drawControl(
                QStyle.ControlElement.CE_PushButton,
                optionButton,
                painter)
            painter.restore()
        else:
            QStyledItemDelegate.paint(painter, option, index)

    def sizeHint(self, option ,index):
        return QSize(self.lineWidth,self.lineHeigth)

class RankedAbilityToChooseDelegate(QStyledItemDelegate):
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
            rankedabilitytochoose_item = index.data(Qt.DisplayRole)
            print(f"Painting {rankedabilitytochoose_item}")
            # display rank as a prefix
            rank = rankedabilitytochoose_item.rank
            prefix = self.tr(f"Rank {rank} : ")
                # self.textQVBoxLayout = QVBoxLayout()
            style.drawItemText(
                painter,
                option.rect,
                option.displayAlignment,
                option.palette,
                True,
                prefix)
            # move after prefix
            option.rect.moveRight(
                option.rect.right()
                + painter.fontMetrics().size(Qt.TextSingleLine,prefix).width()
                )
            # for each ability to choose, display flat button showing up the ability name
            # index_ab = 1
            # for ab_lang in rankedabilitytochoose_item.ab_list:
            #     nameButton = QPushButton(ab_lang.name)
            #     nameButton.flat = True
            #     nameButton.setToolTip(ab_lang.get_shortdescription())
            #     optionButton = QStyleOptionButton()
            #     optionButton.initFrom(nameButton)
            #     style.drawControl(
            #         QStyle.ControlElement.CE_PushButton,
            #         optionButton,
            #         painter)
            #     if index_ab < rankedabilitytochoose_item.ab_count():
            #         # move after previous item
            #         option.rect.moveRight(
            #             option.rect.right()
            #             + optionButton.width()
            #             )
            #         # display separator
            #         separator = self.tr(" or ")
            #             # self.textQVBoxLayout = QVBoxLayout()
            #         style.drawItemText(
            #             painter,
            #             option.rect,
            #             option.displayAlignment,
            #             option.palette,
            #             True,
            #             separator)
            #         # move after separator
            #         option.rect.moveRight(
            #             option.rect.right()
            #             + painter.fontMetrics().size(Qt.TextSingleLine,separator).width()
            #             )
            painter.restore()
        else:
            QStyledItemDelegate.paint(painter, option, index)

    def sizeHint(self, option ,index):
        return QSize(self.lineWidth,self.lineHeigth)