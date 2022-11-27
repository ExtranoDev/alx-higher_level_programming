#!/usr/bin/python3
"""Connects to database and list items in database
fiters result using search keyword
Protecting against sql injection"""


import MySQLdb
from sys import argv

if __name__ == '__main__':
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY %s\
    ORDER BY id", (argv[4], ))
    while (1):
        row = cur.fetchone()
        if not row:
            break
        print(row)
    cur.close()
    db.close()
