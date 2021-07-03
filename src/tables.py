from sqlalchemy import Integer, String, Date, Double
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import DateTime
from .db import Base


class Job(Base):
    __tablename__ = 'Customer'

    id = Column(String, primary_key=True)
    firstName = Column(String, nullable=False)
    lastName = Column(String, nullable=False)
    dateOfBirth = Column(Date, nullable=False)
    creditedAt = Column(Date, nullable=False)
    updatedAt = Column(Date, nullable=False)

class Job(Base):
    __tablename__ = 'Account'

    id = Column(String, primary_key=True)
    accountNumber = Column(String, nullable=False)
    balance = Column(Double, nullable=False)
    creditedAt = Column(Date, nullable=False)
    updatedAt = Column(Date, nullable=False)

class Job(Base):
    __tablename__ = 'Address'

    id = Column(String, primary_key=True)
    street = Column(String, nullable=False)
    city = Column(String, nullable=False)
    country = Column(String, nullable=False)
    postalCode = Column(String, nullable=False)