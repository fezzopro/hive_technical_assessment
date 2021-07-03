from uuid import UUID
from datetime import date
import datetime
from sqlalchemy.sql.sqltypes import Integer, String
from pydantic import BaseModel

class Customer(BaseModel):
    id: UUID
    firstName: str
    lastName: str
    dateOfBirth: datetime.date
class Account(BaseModel):
    id: UUID
    accountNumber: str
    balance: float
    createdAt: date
    updatedAt: date
