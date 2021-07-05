from sqlalchemy import String, Date, DateTime, Float, Column
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class CustomerModel(Base):
    __tablename__ = 'Customer'

    id = Column(String, primary_key=True)
    firstName = Column(String, nullable=False)
    lastName = Column(String, nullable=False)
    dateOfBirth = Column(Date, nullable=False)
    createdAt = Column(DateTime, nullable=False, default=DateTime)
    updatedAt = Column(DateTime, nullable=True, default=DateTime)

class AccountModel(Base):
    __tablename__ = 'Account'

    id = Column(String, primary_key=True)
    accountNumber = Column(String, nullable=False)
    balance = Column(Float, nullable=False)
    createdAt = Column(DateTime, nullable=False)
    updatedAt = Column(DateTime, nullable=False)

class AddressModel(Base):
    __tablename__ = 'Address'

    id = Column(String, primary_key=True)
    street = Column(String, nullable=False)
    city = Column(String, nullable=False)
    country = Column(String, nullable=False)
    postalCode = Column(String, nullable=False)