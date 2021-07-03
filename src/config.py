# from sqlalchemy.sql.schema import MetaData
from src.models import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import session, sessionmaker

engine = create_engine('postgresql+psycopg2://postgres:postgres@localhost:5432/hiveOnline', echo=True)


localSession = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = localSession()

Base.metadata.create_all(engine)

def get_database():
    database = localSession()
    try:
        yield database
    except:
        database.close()