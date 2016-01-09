#https://www.youtube.com/watch?v=Ll_ufNL5rDA
#auto increment primary key
#SQL Read, insert with GUI

import sqlite3
from Tkinter import *


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



#######################################################################################################
#######################################################################################################
#######################################################################################################
#######################################################################################################

root = Tk()

#create label,textboxes and checkbox
label1 = Label(root, text="val1")
label2 = Label(root, text="val2")

textbox1 = Entry(root)
textbox2 = Entry(root)


def getTextbox1Text():
    print textbox1.get()

def getTextbox2Text():
    print textbox2.get()

def getTextboxesToDataBase():
    insertText1 = textbox1.get()
    insertText2 = textbox2.get()
    c.execute("INSERT INTO customers (name,street) VALUES('" + insertText1 + "','" + insertText2 + "')")
    conn.commit()

checkbox1 = Checkbutton(root, text="checbox1")

button1 = Button(root, text="Insert data", command=getTextboxesToDataBase)

button2 = Button(root, text="Read database", command=readTableData)

#Create alignments / sticky e = align to east
label1.grid(row=0, sticky=E)
label2.grid(row=1, sticky=E)

textbox1.grid(row=0, column=1)
textbox2.grid(row=1, column=1)
button1.grid(row=2,column=1)
button2.grid(row=3,column=1)


root.mainloop()
