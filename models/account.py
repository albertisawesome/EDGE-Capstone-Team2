import random
from random import randint, randrange

class Account:
    id = 0
    account_number = 0
    customer_id = 0
    current_balance = 0

    
    def __init__(self, customer_id):
        self.customer_id = customer_id   
        account_number = randint(100, 999)
        
        # account = Account(account_number, customer_id)
        x = float(input("Enter your initial deposit: "))

        if(x >= 25):
            self.account_number = account_number
            self.id += 1
            self.deposit(x)
        else:
            print("error your deposit must be greater than or equal to 25")



    # def open_account(customer_id):
    #     account_number = randint(100, 999)
        
    #     # account = Account(account_number, customer_id)
    #     x = input("Enter your initial deposit: ")

    #     if(x >= 25):
    #         account = Account(account_number, customer_id)
    #         account.id += 1
    #         account.deposit(x)
    #     else:
    #         print("error your deposit must be greater than or equal to 25")

    def deposit(self, deposit):
        if(deposit > 0):
            self.current_balance += deposit
        else:
            print("Deposit must be positive")

    def get_id(self):
        return self.id

    def get_account_number(self):
        return self.account_number

    def get_customer_id(self):
        return self.customer_id

    def check_balance(self):
        return self.current_balance

    def withdraw(self, withdraw_amount):
        if(withdraw_amount > self.current_balance and withdraw_amount < 0):
            print("Insufficient funds")
        else:
            self.current_balance -= withdraw_amount        

    def account_info(self):
        print("********************")
        print("Id: ", self.id)
        print("Account Number :", self.account_number)
        print("Customer Id :", self.customer_id)
        print("Current Balance : ", self.current_balance)
        print("********************")
 
if __name__ == "__main__":
    a = Account(5)
    a.account_info()
