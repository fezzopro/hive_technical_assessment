from sqlalchemy import Integer, String, Date, DateTime, Float, Column
#from sqlalchemy.sql.schema import Column
#from sqlalchemy.sql.sqltypes import DateTime
#from sqlalchemy.types import Float
from sqlalchemy.ext.declarative import declarative_base
# from .config import Base

Base = declarative_base()

class Customer(Base):
    __tablename__ = 'Customer'

    id = Column(String, primary_key=True)
    firstName = Column(String, nullable=False)
    lastName = Column(String, nullable=False)
    dateOfBirth = Column(Date, nullable=False)
    creditedAt = Column(DateTime, nullable=False)
    updatedAt = Column(DateTime, nullable=False)

class Account(Base):
    __tablename__ = 'Account'

    id = Column(String, primary_key=True)
    accountNumber = Column(String, nullable=False)
    balance = Column(Float, nullable=False)
    creditedAt = Column(DateTime, nullable=False)
    updatedAt = Column(DateTime, nullable=False)

class Address(Base):
    __tablename__ = 'Address'

    id = Column(String, primary_key=True)
    street = Column(String, nullable=False)
    city = Column(String, nullable=False)
    country = Column(String, nullable=False)
    postalCode = Column(String, nullable=False)