#https://www.youtube.com/watch?v=Ll_ufNL5rDA
#auto increment primary key
import sqlite3

conn = sqlite3.connect('tutorial.db')
c = conn.cursor()

def tableCreate():
    c.execute('''CREATE TABLE customers
    (id INTEGER PRIMARY KEY, name TEXT, street TEXT)''')

def dataEntry():
    c.execute('''INSERT INTO customers (name,street) VALUES('johhn','Berhlin')''')
    conn.commit()

tableCreate()

dataEntry()
