import sqlite3
conn=sqlite3.connect("celebrities.db")
cursor=conn.cursor()

# create a table called celebs with 7 fields
sql="create table celebs(celebID int PRIMARY KEY, firstname text, lastname text, age int, email text, photo text, bio text)"
cursor.execute(sql)

# commit changes to the db
conn.commit()
conn.close()