#!/usr/bin/python

import psycopg2


conn = psycopg2.connect( 

    host="localhost", 

    database="postgres", 

    user="postgres", 

    password="test") 

 
 

cursor = conn.cursor() 

 
 

#sannity check - am i actually connected to the database?? 

cursor.execute('SELECT * FROM information_schema.tables') 

 
 

rows = cursor.fetchall() 

for table in rows: 

    print(table) 

conn.close() 