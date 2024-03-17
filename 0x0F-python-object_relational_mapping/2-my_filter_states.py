#!/usr/bin/python3
"""Lists states from the database hbtn_0e_0_usa based on a provided name
pattern."""

import MySQLdb
import sys

def filter_states(db_user, db_password, db_name, name_pattern):
    """Filter states based on the provided name pattern."""
    try:
        db = MySQLdb.connect(host="localhost", user=db_user,
                             passwd=db_password, db=db_name, port=3306)
        cur = db.cursor()
        query = "SELECT * FROM states WHERE name LIKE BINARY %s"
        cur.execute(query, (name_pattern,))
        rows = cur.fetchall()
        for row in rows:
            print(row)
    except MySQLdb.Error as e:
        print("MySQL Error:", e)
    finally:
        if 'cur' in locals():
            cur.close()
        if 'db' in locals():
            db.close()

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python3 my_filter_states.py [DB_USER] [DB_PASSWORD] "
              "[DB_NAME] [NAME_PATTERN]")
        sys.exit(1)

    db_user = sys.argv[1]
    db_password = sys.argv[2]
    db_name = sys.argv[3]
    name_pattern = sys.argv[4]

    filter_states(db_user, db_password, db_name, name_pattern)
