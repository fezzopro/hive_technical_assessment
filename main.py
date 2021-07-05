
import uuid
from src.config import get_database, session
from uuid import uuid4
from sqlalchemy.sql.functions import now
from fastapi import FastAPI
from sqlalchemy.sql.sqltypes import DateTime, Integer, String
from starlette.requests import Request

from sqlalchemy.orm import Session
from sqlalchemy.dialects.postgresql import Insert, UUID
from src.models import CustomerModel, AccountModel, AddressModel
from src.schemas import AccountID, CustomerSchema, AccountSchema


app = FastAPI()

# print("DateTime:",)

@app.post("/create_customer")
def createCustomer(customer: CustomerSchema):
    # statement = Insert(CustomerModel).values(id=customer.id, firstName=customer.firstName, lastName=customer.lastName, dateOfBirth=customer.dateOfBirth)
    c = CustomerModel(id=customer.id, firstName=customer.firstName, lastName=customer.lastName, dateOfBirth=customer.dateOfBirth)
    session.add(c)
    session.execute()
    return customer.firstName

@app.post("/create_account")
def createAccount(account: AccountSchema):
    # c = CustomerModel(id=str(uuid4()), firstName="Customer.firstName", lastName="Customer.lastName", dateOfBirth="2021-07-03",createdAt="2021-07-03", updatedAt="2021-07-03")
    acc = AccountModel(id=str(uuid4()), accountNumber=account.accountNumber, balance=account.balance, createdAt=account.createdAt, updatedAt=account.updatedAt)
    session.add(acc)
    results = session.commit()
    return {"Status":results}


@app.get("/get_all_customers_with_accounts")
def getAllCustomersAndAccouns():
    c = session.query(AccountModel)
    for customer in c:
        print(customer.id)
    return {customer}

@app.get("/get_customer_account")
def getCustomersAccount(customerId: AccountID):
    c = session.query(AccountModel)
    for customer in c:
        print(customer.id)
    return {"Customers":customer}

@app.post("/credit_and_debit_customer_account")
def creditAndDebitCustomerAccount():
    return {}

@app.post("/credit_customer_account")
def creditCustomerAccount():
    return {}

app.post("/debit_customer_account")
def DebitCustomerAccount():
    return {}

@app.get("/")
def read_root(request: Request) -> None:
    return {"Task": "HiveOnline Challenge", "Swagger Documentation": str(request.url)+"docs", "ReDoc Documentation": str(request.url)+"docs"}