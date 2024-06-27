#!/usr/bin/python3
"""
Script to fetch and display states where name mataches the argument
"""

import sys
import MySQLdb


if __name__ == '__main__':
    # Retrieve command line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    # connect to MySQL server
    conn = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=databse_name,
    )

    # create a cursor object using cursor() method
    cursor = conn.cursor()

    # execute SQL query to fetch states where name matches the argument
    query = "SELECT * FROM states WHERE name LIKE %s"
    cursor.execute(query, (state_name))

    # fetch all rows
    query_rows = cursor.fetchall()

    # display results
    for row in query_rows:
        print(row)

    # close cursor and connection
    cursor.close()
    conn.close()
