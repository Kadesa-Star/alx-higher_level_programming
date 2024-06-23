#!/usr/bin/python3
import sys
import MySQLdb


def list_states(username, password, database):
    # connect to MySQL server
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
    )
    cursor = db.cursor()

    try:
        # Execute SQL query to fetch states sorted by id
        cursor.execute("SELECT * FROM states ORDER BY id ASC")
        states = cursor.fetchall()

        # Display results as specified
        for state in states:
            print(state)
    except MySQLdb.Error as e:
        print(f"Error querying database: {e}")

    finally:
        # close cursor and connection
        cursor.close()
        db.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./0-select_states.py <username> <password> <database>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    list_states(username, password, database)
