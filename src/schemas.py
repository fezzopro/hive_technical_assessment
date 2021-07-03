from uuid import UUID
from datetime import date
import uuid
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
