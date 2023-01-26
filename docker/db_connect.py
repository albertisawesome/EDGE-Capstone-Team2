#!/usr/bin/python

import psycopg2

conn = psycopg2.connect( 
    host="group2rds.ckokfd9swhyk.us-west-2.rds.amazonaws.com", 
    database="group2rds", 
    user="postgres", 
    password="password") 
  

cursor = conn.cursor()  

#sannity check - am i actually connected to the database?? 

cursor.execute(
            """
            CREATE TABLE Address (
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    address VARCHAR(50) NOT NULL,
                    city VARCHAR(25) NOT NULL,
                    state CHAR(2) NOT NULL,
                    zip_code CHAR(5) NOT NULL);"""
    )


cursor.execute( 
        """ CREATE TABLE IF NOT EXISTS Customer (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                first_name VARCHAR(25) NOT NULL,
                last_name VARCHAR(25) NOT NULL,
                address_id INTEGER NOT NULL,
                email_address VARCHAR(50) NOT NULL.
                FOREIGN KEY (address_id)
                    REFERENCES Address (address_id));"""
    )

cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS Account (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            account_number char(10) NOT NULL
            current_balance DECIMAL (6, 2) NOT NULL,
            FOREIGN KEY (customer_id)
                REFERENCES Customer (customer_id));"""                                         
    )


cursor.execute('SELECT * FROM information_schema.tables') 

 
rows = cursor.fetchall() 

for table in rows: 

    print(table) 

conn.close() 
