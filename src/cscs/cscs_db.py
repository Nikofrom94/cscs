import sqlite3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select,delete

from models import CSFocusLang, CSCharacterTypeLang, CSAbilityLang,Language,CSDescriptorLang,CSFlavorLang
from models import CSFocus, CSCharacterType, CSAbility,CSDescriptor,CSFlavor


import settings
db_path=settings.DATABASE['URL']
engine = create_engine(db_path)

Session = sessionmaker(engine)

class CSCGDB():
    @staticmethod
    def get_abilities(session):
        """get all abilities"""
        return session.scalars(select(CSAbilityLang).join(Language).join(CSAbility).where(CSAbility.enabled==True).where(Language.id==settings.LANG_ID).order_by('name'))
    
    @staticmethod
    def get_foci(session):
        return session.scalars(select(CSFocusLang).join(Language).where(Language.id==settings.LANG_ID).order_by('name'))

    @staticmethod
    def get_types(session):
        return session.scalars(select(CSCharacterTypeLang).join(Language).where(Language.id==settings.LANG_ID).order_by('name'))

    @staticmethod
    def get_descriptors(session):
        return session.scalars(select(CSDescriptorLang).join(Language).join(CSDescriptor).where(CSDescriptor.enabled==True).where(Language.id==settings.LANG_ID).order_by('name'))

    @staticmethod
    def get_flavors(session):
        return session.scalars(select(CSFlavorLang).join(Language).where(Language.id==settings.LANG_ID).order_by('name'))

    @staticmethod
    def disable_descriptor(session, id) -> None:
        """Disable descriptor in DB (CSDescriptor.enabled=False)"""
        CSCGDB._disable_item(id, CSDescriptor)

    @staticmethod
    def disable_ability(session, id) -> None:
        """Disable ability in DB (CSAbility.enabled=False)"""
        CSCGDB._disable_item(id, CSAbility)

    @staticmethod
    def _disable_item(session, id, model) -> None:
        result = session.scalars(select(model).where(model.id == id)).first()
        if result is not None:
            result.enabled = False
            session.commit()
