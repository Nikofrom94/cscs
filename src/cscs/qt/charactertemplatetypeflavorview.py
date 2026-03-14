# This Python file uses the following encoding: utf-8
from PySide6.QtWidgets import (QTableView, QStyledItemDelegate, QComboBox,QStyleOptionViewItem,
    QWidget,QPushButton,QStyleOptionComboBox,QStyle,QStyleOption,QStyleOptionButton,QApplication)
from PySide6.QtCore import Qt,QCoreApplication,QAbstractTableModel,QModelIndex,QEvent
from PySide6.QtGui import QIcon

from cscs_db import CSCGDB
from models import CSCharacterTemplateTypeFlavor,CSCharacterTypeLang,CSFlavorLang

class TypeFlavorItem():
    def __init__(self,session,charactertype_lang:CSCharacterTypeLang,flavor_lang:CSFlavorLang=None):
        self.session = session
        self.charactertype_lang = charactertype_lang
        self.flavor_lang = flavor_lang


    def __repr__(self):
        return f"TypeFlavorItem : {self.charactertype_lang}/{self.flavor_lang}"

class TypeFlavorComboBoxDelegate(QStyledItemDelegate):
    def __init__(self, session,parent=None):
        super(TypeFlavorComboBoxDelegate,self).__init__(parent)
        self.session = session
        self.charactertype_lang_list = []
        self.typenames = []
        self.flavornames = []
        for charactertype_lang in CSCGDB.get_types(session):
            self.charactertype_lang_list.append(charactertype_lang)
            self.typenames.append(charactertype_lang.name)
        self.flavor_lang_list = []
        for flavor_lang in CSCGDB.get_flavors(session):
            self.flavor_lang_list.append(flavor_lang)
            self.flavornames.append(flavor_lang.name)

    def createEditor(self, parent:QWidget, option:QStyleOptionViewItem, index:QModelIndex):
        cell_data = index.data()
        print(f"create editor for index ({index.row()} x {index.column()})")
        print(f"  |- cell_data : {cell_data}")
        if index.column() == 0:
            print("create editor for column 0")
            editor = QComboBox(parent)
            for char_type_lang in self.charactertype_lang_list:
                editor.addItem(char_type_lang.name,char_type_lang)
            if cell_data is not None:
                editor.setCurrentIndex(0)
            else:
                editor.setCurrentIndex(0)
            editor.currentIndexChanged.connect(lambda: self.commitData.emit(editor))
            return editor
        if index.column() == 1:
            print("create editor for column 1")
            editor = QComboBox(parent)
            editor.addItem(None)
            for flavor_lang in self.flavor_lang_list:
                editor.addItem(flavor_lang.name,flavor_lang)
            if cell_data is not None:
                editor.setCurrentIndex(self.flavornames.index(cell_data))
            else:
                editor.setCurrentIndex(0)
            editor.currentIndexChanged.connect(lambda: self.commitData.emit(editor))
            return editor
        return None

    def setEditorData(self,editor:QWidget, index:QModelIndex):
        """Set data for the editor related to the data refered with the index in the model"""
        cell_data = index.data()
        print(f"setEditorData cell_data {cell_data} for index ({index.row()} x {index.column()})")
        if cell_data is None:
            return
        if index.column() == 0:
            editor.setCurrentIndex( self.typenames.index(cell_data) )
            #editor.setValue(cell_data.name)
        elif index.column() == 1:
            editor.setCurrentIndex( self.flavornames.index(cell_data) )
            #editor.setValue(cell_data.name)

    def updateEditorGeometry(self, editor, option, index):
        editor.setGeometry(option.rect)

    def setModelData(self,editor,model,index):
        """Set the data for the model """
        print(f"setModelData for index ({index.row()} x {index.column()})")
        editor_data = editor.currentData()
        model.setData(index, editor_data)

