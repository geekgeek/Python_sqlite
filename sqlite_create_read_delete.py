#!/usr/bin/python
# -*- coding: utf-8 -*-
#http://zetcode.com/db/sqlitepythontutorial/

import sqlite3 as lite
import sys

#<create database>
con = lite.connect('test.txt')
#</>

#Create a Table and rows in the database
def createTable():
    with con:
        cur = con.cursor()    
        cur.execute("CREATE TABLE Cars(Id INTEGER PRIMARY KEY AUTOINCREMENT, Name TEXT, Price INT)")

#Insert data inside a table and rows in the database
def insertData():
     with con:
        cur = con.cursor() 
        cur.execute("INSERT INTO Cars(name,price) VALUES('Renault',52642)")
        cur.execute("INSERT INTO Cars(name,price) VALUES('Saab',54642)")

#Read all data from one table inside the database
def readTableData():
    with con:    
        cur = con.cursor()    
        cur.execute("SELECT * FROM Cars")

        rows = cur.fetchall()

        for row in rows:
            print row

#Delete all data from a table inside the database
def deletAllData():
    with con:
        cur = con.cursor() 
        cur.execute('delete from cars')
        print('Records after delete: ')
        cur.execute('select * from cars')
        for row in cur.fetchall():
            print('\t', row)



#createTable()

readTableData()
            
#deletAllData()

#insertData()
