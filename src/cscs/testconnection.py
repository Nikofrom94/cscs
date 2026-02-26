from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import CSAbility,CSAbilityLang,Language
from sqlalchemy import select

engine = create_engine("sqlite+pysqlite:///./db.sqlite3")
conn = engine.connect()
session = Session(engine)
ab = session.scalars(select(CSAbilityLang).join(Language).where(Language.name=="fr-fr").order_by('name')).first()



print(ab.name)