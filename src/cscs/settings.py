from PySide6.QtCore import QSettings
import platform,os
from pathlib import Path

APPNAME = "CSCS"
ORGNAME = "Nikofrom94"

DATABASEDEFAULT= "sqlite+pysqlite:///./db.sqlite3"

LANGDEFAULT = "English_United States"
LANG_IDDEFAULT = 1

class CSCSSettings:
    APPNAME = APPNAME
    @staticmethod
    def _initSettings(file_path:Path) -> QSettings:
        settings:QSettings = QSettings(format(file_path), QSettings.IniFormat)
        settings.beginGroup("Common")
        settings.setValue("DATABASE", DATABASEDEFAULT)
        settings.setValue("LANG_IDDEFAULT", LANG_IDDEFAULT)
        settings.endGroup()
        settings.sync()
        return settings

    @staticmethod
    def _getSettings() -> QSettings:
        file_path = None
        system = platform.system()
        if system == "Linux":
            home_path = Path(os.environ["HOME"])
            file_path = home_path / ".local/share/CSCS/cscs.ini"
        elif system == "Windows":
            home_path = Path(os.environ["APPDATA"])
            file_path = home_path / "CSCS/cscs.ini"
        else:
            raise Exception(f"Sytem not supported : {system}")
        if not file_path.exists():
            return CSCSSettings._initSettings(file_path)
        else:
            return QSettings(format(file_path), QSettings.IniFormat)

    @staticmethod
    def getDatabase():
        settings = CSCSSettings._getSettings()
        settings.beginGroup("Common")
        return {'URL':settings.value("DATABASE")}

    @staticmethod
    def getLang():
        settings = CSCSSettings._getSettings()
        settings.beginGroup("Common")
        return settings.value("LANG")

    @staticmethod
    def getLangID():
        settings = CSCSSettings._getSettings()
        settings.beginGroup("Common")
        return settings.value("LANG_IDDEFAULT")


    @staticmethod
    def setLangID(value:int):
        settings = CSCSSettings._getSettings()
        settings.beginGroup("Common")
        settings.setValue("LANG_IDDEFAULT",value)
        settings.endGroup()
