import sqlite3
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import select

from models import CSFocusLang, CSCharacterTypeLang, CSAbilityLang,Language,CSDescriptorLang

class CSCGDB():
    def __init__(self, db_path):
        self.engine = create_engine("sqlite+pysqlite:///./db.sqlite3")
        self.session = Session(self.engine)

    def get_csitems(self, table_name, wrapper):
        query = f"SELECT * FROM {table_name} ORDER BY name_en"
        cursor = self.con.execute(query)
        items = []
        for row in cursor:
            items.append(wrapper(row))
        return items

    def get_abilities(self, lang_id):
        """get all abilities"""
        return self.session.scalars(select(CSAbilityLang).join(Language).where(Language.id==lang_id).order_by('name'))
    
    def get_foci(self, lang_id):
        return self.session.scalars(select(CSFocusLang).join(Language).where(Language.id==lang_id).order_by('name'))

    def get_types(self, lang_id):
        return self.session.scalars(select(CSCharacterTypeLang).join(Language).where(Language.id==lang_id).order_by('name'))

    def get_descriptors(self,lang_id):
        return self.session.scalars(select(CSDescriptorLang).join(Language).where(Language.id==lang_id).order_by('name'))


