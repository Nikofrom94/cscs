# https://doc.qt.io/qt-6/qtwidgets-itemviews-simpletreemodel-example.html
# https://doc.qt.io/qtforpython-6/examples/example_widgets_itemviews_editabletreemodel.html

from PySide6.QtCore import QAbstractListModel,QModelIndex,Qt, Slot
from PySide6.QtQml import QmlElement

from cscs_db import CSCGDB,Session,Database

QML_IMPORT_NAME = "CSCS"
QML_IMPORT_MAJOR_VERSION = 1

class CSDirectoryItem:
    def __init__(self, label:str, csDBItem=None, parent: 'CSDirectoryItem' = None):
        self.csDBItem = csDBItem
        self.parent_item = parent
        self.label:str = label
        self.child_items = []

    def child(self, number: int) -> 'CSDirectoryItem':
        if number < 0 or number >= len(self.child_items):
            return None
        return self.child_items[number]

    def last_child(self):
        return self.child_items[-1] if self.child_items else None

    def child_count(self) -> int:
        return len(self.child_items)

    def child_number(self) -> int:
        if self.parent_item:
            return self.parent_item.child_items.index(self)
        return 0

    def insert_child(self, position: int, label:str, csDBItem=None) -> bool:
        """ Insert one children item"""
        if position < 0 or position > len(self.child_items):
            return False

        item = CSDirectoryItem(label=label,csDBItem=csDBItem, parent=self)
        self.child_items.insert(position, item)

        return True

    def insert_children(self, position: int, count: int) -> bool:
        """ Insert a count blank children in position """
        if position < 0 or position > len(self.child_items):
            return False

        for row in range(count):
            item = CSDirectoryItem(None)
            self.child_items.insert(position, item)

        return True

    def append_child(self, childItem:'CSDirectoryItem'):
        self.child_items.append(childItem)

    def parent(self):
        return self.parent_item

    def remove_children(self, position: int, count: int) -> bool:
        if position < 0 or position + count > len(self.child_items):
            return False

        for row in range(count):
            self.child_items.pop(position)

        return True

    def data(self, column: int):
        if column < 0 or column > 1:
            return None
        return self.label

    def set_data(self, label, csDBItem):
        self.label = label
        self.csDBItem = csDBItem
        return True

    def __repr__(self) -> str:
        result = f"<treeitem.CSDirectoryItem "
        result += f' with label={self.label}' if self.label else " <No label>"
        result += f", {len(self.child_items)} children>"
        return result

    def column_count(self) -> int:
        return 1

