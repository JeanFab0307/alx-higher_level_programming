#!/usr/bin/python3
"""Lists all States from the database hbtn_0e_0_usa"""

if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    db = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    query = "SELECT * FROM states WHERE states.name = '{}'"
    "ORDER BY states.id ASC"
    value = argv[4].partition(";")
    if value[1] == ";":
        value = value[0][:-1]
    else:
        value = value[0]
    query = query.format(value)
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
