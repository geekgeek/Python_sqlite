#!/usr/bin/python
# -*- coding: utf-8 -*-
#http://zetcode.com/db/sqlitepythontutorial/
#Alternative to create db in file: http://codecr.am/blog/post/3/
#Create table, rows and read data
import sqlite3 as lite
import sys

con = lite.connect('test.txt')

def createTable():
    with con:
        cur = con.cursor()    
        cur.execute("CREATE TABLE Cars(Id INTEGER PRIMARY KEY AUTOINCREMENT, Name TEXT, Price INT)")
        cur.execute("INSERT INTO Cars(name,price) VALUES('Audi',52642)")
        cur.execute("INSERT INTO Cars(name,price) VALUES('Toyota',52632)")
        cur.execute("INSERT INTO Cars(name,price) VALUES('Volvo',58642)")
 
def getTableData():
    with con:    
        cur = con.cursor()    
        cur.execute("SELECT * FROM Cars")

        rows = cur.fetchall()

        for row in rows:
            print row

createTable()

#getTableData()
