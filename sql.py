import sqlite3
con = sqlite3.connect("Movies.db")
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS movies(movie text,director text)")
cur.execute("INSERT INTO movies VALUES('Bhahubali','Rajamouli')")
cur.execute("INSERT INTO movies VALUES('KGF','Prashanth Neel')")
for row in cur.execute("SELECT * FROM movies"):
    print(row)
con.commit()
con.close()
