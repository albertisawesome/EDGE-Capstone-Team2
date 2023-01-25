import uvicorn
from fastapi import FastAPI
from models.account import Account
from services.AccountService import AccountService
from repositories.account import AccountRepository
from repositories.customer import CustomerRepository
from repositories.address import AddressRepository
from typing import List

app = FastAPI()
account_repository = AccountRepository()
customer_repository = CustomerRepository()
address_repository = AddressRepository()

account_service = AccountService(account_repository, customer_repository, address_repository)

@app.post('/accounts')
async def open_account(account: Account):
    if account.current_balance < 25.00:
        print("Please deposit an amount greater than 25.00")
    return account_service.open_account(account)

@app.get('/accounts/{account_number}')
async def grab_account(account: Account) -> Account:
    return account_service.get_account(account.account_number)

# @app.get('/accounts/{account_number}/deposit/{amount}')
# async def deposit(account_number, amount, account: Account) -> Account:
#     account.current_balance += amount
#     return grab_account(account)


if __name__ == "__main__":
    uvicorn.run("main:app",host="0.0.0.0",port=8080,reload=True)