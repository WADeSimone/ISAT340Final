import sqlite3
conn=sqlite3.connect("celebrities.db")
cursor=conn.cursor()

# SQL select statement - CHANGE 'celebs' TO 'members' TO SEE MEMBERS TABLE
sql="select * from members"
cursor.execute(sql)

# get the rows
rows=cursor.fetchall()

# iterate over the results and print them
for row in rows:
    print(row)
conn.close()
