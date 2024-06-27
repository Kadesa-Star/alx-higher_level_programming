#!/usr/bin/python3
"""
Script to list all cities from the databse
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
        db=database_name,
    )

    # create a cursor object using cursor() method
    cursor = conn.cursor()

    # execute SQL query to fetch all cities, joining with states to get names
    query = ("SELECT cities.name "
             "FROM cities JOIN states ON cities.state_id = states.id "
             "WHERE states.name = %s "
             "ORDER BY cities.id")
    cursor.execute(query, (state_name,))

    # fetch all rows
    query_rows = cursor.fetchall()

    # display results
    cities = [row[0] for row in query_rows]
    print(", ".join(cities))

    # close cursor and connection
    cursor.close()
    conn.close()
