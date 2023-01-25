from ctypes import addressof
import psycopg2
from models.address import Address
from models.customer import Customer
from models.account import Account



class AddressRepository():
    def insert(self, address: Address) -> Address:
        with psycopg2.connect() as db:
            with db.cursor() as cursor:
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
        return address