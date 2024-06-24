#!/usr/bin/python3
"""
script to fetch and display states with name matches the argument
"""
import sys
import MySQLdb


if __name__ == '__main__':
    # Retrieve command line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    # connect to MySQLdb server
    conn = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=mysql_username,
            passwd=mysql_password,
            db=database_name,
            )
    # create a cursor object using cursor() method
    cursor = conn.cursor()

    # execute SQL query to fetch states where name matches the argument
    query = "SELECT * FROM states WHERE name = %s ORDER BY id"
    cursor.execute(query, (state_name,))

    # Fetch all rows
    query_rows = cursor.fetchall()

    # Display results
    for row in query_rows:
        print(row)

    # close cursor and connection
    cursor.close()
    conn.close()
