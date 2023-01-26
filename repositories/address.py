from ctypes import addressof
import psycopg2
from models.address import Address
from models.customer import Customer
from models.account import Account



class AddressRepository():

    conn = psycopg2.connect( 
    host="group2rds.ckokfd9swhyk.us-west-2.rds.amazonaws.com", 
    database="group2rds", 
    user="postgres", 
    password="password") 
  

    #cursor = conn.cursor()  




    def insert(self, address: Address) -> Address:
        with psycopg2.connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute("""INSERT INTO address(Address, City, State, ZipCode)
             VALUES(%(address)s, %(city)s, %(state)s, %(zip_code)s) 
             RETURNING id
             """, {
                    'address': address.address,
                    'city': address.city,
                    'state': address.state,
                    'zip_code': address.zip_code



            }
            )
            address.id = cursor.fetchone()[0]
            conn.close()
        return address

    def get_by_id(self, id) -> Address:
        with psycopg2.connect() as conn:
            with conn.cursor() as cursor:
                cursor.execute("""
                    SELECT ID, Address, City, State, ZipCode FROM 
                        address WHERE ID=%(address_id)s
                    """, {
                    'address_id': id
                }
                )
                row = cursor.fetchone()
            conn.close()
        return Address.construct(id=row[0], address=row[1], city=row[2], state=row[3], zip_code=row[4])