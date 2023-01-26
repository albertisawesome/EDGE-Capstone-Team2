import psycopg2
from models.account import Account
from models.customer import Customer

class AccountRepository():
    
    conn = psycopg2.connect( 
    host="group2rds.ckokfd9swhyk.us-west-2.rds.amazonaws.com", 
    database="group2rds", 
    user="postgres", 
    password="password") 
  

    #cursor = conn.cursor()  



    def insert(self, account: Account) -> Account:
        with psycopg2.connect() as conn:
            with conn.cursor() as cursor:
               
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
            conn.close()
        return account

        
    def get_by_account_number(self, account_number: str) -> Account:
        with psycopg2.connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute("""
                    SELECT ID, AccountNumber, CustomerID, CurrentBalance FROM 
                        account WHERE AccountNumber=%(account_number)s
                    """, {
                    'account_number': account_number
                }
                )
                row = cursor.fetchone()
            conn.close()
        return Account.construct(id=row[0], account_number=row[1], customer=Customer.construct(id=row[2]), current_balance=round(row[3], 2))