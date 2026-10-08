import sqlite3
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# __________________________________________

#cursor.execute("""
#CREATE TABLE users (
#    id INTEGER PRIMARY KEY,
#    username TEXT,
#    dateofbirth TEXT,
#    login_attempts INTEGER
#)
#""")

# __________________________________________

#cursor.execute("INSERT INTO users (username, dateofbirth, login_attempts) VALUES ('bob', '10/10/2000', 5)")
#cursor.execute("INSERT INTO users (username, dateofbirth, login_attempts) VALUES ('alex', '11/02/2000', 27)")
#cursor.execute("INSERT INTO users (username, dateofbirth, login_attempts) VALUES ('kim', '02/12/1990', 12)")
#cursor.execute("INSERT INTO users (username, dateofbirth, login_attempts) VALUES ('john', '12/12/1992', 5)")
#cursor.execute("INSERT INTO users (username, dateofbirth, login_attempts) VALUES ('johnny', '01/10/1987', 13)")
#cursor.execute("INSERT INTO users (username, dateofbirth, login_attempts) VALUES ('tommy', '09/07/1992', 15)")
#cursor.execute("INSERT INTO users (username, dateofbirth, login_attempts) VALUES ('aimal', '02/12/1990', 16)")
#cursor.execute("INSERT INTO users (username, dateofbirth, login_attempts) VALUES ('frederik', '02/05/1992', 6)")
#cursor.execute("INSERT INTO users (username, dateofbirth, login_attempts) VALUES ('erik', '02/04/2005', 8)")
#cursor.execute("INSERT INTO users (username, dateofbirth, login_attempts) VALUES ('mads', '12/07/1992', 10)")

# Ændringen skrives til databasen, samt den gemmes.
conn.commit()

print("--- 1 Hent alle brugere og udskriv dem ---")
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
for row in rows:
    print(row)

print("\n--- 2 Hent kun brugernavnene og udskriv dem ---")
cursor.execute("SELECT username FROM users")
rows = cursor.fetchall()
for row in rows:
    print(row)

print("\n--- 3 Hent alle brugere hvor login_attempts er større end 10 ---")
cursor.execute("SELECT * FROM users WHERE login_attempts > 10")
rows = cursor.fetchall()
for row in rows:
    print(row)

conn.close()