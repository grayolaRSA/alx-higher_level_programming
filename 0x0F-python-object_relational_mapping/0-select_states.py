#!/usr/bin/python3
"""
Lists states from database hbtn_0e_0_usa
"""
import sys
import MySQLdb

if __name__ == '__main__':
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cur = db.cursor()
    query = "SELECT * FROM states ORDER BY id ASC"
    cur.execute(query)
    states = cur.fetchall()

    for state in states:
        print(state)
