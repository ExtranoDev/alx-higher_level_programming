#!/usr/bin/python3
"""Connects to database and list items in database
list cities in the database"""


import MySQLdb
from sys import argv

if __name__ == '__main__':
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities\
            INNER JOIN states WHERE states.name=%s\
            AND states.id=cities.state_id\
            ORDER BY cities.id;", (argv[4], ))
    cities = [i[0] for i in cur.fetchall()]
    print(', '.join(cities))
    cur.close()
    db.close()
