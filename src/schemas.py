from uuid import UUID
from datetime import date
from pydantic import BaseModel

class Customer(BaseModel):
    id: UUID
    firstName: str
    lastName: str
    dateOfBirth: date
class Account(BaseModel):
    id: UUID
    accountNumber: str
    balance: float
    createdAt: date
    updatedAt: date
