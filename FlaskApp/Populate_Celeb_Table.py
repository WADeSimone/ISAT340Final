import sqlite3
conn=sqlite3.connect("celebrities.db")
cursor=conn.cursor()

# data supplied as tuples. ? - placeholders for data
sql="insert into celebs values(?,?,?,?,?,?,?)"
data=(1,"Angelina","Jolie",40,"angie@hollywood.us","https://s3.amazonaws.com/isat3402021/aj.jpg","Angelina Jolie is an Academy Award–winning actress known for roles in Girl, Interrupted and Maleficent. She is also a prominent humanitarian and former UNHCR Goodwill Ambassador."),\
(2,"Brad","Pitt",51,"brad@hollywood.us","https://s3.amazonaws.com/isat3402021/bp.jpg","Brad Pitt is a leading Hollywood actor recognized for films like Fight Club, Ocean’s Eleven, and Once Upon a Time in Hollywood. He also produces critically acclaimed films through his company Plan B."),\
(3,"Snow","White",21,"sw@disney.org","https://s3.amazonaws.com/isat3402021/sw.jpg","Snow White is a classic fairy-tale princess known for her kindness, innocence, and friendship with forest animals. Her story centers on escaping her wicked stepmother and finding safety with seven dwarfs."),\
(4,"Darth","Vader",29,"dv@darkside.me","https://s3.amazonaws.com/isat3402021/dv.jpg","Darth Vader is one of the central antagonists of Star Wars, once a Jedi Knight named Anakin Skywalker. His character arc follows his fall to the dark side and eventual redemption."),\
(5,"Taylor","Swift",25,"ts@1989.us","https://s3.amazonaws.com/isat3402021/ts.jpg","Taylor Swift is a globally successful singer-songwriter known for narrative storytelling across genres from country to pop. She is one of the best-selling artists of all time with a massive cultural influence."),\
(6,"Beyonce","Knowles",34,"beyonce@jayz.me","https://s3.amazonaws.com/isat3402021/bk.jpg","Beyonce Knowles is a Grammy-winning singer, performer, and entrepreneur who rose to fame with Destiny’s Child before launching a dominant solo career. She is widely regarded as one of the most influential artists of her generation."),\
(7,"Selena","Gomez",23,"selena@hollywood.us","https://s3.amazonaws.com/isat3402021/sg.jpg","Selena Gomez is a singer, actress, and producer who began her career on Disney Channel before transitioning into music and film. She is also known for her philanthropic work and mental health advocacy."),\
(8,"Stephen","Curry",27,"steph@golden.bb","https://s3.amazonaws.com/isat3402021/sc.jpg","Stephen Curry is a professional NBA player for the Golden State Warriors and widely credited with revolutionizing basketball through long-range shooting. He is a multiple-time MVP and four-time NBA champion.")
cursor.executemany(sql,data)

# commit the changes to the db
conn.commit()
conn.close()
