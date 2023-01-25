import psycopg2
from models.address import Address
from models.customer import Customer
from models.account import Account



class AddressRepository():
    def insert(self, account: Account) -> Address:
        with psycopg2.connect() as db:
            with db.cursor() as cursor:
               

                cursor.execute("""INSERT INTO address(Address, City, State, ZipCode)
             VALUES(%(address)s, %(city)s, %(state)s, %(zip_code)s) 
             RETURNING id
             """, {
                    'address': account.customer.address,
                    'city': account.customer.address.city,
                    'state': account.customer.address.state,
                    'zip_code': account.customer.address.zip_code



            }
            )
            account.customer.id = cursor.fetchone()[0]
        return account.customer.address