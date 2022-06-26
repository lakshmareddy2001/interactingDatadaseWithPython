import sqlite3
con = sqlite3.connect("Movies.db")
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS Movie(movie text PRIMARY KEY,actress text,director text,release date)")
cur.execute("DELETE FROM Movie")
cur.execute("INSERT INTO Movie VALUES('Bhahubali 1','Anushka','Rajamouli','2015')")
cur.execute("INSERT INTO Movie VALUES('KGF 1','Srinidhi Shetty','Prashanth Neel','2018')")
for row in cur.execute("SELECT * FROM Movie"):
    print(row)
con.commit()
con.close()
