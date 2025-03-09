#!/usr/bin/python3

"""
This script connects to a MySQL database
and lists all states where name matches
the argument.It takes 4 arguments:
MySQL username, password, and database name
state name searched.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        db=database,
        port=3306
    )

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(state_name))
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
