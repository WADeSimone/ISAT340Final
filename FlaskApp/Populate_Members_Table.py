import sqlite3
conn=sqlite3.connect("celebrities.db")
cursor=conn.cursor()

# data supplied as tuples. ? - placeholders for data
sql="insert into members values(?,?,?,?,?,?)"
data=(1,"William","DeSimone",22,"desimowa@dukes.jmu.edu","I was born and raised in Charlottesville, VA. I attended WAHS and am currently pursuing a B.S. in Integrated Science and Technology at James Madison University in Harrisonburg, VA.")
cursor.execute(sql,data)

# commit the changes to the db
conn.commit()
conn.close()