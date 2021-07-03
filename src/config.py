from src.models import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql+psycopg2://postgres:AdminDB@localhost:5432/hiveOnline', echo=True)

print("DB:",engine)

localSession = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base = declarative_base()
Base.metadata.create_all(engine)

def get_database():
    database = localSession()
    try:
        yield database
    except:
        database.close()