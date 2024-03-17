#!/usr/bin/python3
""" Lists all states from the database hbtn_0e_0_usa """

import MySQLdb
import sys

if __name__ == "__main__":
    # Establish a connection to the MySQL database
    db = MySQLdb.connect(
            host="localhost",
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            port=3306
            )

    # Create a cursor object to execute queries
    cur = db.cursor()

    # Execute the SQL query to retrieve all states
    cur.execute("SELECT * FROM states")

    # Fetch all rows returned by the query
    rows = cur.fetchall()

    # Print each row
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cur.close()
    db.close()
