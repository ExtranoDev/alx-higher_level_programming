#!/usr/bin/python3

import MySQLdb
import sys

if __name__ == '__main__':
    if (len(sys.argv) == 4):
        user = sys.argv[1]
        passwd = sys.argv[2]
        database = sys.argv[3]
        db = MySQLdb.connect(user=user, passwd=passwd, db=database)
        cur = db.cursor()
        query = "SELECT * FROM states ORDER by id"
        cur.execute(query)

        while (1):
            row = cur.fetchone()
            if row:
                print(row)
            else:
                break
