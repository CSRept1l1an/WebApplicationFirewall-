import sqlite3

connection = sqlite3.connect('database.db', check_same_thread=False)


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('First Post', 'Content for the first post')
            )

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Second Post', 'Content for the second post')
            )

cur.execute("INSERT INTO users(username, password) VALUES(?, ?)", 
            ("username", "username")
            )

for user in cur.execute(f"SELECT *  from users  ").fetchall():
    print(user[1])

connection.commit()
connection.close()
