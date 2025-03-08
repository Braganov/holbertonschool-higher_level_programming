#!/usr/bin/python3

"""
This script connects to a MySQL database
and takes in the name of a state as an argument
and lists all cities of the state name.
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

    query = ("SELECT cities.name FROM cities "
             "JOIN states ON cities.state_id = states.id "
             "WHERE states.name = %s "
             "ORDER BY cities.id ASC ")

    cursor.execute(query, (state_name,))

    results = cursor.fetchall()
    print(", ".join(city[0]for city in results))

    cursor.close()
    mydb.close()
