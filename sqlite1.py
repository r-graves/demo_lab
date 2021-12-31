#!/usr/bin/env python
import datetime
import sqlite3 as db

con = db.connect('main.db')

cur = con.cursor()

# Create table
cur.execute('''CREATE TABLE stocks2
               (date text, trans text, symbol text, qty real, price real)''')

# Insert a row of data
cur.execute("INSERT INTO stocks2 VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

# Save (commit) the changes
con.commit()