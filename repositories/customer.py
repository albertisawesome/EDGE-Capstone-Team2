import psycopg2
from models.address import Address
from models.customer import Customer
from models.account import Account




class CustomerRepository():

    conn = psycopg2.connect( 
    host="group2rds.ckokfd9swhyk.us-west-2.rds.amazonaws.com", 
    database="group2rds", 
    user="postgres", 
    password="password") 
  

    #cursor = conn.cursor()  



    def insert(self, customer: Customer) -> Customer:
        with psycopg2.connect() as conn:
            with conn.cursor() as cursor:


                cursor.execute("""INSERT INTO customer(FirstName, LastName, Address, EmailAddress)
             VALUES(%(first_name)s, %(last_name)s, %(address_id)s, %(email_address)s) 
             RETURNING id
             """, {
                    'first_name': customer.first_name,
                    'last_name': customer.last_name,
                    'address_id': customer.address.id,
                    'email_address': customer.email_address
    

            }
            )
            customer.id = cursor.fetchone()[0]
            conn.close()
        return customer

    def get_by_id(self, id) -> Customer:
        with psycopg2.connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute("""
                    SELECT ID, FirstName, LastName, AddressID, Email FROM 
                        customer WHERE ID=%(customer_id)s
                    """, {
                    'customer_id': id
                }
                )
                row = cursor.fetchone()
        # In a larger enterprise app, you would likely be using an ORM like
        # SQLAlchemy, which would handle the mapping of the database row to the object
        # (and its hierarchy) automatically. The other approach you could take is to
        # use a separate set of DTOs (Data Transfer Objects) and manage mapping between
        # the DTO and the Pydantic model.
            conn.close()
        return Customer.construct(id=row[0], first_name=row[1], last_name=row[2], address=Address.construct(id=row[3]), email_address=row[4])