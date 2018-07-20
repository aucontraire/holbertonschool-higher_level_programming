#!/usr/bin/python3
"""Script displays states in database by ascending id order that match request
   and protects against SQL injections
   Script should take 4 arguments:
   mysql username, mysql-password, database-name, state-name
"""

if __name__ == '__main__':
    import sys
    import MySQLdb
    import re

    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        charset="utf8"
    )
    cur = conn.cursor()
    re_apost = re.compile("(a?[^']+)")
    state = re_apost.findall(sys.argv[4])
    query = """SELECT * FROM states WHERE name = '{}' ORDER BY states.id ASC"""
    cur.execute(query.format(sys.argv[4]))
    query_rows = cur.fetchall()
    for row in query_rows:
        if row[1] == state[0]:
            print(row)
    cur.close()
    conn.close()
