#!/usr/bin/python3
"""Script lists all cities from a given state
   and protects against SQL injections
   Script should take 4 arguments:
   mysql username, mysql-password, database-name, state-name
"""

if __name__ == '__main__':
    import sys
    import MySQLdb

    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        charset="utf8"
    )
    cur = conn.cursor()
    query = """SELECT name FROM cities
    WHERE state_id = (SELECT id FROM states WHERE name = %s)
    ORDER BY id ASC"""
    cur.execute(query, (sys.argv[4],))
    query_rows = cur.fetchall()
    row_len = len(query_rows)
    for i, row in enumerate(query_rows):
        if row_len == 1 or i == row_len - 1:
            print(row[0])
        else:
            print(row[0], end=", ")

    cur.close()
    conn.close()
