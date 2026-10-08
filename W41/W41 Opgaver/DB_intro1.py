# This is my first database
import sqlite3
conn = sqlite3.connect("animals.db")
cursor = conn.cursor() # Man sætter pegepind op
# Now starting with empty DB, RUN IT ONCE!, THEN PUT # INFRONT.
#__________________________________________________________________________________

# Vi definerer tabelstrukturen, bemærk her """ xxx """

#cursor.execute("""
#CREATE TABLE animals (
#    id INTEGER PRIMARY KEY,
#    name TEXT,
#    count INTEGER
#)
#""")

#__________________________________________________________________________________

# Der indsættes værdier til name og count.
#cursor.execute("INSERT INTO animals (name,count) VALUES ('pig',15)")
#cursor.execute("INSERT INTO animals (name,count) VALUES ('eagle',5)")
#cursor.execute("INSERT INTO animals (name,count) VALUES ('tiger',23)")
#cursor.execute("INSERT INTO animals (name,count) VALUES ('lion',43)")

# Ændringen skrives til databasen, samt  den gemmes.
conn.commit()

cursor.execute("SELECT * FROM animals")
rows = cursor.fetchall()

for row in rows:
    print(row)

