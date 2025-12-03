import sqlite3
conn=sqlite3.connect("celebrities.db")
cursor=conn.cursor()

# create a table called members with 6 fields
sql="create table members(memberID int PRIMARY KEY, firstname text, lastname text, age int, email text, bio text)"
cursor.execute(sql)

# commit changes to the db
conn.commit()
conn.close()