#!/usr/lib/python3



from pydantic import BaseModel
from models.customer import Customer



class Account(BaseModel):
    id: int
    account_number: str
    customer: Customer
    current_balance: float

