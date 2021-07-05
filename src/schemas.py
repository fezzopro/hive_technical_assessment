from uuid import UUID
from datetime import date
from pydantic import BaseModel

class CustomerSchema(BaseModel):
    id: UUID
    firstName: str
    lastName: str
    dateOfBirth: date

class AccountSchema(BaseModel):
    id: UUID
    accountNumber: str
    balance: float
    createdAt: date
    updatedAt: date

class AddressSchema(BaseModel):
    id: UUID
    street: str
    city: str
    country: str
    postCode: str
    
class AccountID(BaseModel):
    id: UUID