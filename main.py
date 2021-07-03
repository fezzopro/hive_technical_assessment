from sqlalchemy.sql.sqltypes import Integer, String
from fastapi import FastAPI
from starlette.requests import Request

from pydantic import BaseModel
from src.config import get_database
from sqlalchemy.orm import Session
from src.schemas import Customer, Account


app = FastAPI()

print("DB: ",get_database())

@app.post("/create_customer")
def createCustomer(customer: Customer):
    return "created"

@app.post("/create_account")
def createAccount(account: Account):
    return {"Status":"Created"}

@app.get("/get_all_customers_with_accounts")
def getAllCustomersAndAccouns():
    return {}

@app.get("/get_customer_account")
def getCustomersAccount(customerId: Account):
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