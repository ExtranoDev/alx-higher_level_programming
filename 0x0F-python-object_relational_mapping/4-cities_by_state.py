#!/usr/bin/python3
"""Connects to database and list items in database
list cities in the database"""


import MySQLdb
from sys import argv

if __name__ == '__main__':
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    query = "SELECT cities.id, cities.name, states.name\
            FROM states INNER JOIN cities\
            ON states.id=cities.state_id ORDER BY cities.id;"
    cur.execute(query)
    while (1):
        row = cur.fetchone()
        if not row:
            break
        print(row)
    cur.close()
    db.close()
