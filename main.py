
from src.config import get_database, session
from uuid import uuid4
import uuid
from sqlalchemy.sql.functions import now
from fastapi import FastAPI
from src.models import Base
from sqlalchemy.sql.sqltypes import DateTime, Integer, String
from starlette.requests import Request

from sqlalchemy.orm import Session
from sqlalchemy.dialects.postgresql import Insert, UUID
from src.models import CustomerModel, AccountModel, AddressModel
from src.schemas import CustomerSchema, AccountSchema


app = FastAPI()

# print("DateTime:",)

@app.post("/create_customer")
def createCustomer(customer: CustomerSchema):
    db = Session(get_database)
    statement = Insert(CustomerModel).values(id=customer.id, firstName=customer.firstName, lastName=customer.lastName, dateOfBirth=customer.dateOfBirth)
    c = CustomerModel(id=customer.id, firstName=customer.firstName, lastName=customer.lastName, dateOfBirth=customer.dateOfBirth)
    # db.add(c)
    # db.query(Customer).get(2)
    # db.commit()
    statement.execute()
    print(statement)
    return customer.firstName

@app.post("/create_account")
def createAccount(account: AccountSchema):
    return {"Status":"Created"}

@app.get("/get_all_customers_with_accounts")
def getAllCustomersAndAccouns():

    # c = CustomerModel(id=uuid.uuid4(), firstName="Customer.firstName", lastName="Customer.lastName", dateOfBirth="2021-07-03",creditedAt="2021-07-03", updatedAt="2021-07-03")
    c = session.query(CustomerModel)
    # session.add(c)
    # session.commit()
    for customer in c:
        print(customer.firstName)
    return {}

@app.get("/get_customer_account")
def getCustomersAccount(customerId: AccountSchema):
    return {"customerID":customerId}

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