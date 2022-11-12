#!/usr/bin/python3
"""Connects to database and list items in database
fiters result using search keyword"""


import MySQLdb
from sys import argv

if __name__ == '__main__':
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    query = "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY id".format(argv[4])
    cur.execute(query)
    while (1):
        row = cur.fetchone()
        if not row:
            break
        print(row)
