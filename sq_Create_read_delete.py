#https://www.youtube.com/watch?v=Ll_ufNL5rDA
#auto increment primary key
import sqlite3

conn = sqlite3.connect('tutorial.db')
c = conn.cursor()

def tableCreate():
    c.execute('''CREATE TABLE customers
    (id INTEGER PRIMARY KEY, name TEXT, street TEXT)''')

def dataEntry():
    c.execute('''INSERT INTO customers (name,street) VALUES('johhn5','Berhlin5')''')
    conn.commit()


#Read all data from one table inside the database
def readTableData():
    with conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM customers")

        rows = cur.fetchall()

        for row in rows:
            print row


#Delete all data from a table inside the database
def deletAllData():
    with conn:
        cur = conn.cursor()
        cur.execute('delete from customers')
        print('Records after delete: ')
        cur.execute('select * from customers')
        for row in cur.fetchall():
            print('\t', row)

readTableData()
