#!/usr/bin/python

import psycopg2

conn = psycopg2.connect( 
    host="group2rds.ckokfd9swhyk.us-west-2.rds.amazonaws.com", 
    database="group2rds", 
    user="postgres", 
    password="password") 
  

cursor = conn.cursor()  

#sannity check - am i actually connected to the database?? 

cursor.execute('SELECT * FROM information_schema.tables') 

 
rows = cursor.fetchall() 

for table in rows: 

    print(table) 

conn.close() 