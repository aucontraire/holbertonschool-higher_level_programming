#!/usr/bin/python3
"""Script displays states in database by ascending id order
   Script should take 3 arguments:
   mysql username, mysql password and database name
"""

if __name__ == '__main__':
    import sys
    import MySQLdb

    if len(sys.argv) > 3:
        conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            charset="utf8"
        )
        cur = conn.cursor()
        cur.execute("""SELECT * FROM states ORDER BY states.id ASC""")
        query_rows = cur.fetchall()
        for row in query_rows:
            print(row)
        cur.close()
        conn.close()
