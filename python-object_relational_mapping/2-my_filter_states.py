#!/usr/bin/python3

"""
Filters database for user search
"""

import MySQLdb
import sys


if __name__ == "__main__":
    MY_HOST = "localhost"
    MY_PORT = 3306
    MY_USER = sys.argv[1]
    MY_PASS = sys.argv[2]
    MY_DB = sys.argv[3]
    USER_INPUT = sys.argv[4]
    db = MySQLdb.connect(
        host=MY_HOST,
        port=MY_PORT,
        user=MY_USER,
        passwd=MY_PASS,
        db=MY_DB
        )
    cursor = db.cursor()

    query = (
        "SELECT * FROM states WHERE name = '{}' ORDER BY states.id ASC"
        )

    cursor.execute(query.format(USER_INPUT))

    query_rows = cursor.fetchall()
    for row in query_rows:
        print(row)

    cursor.close()
    db.close()
