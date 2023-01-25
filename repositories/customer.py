import psycopg2
from models.address import Address
from models.customer import Customer
from models.account import Account




class CustomerRepository():
    def insert(self, customer: Customer) -> Customer:
        with psycopg2.connect() as db:
            with db.cursor() as cursor:


                cursor.execute("""INSERT INTO customer(FirstName, LastName, Address, EmailAddress)
             VALUES(%(first_name)s, %(last_name)s, %(address)s, %(email_address)s) 
             RETURNING id
             """, {
                    'first_name': customer.first_name,
                    'last_name': customer.last_name,
                    'address': customer.address,
                    'email_address': customer.email_address
    

            }
            )
            customer.id = cursor.fetchone()[0]
        return customer