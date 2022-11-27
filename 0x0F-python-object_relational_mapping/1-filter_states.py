#!/usr/bin/python3
"""Connects to database and list items in database
fiters result"""


import MySQLdb
from sys import argv

if __name__ == '__main__':
    if (len(argv) == 4):
        db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
        cur = db.cursor()
        query = "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER by id"
        cur.execute(query)

        while (1):
            row = cur.fetchone()
            if row:
                print(row)
            else:
                break
