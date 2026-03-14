# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from qt.main_form import Ui_MainWindow
from cscs_db import Session

from settings import CSCSSettings

APP_NAME = "Cypher System Character Sheet"

class MainWindow(QMainWindow):
    def __init__(self, session,parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setObjectName(CSCSSettings.APPNAME)
        self.ui.mainTree.fill_browser(target_tab=self.ui.mainTab,session=session)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    session = Session()
    widget = MainWindow(session)
    widget.show()
    sys.exit(app.exec())
