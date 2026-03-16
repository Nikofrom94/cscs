# This Python file uses the following encoding: utf-8
from PySide6.QtWidgets import (QTableView, QStyledItemDelegate, QComboBox,QStyleOptionViewItem,
    QWidget,QPushButton,QStyleOptionComboBox,QStyle,QStyleOption,QStyleOptionButton,QApplication)
from PySide6.QtCore import Qt,QCoreApplication,QAbstractTableModel,QModelIndex,QEvent,QSize
from PySide6.QtGui import QIcon
from sqlalchemy import select
from cscs_db import CSCGDB
from models import CSCharacterTemplateTypeFlavor,CSCharacterTypeLang,CSFlavorLang,CSCharacterTemplate
from settings import CSCSSettings

class CharacterTypeLangComboBoxDelegate(QStyledItemDelegate):
    """Delegate for CSCharacterTypeLang wit a ComboBox"""
    def __init__(self, session,parent=None):
        super(CharacterTypeLangComboBoxDelegate,self).__init__(parent)
        self.session = session
        self.charactertype_lang_list = []
        for charactertype_lang in CSCGDB.get_types(session):
            self.charactertype_lang_list.append(charactertype_lang)

    def displayText(self,value, locale):
        return value.name

    def createEditor(self, parent:QWidget, option:QStyleOptionViewItem, index:QModelIndex):
        cell_data = index.data()
        editor = QComboBox(parent)
        for char_type_lang in self.charactertype_lang_list:
            editor.addItem(char_type_lang.name,char_type_lang)
        editor.setCurrentIndex(0)
        editor.currentIndexChanged.connect(lambda: self.commitData.emit(editor))
        return editor

    def setEditorData(self,editor:QWidget, index:QModelIndex):
        """Set data for the editor related to the data refered with the index in the model"""
        cell_data = index.data()
        if cell_data is None:
            return
        editor.setCurrentIndex( self.charactertype_lang_list.index(cell_data) )
        #editor.setValue(cell_data.name)


    def updateEditorGeometry(self, editor, option, index):
        editor.setGeometry(option.rect)

    def setModelData(self,editor,model,index):
        """Set the data for the model """
        editor_data = editor.currentData()
        model.setData(index, editor_data)

class FlavorLangComboBoxDelegate(QStyledItemDelegate):
    def __init__(self, session,parent=None):
        super(FlavorLangComboBoxDelegate,self).__init__(parent)
        self.session = session
        self.flavor_lang_list = []
        for flavor_lang in CSCGDB.get_flavors(session):
            self.flavor_lang_list.append(flavor_lang)

    def displayText(self,value, locale):
        if value is not None:
            return value.name
        else:
            return None

    def createEditor(self, parent:QWidget, option:QStyleOptionViewItem, index:QModelIndex):
        cell_data = index.data()
        editor = QComboBox(parent)
        editor.addItem("",None)
        for flavor_lang in self.flavor_lang_list:
            editor.addItem(flavor_lang.name,flavor_lang)
        if cell_data is not None:
            editor.setCurrentIndex(self.flavor_lang_list.index(cell_data))
        else:
            editor.setCurrentIndex(0)
        editor.currentIndexChanged.connect(lambda: self.commitData.emit(editor))
        return editor

    def setEditorData(self,editor:QWidget, index:QModelIndex):
        """Set data for the editor related to the data refered with the index in the model"""
        cell_data = index.data()
        if cell_data is None:
            return
        editor.setCurrentIndex( self.flavor_lang_list.index(cell_data) )
        #editor.setValue(cell_data.name)

    def updateEditorGeometry(self, editor, option, index):
        editor.setGeometry(option.rect)

    def setModelData(self,editor,model,index):
        """Set the data for the model """
        editor_data = editor.currentData()
        model.setData(index, editor_data)


class DeleteButtonDelegate(QStyledItemDelegate):
    """Small delete button to remove the current line for the model"""
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
        self.buttonsize = button_option.rect.size()

    def sizeHint(self,option,index):
        return self.buttonsize

    def editorEvent(self,event:QEvent, model, option:QStyleOptionViewItem, index:QModelIndex):
        if index.column() == 2:
            if event.type() == QEvent.Type.MouseButtonPress or event.type() == QEvent.Type.MouseButtonDblClick:
                model.removeRow(index.row())
                return True
        return False