@QmlElement
class CSDirectoryModel(QAbstractListModel):

    def __init__(self, session=None, parent=None):
        super().__init__(parent)
        self.session = session
        self.root_item = CSDirectoryItem(label="root")
        self.session = Session()
        self.load_data(self.session,self.root_item )

    def load_data(self, session, root:CSDirectoryItem ):
        """Load all data from DB using the session """
        parents = [root]
        # loading abilities
        self.ab_parent = CSDirectoryItem(label=self.tr("Abilities"))
        root.append_child(self.ab_parent)
        parents.append(self.ab_parent)
        self.load_abilities(session,self.ab_parent)
        # loading foci
        self.foci_parent = CSDirectoryItem(label=self.tr("Foci"))
        root.append_child(self.foci_parent)
        parents.append(self.foci_parent)
        self.load_foci(session,self.foci_parent)
        # loading flavors
        self.flavors_parent = CSDirectoryItem(label=self.tr("Flavors"))
        root.append_child(self.flavors_parent)
        parents.append(self.flavors_parent)
        self.load_flavors(session,self.flavors_parent)
        # loading types
        self.types_parent = CSDirectoryItem(label=self.tr("Types"))
        root.append_child(self.types_parent)
        parents.append(self.types_parent)
        self.load_charactertypes(session,self.types_parent)
        # loading descriptors
        self.descriptors_parent = CSDirectoryItem(label=self.tr("Descriptors"))
        root.append_child(self.descriptors_parent)
        parents.append(self.descriptors_parent)
        self.load_descriptors(session,self.descriptors_parent)


    def load_abilities(self,session,parent:CSDirectoryItem) -> None:
        """Load abilities data from DB using the session """
        for csDBItem in CSCGDB.get_abilities(session):
            parent.insert_child(position=parent.child_count(),label = csDBItem.name, csDBItem=csDBItem)
        return parent

    def load_foci(self,session,parent) -> None:
        """Load foci data from DB using the session """
        for csDBItem in CSCGDB.get_foci(session):
            parent.insert_child(position=parent.child_count(),label = csDBItem.name, csDBItem=csDBItem)

    def load_flavors(self,session,parent) -> None:
        """Load flavors data from DB using the session """
        for csDBItem in CSCGDB.get_flavors(session):
            parent.insert_child(position=parent.child_count(),label = csDBItem.name, csDBItem=csDBItem)

    def load_charactertypes(self, session,parent) -> None:
        """Load character types data from DB using the session """
        for csDBItem in CSCGDB.get_types(session):
            parent.insert_child(position=parent.child_count(),label = csDBItem.name, csDBItem=csDBItem)

    def load_descriptors(self, session,parent) -> None:
        """Load descriptor data from DB using the session """
        for csDBItem in CSCGDB.get_descriptors(session):
            parent.insert_child(position=parent.child_count(),label = csDBItem.name, csDBItem=csDBItem)

    def get_item(self, index: QModelIndex = QModelIndex()) -> CSDirectoryItem:
        print(f"get_item : for index ({index.row()} x {index.column()})")
        if index.isValid():
            item:CSDirectoryItem = index.internalPointer()
            if item:
                print(f"  -> get_item : {item}")
                return item
            else:
                print(f"  -> get_item : no item for index ({index.row()} x {index.column()})")
        return self.root_item

    def columnCount(self, parent: QModelIndex = None) -> int:
        return 1

    def rowCount(self, parent_index: QModelIndex = QModelIndex()) -> int:
        if parent_index.isValid() and parent_index.column() > 0:
            return 0
        parent_item: CSDirectoryItem = self.get_item(parent_index)
        if not parent_item:
            return 0
        return parent_item.child_count()

    # CS Directory data is composed of CSDirectoryItem
    def data(self, index: QModelIndex, role: int = None):
        print(f"data for index ({index.row()} x {index.column()}):")
        if not index.isValid():
            return None

        if role == Qt.ItemDataRole.DisplayRole:
            item:CSDirectoryItem = self.get_item(index)
            print(f" => {item}")
            return item.data(index.column())

        return None

    def index(self, row: int, column: int, parent_index: QModelIndex = QModelIndex()) -> QModelIndex:
        print(f"index for row({row}) and col({column}) and parent_index({parent_index.row()} x {parent_index.column()   })")
        if parent_index.isValid() and parent_index.column() != 0:
            return QModelIndex()

        parent_item:CSDirectoryItem = self.get_item(parent_index)
        if not parent_item:
            print(" -> no parent item")
            return QModelIndex()
        print(f" -> parent item ({parent_item})")


        if child_item := parent_item.child(row):
            print(f" -> child item ({child_item})")
            return self.createIndex(row, column, child_item)
        else:
            print(" -> no child item at row ({row})")
        return QModelIndex()

    def insertRows(self, position: int, rows: int,
                   parent:QModelIndex = QModelIndex()) -> bool:
        parent_item:CSDirectoryItem = self.get_item(parent)
        if not parent_item:
            return False

        self.beginInsertRows(parent, position, position + rows - 1)
        success: bool = parent_item.insert_children(position, rows)
        self.endInsertRows()
        return success

    def removeRows(self, position: int, rows: int,
                   parent: QModelIndex = QModelIndex()) -> bool:
        parent_item:CSDirectoryItem = self.get_item(parent)
        if not parent_item:
            return False

        self.beginRemoveRows(parent, position, position + rows - 1)
        success: bool = parent_item.remove_children(position, rows)
        self.endRemoveRows()

        return success

    def parent(self, index: QModelIndex = QModelIndex()) -> QModelIndex:
        if not index.isValid():
            return QModelIndex()

        if child_item := self.get_item(index):
            parent_item:CSDirectoryItem = child_item.parent()
        else:
            parent_item = None

        if parent_item == self.root_item or not parent_item:
            return QModelIndex()

        return self.createIndex(parent_item.child_number(), 0, parent_item)

    def _repr_recursion(self, item: CSDirectoryItem, indent: int = 0) -> str:
        result = " " * indent + repr(item) + "\n"
        for child in item.child_items:
            result += self._repr_recursion(child, indent + 2)
        return result

    def __repr__(self) -> str:
        return self._repr_recursion(self.root_item)

