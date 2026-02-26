# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from qt.main_form import Ui_MainWindow
from cscs_db import CSCGDB

CSQT_DBPATH = './db.sqlite3'

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        session = CSCGDB(CSQT_DBPATH)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.csItemDirectory.fill_browser(target_tab=self.ui.csItemTab,session=session)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
