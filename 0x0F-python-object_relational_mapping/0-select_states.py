#!/usr/bin/python3
"""
Script to fetch and display from the database sorted by states.id
"""


import sys
import MySQLdb


if __name__ == "__main__":
    # check if the correct number of arguments are provided
    if len(sys.argv) != 4:
        sys.exit("Usage: ./0-select_states.py <username>"
                 "<password> <database>")

    # Retrieve command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    # connect to MySQL server
    connec = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database,
        charset='utf8'
    )
    cursor = connec.cursor()
    # Execute SQL query to fetch states sorted by id
    cursor.execute("SELECT * FROM states")
    # fetch all rows
    states = cursor.fetchall()

    # Display results as specified
    for state in states:
        print(state)

    # close cursor and connection
    cursor.close()
    connec.close()
