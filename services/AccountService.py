import psycopg2
from models.account import Account
from repositories.account import AccountRepository
from repositories.customer import CustomerRepository
from repositories.address import AddressRepository

class AccountService():
    def __init__(self, account_repository: AccountRepository, customer_repository : CustomerRepository, address_repository: AddressRepository) -> None:
        self.account_repository = account_repository
        self.customer_repository = customer_repository
        self.address_repository = address_repository


    def open_account(self, account: Account) -> Account:
        address = self.address_repository.insert(account.customer.address)
        account.customer.address = address
        customer = self.customer_repository.insert(account.customer)
        account.customer = customer
        return self.account_repository.insert(account)


    # def get_all_accounts(self) -> 'list[Account]':
    #     accounts = self.account_repository.get_all()
    #     for account in accounts:
    #         account.customer = self.customer_repository.get_by_id(account.customer.id)
    #         account.customer.address = self.address_repository.get_by_id(account.customer.address.id)
    #     return accounts


    def get_by_account_number(self, account_number: str) -> Account:
        with psycopg2.connect() as db:
            with db.cursor() as cursor:
                cursor.execute("""
                    SELECT ID, AccountNumber, CustomerID, CurrentBalance FROM 
                        account WHERE AccountNumber=%(account_number)s
                    """, {
                    'account_number': account_number
                }
                )
                row = cursor.fetchone()
        return Account.construct(id=row[0], account_number=row[1], customer=Customer.construct(id=row[2]), current_balance=round(row[3], 2))


    def get_account(self, account_number: str) -> Account:
        account = self.account_repository.get_by_account_number(account_number)
        account.customer = self.customer_repository.get_by_id(account.customer.id)

