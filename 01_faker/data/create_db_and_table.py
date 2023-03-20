import sqlite3
import os

# check if db exists
if os.path.exists("data.db"):
    os.remove("data.db")

# connect to db
connection = sqlite3.connect("data.db")

#  create db cursor
cursor = connection.cursor()

# create table
rows = cursor.execute('''
    CREATE TABLE people(
        firstname, 
        lastname,
        address,
        job,
        company,
        phone,
        email, 
        ssn,
        creditcard_provider,
        credicard_number)
''')

# verify table creation
rows = cursor.execute('SELECT name FROM sqlite_master').fetchall()
print(rows)