class DeleteButtonDelegate(QStyledItemDelegate):
    def __init__(self,parent=None):
        super(DeleteButtonDelegate,self).__init__(parent)

    def paint(self, painter, option, index):
        style = option.widget.style()
        size = min(option.rect.width(),option.rect.height())
        button_option = QStyleOptionButton()
        button_option.rect = option.rect
        button_option.rect.setWidth(size)
        button_option.rect.setHeight(size)
        button_option.rect.moveCenter(option.rect.center())
        button_option.state = option.state
        button_option.icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.EditDelete))
        button_option.iconSize.setWidth(size*0.7)
        button_option.iconSize.setHeight(size*0.7)

        style.drawControl(QStyle.CE_PushButton,button_option,painter)

    def editorEvent(self,event:QEvent, model, option:QStyleOptionViewItem, index:QModelIndex):
        if index.column() == 2:
            if event.type() == QEvent.Type.MouseButtonPress or event.type() == QEvent.Type.MouseButtonDblClick:
                model.removeRow(index.row())
                return True
        return False

class TypeFlavorListModel(QAbstractTableModel):
    def __init__(self,session, typeflavor_list:list[CSCharacterTemplateTypeFlavor]):
        super().__init__()
        self.session = session
        self.typeflavor_list = []
        for typeflavor in typeflavor_list:
            self.typeflavor_list.append(TypeFlavorItem(self.session,typeflavor))

    def rowCount(self, parent=QModelIndex()) -> int:
        return len(self.typeflavor_list)

    def columnCount(self, parent=QModelIndex()) -> int:
        return 3

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid():
            return None
        row = index.row()
        if role in (Qt.DisplayRole, Qt.EditRole):
            if row < self.rowCount():
                flavortype = self.typeflavor_list[row]
            if index.column() == 0:
                return flavortype.charactertype_lang
            if index.column() == 1:
                return flavortype.flavor_lang
            # if index.column() == 2:
            #     return flavortype.deletestate
        return None

    def flags(self, index):
        if not index.isValid():
            return Qt.ItemIsEnabled
        if index.column() == 2:
            return Qt.ItemIsEnabled
        return Qt.ItemIsSelectable | Qt.ItemIsEditable | Qt.ItemIsEnabled

    def setData(self, index, value, role=Qt.EditRole):
        print(f"setData for index ({index.row()} x {index.column()})")
        print(f" -> value : {value}")
        if index.isValid() and role == Qt.EditRole:
            flavortype = self.typeflavor_list[index.row()]
            print(f" -> flavortype : {flavortype}")
            if index.column() == 0:
                flavortype.charactertype = value.charactertype
            if index.column() == 1:
                flavortype.flavor = value.flavor

    def insertRows(self, row:int, count:int):
        #https://doc.qt.io/qtforpython-6/PySide6/QtCore/QAbstractItemModel.html#PySide6.QtCore.QAbstractItemModel.insertRows
        self.beginInsertRows(QModelIndex(),row,row+count-1)
        for i in range(count):
            self.typeflavor_list.insert(row+i, CSCharacterTemplateTypeFlavor())
        self.endInsertRows()

    def addLine(self, newTypeFlavor):
        position = len(self.typeflavor_list)-1
        self.beginInsertRows(QModelIndex(),position,position)
        self.typeflavor_list.insert(position, TypeFlavorItem(self.session,newTypeFlavor))
        self.endInsertRows()

    def removeRow(self, indexRow, parent=None):
        if 0 <= indexRow < len(self.typeflavor_list):
            self.beginRemoveRows(parent or QModelIndex(), indexRow, indexRow)
            self.typeflavor_list.pop(indexRow)
            self.endRemoveRows()
            return True
        return False

class CharacterTemplateTypeFlavorView(QTableView):
    def __init__(self, parent=None):
        super().__init__(parent)

    def load(self,session, typeflavor_list:list[CSCharacterTemplateTypeFlavor]):
        self.session = session
        self.typeflavor_list = typeflavor_list
        self.setModel(TypeFlavorListModel(session,typeflavor_list))
        self.setItemDelegateForColumn(0,TypeFlavorComboBoxDelegate(session))
        self.setItemDelegateForColumn(1,TypeFlavorComboBoxDelegate(session))
        self.setItemDelegateForColumn(2,DeleteButtonDelegate())
        self.horizontalHeader().hide()


