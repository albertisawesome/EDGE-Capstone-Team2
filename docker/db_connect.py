#!/usr/bin/python

import psycopg2

conn = psycopg2.connect( 
    host="group2rds.ckokfd9swhyk.us-west-2.rds.amazonaws.com", 
    database="group2rds", 
    user="postgres", 
    password="password") 
  

cursor = conn.cursor()  

#sannity check - am i actually connected to the database?? 

cursor.execute('''CREATE TABLE IF NOT EXISTS ADDRESS (ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, ADDRESS VARCHAR(50) NOT NULL, CITY VARCHAR(25) NOT NULL, STATE CHAR(2) NOT NULL, ZIP_CODE CHAR(5) NOT NULL);''') 
print('Address table ready') 


cursor.execute('''CREATE TABLE IF NOT EXISTS CUSTOMER (ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, FIRST_NAME VARCHAR(25) NOT NULL, LAST_NAME VARCHAR(25) NOT NULL, ADDRESS_ID INTEGER NOT NULL, EMAIL_ADDRESS VARCHAR(50) NOT NULL, FOREIGN KEY (ADDRESS_ID) REFERENCES ADDRESS (ADDRESS_ID));''') 
print('Customer table ready') 

conn.execute('''CREATE TABLE IF NOT EXISTS ACCOUNT (ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, ACCOUNT_NUMBER CHAR(10) NOT NULL, CUSTOMER_ID INTEGER NOT NULL, CURRENT_BALANCE DECIMAL(8, 2) NOT NULL, FOREIGN KEY (CUSTOMER_ID) REFERENCES CUSTOMER (CUSTOMER_ID));''') print('Account table ready') 
print('Account table ready')

cursor.execute('SELECT * FROM information_schema.tables') 

 
rows = cursor.fetchall() 

for table in rows: 

    print(table) 

conn.close() 