class TypeFlavorListModel(QAbstractTableModel):
    def __init__(self,session, typeflavor_list:list[CSCharacterTemplateTypeFlavor], charactertemplate:CSCharacterTemplate):
        super().__init__()
        self.session = session
        self.charactertemplate = charactertemplate
        self.typeflavor_list = typeflavor_list
        self.typeflavor_lang_list = []
        for typeflavor in self.typeflavor_list:
            charactertype_lang = session.scalars(select(CSCharacterTypeLang).where(CSCharacterTypeLang.charactertype==typeflavor.charactertype).where(CSCharacterTypeLang.lang_id==CSCSSettings.getLangID())).first()
            if typeflavor.flavor is not None:
                flavor_lang = session.scalars(select(CSFlavorLang).where(CSFlavorLang.flavor==typeflavor.flavor).where(CSFlavorLang.lang_id==CSCSSettings.getLangID())).first()
            else:
                flavor_lang = None
            self.typeflavor_lang_list.append([charactertype_lang,flavor_lang])

    def rowCount(self, parent=QModelIndex()) -> int:
        return len(self.typeflavor_list)

    def columnCount(self, parent=QModelIndex()) -> int:
        return 3

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid():
            return None
        row = index.row()
        column = index.column()
        if row > self.rowCount()+1:
            return None
        if 0 <= column <= 1:
            return self.typeflavor_lang_list[row][column]
        return None

    def flags(self, index):
        column = index.column()
        if 0 <= column <= 1:
            return Qt.ItemIsEditable | Qt.ItemIsEnabled
        if not index.isValid():
            return Qt.ItemIsEnabled
        if index.column() == 2:
            return Qt.ItemIsEnabled
        return Qt.ItemIsEditable | Qt.ItemIsEnabled

    def setData(self, index, value, role=Qt.EditRole):
        if index.isValid() and role == Qt.EditRole:
            self.typeflavor_lang_list[index.row()][index.column()] = value
            if type(value) is CSCharacterTypeLang:
                self.typeflavor_list[index.row()].charactertype = value.charactertype
            if type(value) is CSFlavorLang:
                self.typeflavor_list[index.row()].flavor = value.flavor

    def insertRows(self, row:int, count:int):
        #https://doc.qt.io/qtforpython-6/PySide6/QtCore/QAbstractItemModel.html#PySide6.QtCore.QAbstractItemModel.insertRows
        self.beginInsertRows(QModelIndex(),row,row+count-1)
        type_lang_list = CSCGDB.get_types(self.session)
        for type_lang in type_lang_list:
            first_type_lang = type_lang
            break
        new_typeflavor = CSCharacterTemplateTypeFlavor()
        new_typeflavor.charactertempalte = self.charactertemplate
        new_typeflavor.charactertype = first_type_lang.charactertype
        for i in range(count):
            self.typeflavor_list.insert(row+i, new_typeflavor)
            self.typeflavor_lang_list.insert(row+i, [first_type_lang,None])
        self.endInsertRows()

    def addLine(self, newTypeFlavor):
        position = len(self.typeflavor_list)-1
        self.insertRows(position, 1)

    def removeRow(self, indexRow, parent=None):
        if 0 <= indexRow < len(self.typeflavor_list):
            self.beginRemoveRows(parent or QModelIndex(), indexRow, indexRow)
            self.typeflavor_list.pop(indexRow)
            self.typeflavor_lang_list.pop(indexRow)
            self.endRemoveRows()
            return True
        return False

class CharacterTemplateTypeFlavorView(QTableView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setEditTriggers(QTableView.EditTrigger.AllEditTriggers)

    def load(self,session, typeflavor_list:list[CSCharacterTemplateTypeFlavor], charactertemplate:CSCharacterTemplate):
        self.session = session
        self.charactertemplate = charactertemplate
        self.typeflavor_list = typeflavor_list
        self.setModel(TypeFlavorListModel(session,typeflavor_list,charactertemplate))
        self.setItemDelegateForColumn(0,CharacterTypeLangComboBoxDelegate(session))
        self.setItemDelegateForColumn(1,FlavorLangComboBoxDelegate(session))
        self.setItemDelegateForColumn(2,DeleteButtonDelegate())
        self.horizontalHeader().hide()
        self.resizeRowsToContents()


