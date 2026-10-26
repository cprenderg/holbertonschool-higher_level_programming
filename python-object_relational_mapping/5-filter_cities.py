#!/usr/bin/python3

"""
Lists all cities from the database hbtn_0e_4_usa
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
        """
        SELECT cities.name
        FROM cities
        JOIN states
        ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
        """)

    cursor.execute(query, (USER_INPUT,))

    query_rows = cursor.fetchall()
    print(", ".join([row[0] for row in query_rows]))

    cursor.close()
    db.close()
