import sys
from pathlib import Path


from PySide6.QtWidgets import QApplication
from PySide6.QtQml import QQmlApplicationEngine

from cscs_db import Session,Database
from CSCS.csdirectory_model import CSDirectoryModel

from settings import CSCSSettings

if __name__ == '__main__':

    # initialize DB session
    session = Session()
    app = QApplication(sys.argv)
    QApplication.setOrganizationName("CSFRRocks")
    QApplication.setApplicationName("Cypher System Character Sheet")
    engine = QQmlApplicationEngine()

    engine.addImportPath(Path(__file__).parent)
    engine.loadFromModule("CSCS", "Main")

    if not engine.rootObjects():
        sys.exit(-1)

    exit_code = app.exec()
    del engine
    sys.exit(exit_code)
