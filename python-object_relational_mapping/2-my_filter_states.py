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

    mydb = MySQLdb.connect(
        host="localhost",
        user=username,
        password=password,
        database=database
        )

    cursor = mydb.cursor()

    cursor.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC",
                   (state_name,))

    for state in cursor.fetchall():
        print(state)

    cursor.close()
    mydb.close()
