import psycopg2
from models.account import Account
from models.customer import Customer

class AccountRepository():
    def insert(self, account: Account) -> Account:
        with psycopg2.connect() as db:
            with db.cursor() as cursor:
                cursor.execute("")

                cursor.execute('''INSERT INTO account(AccountNumber, CustomerId, CurrentBalance)
                VALUES)''')

                

                cursor.execute("""INSERT INTO account(AccountNumber, CustomerId, CurrentBalance)
             VALUES(%(account_number)s, %(customer_ids)s, %(current_balance)s) 
             RETURNING id
             """, {
                    'account_number': account.account_number,
                    'customer_id': account.customer.id,
                    'current_balance': account.current_balance


            }
            )
            account.id = cursor.fetchone()[0]
        return account