import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

create_table = "CREATE TABLE users(id init, username text, password text)"
cursor.execute(create_table)

user = (1, 'user', 'password')
insert_query = "INSERT INTO users VALUES(?, ?, ?)"
cursor.execute(insert_query, user)

users = [
    (2, 'admin', 'password'),
    (3, 'hr', 'password')
]
cursor.executemany(insert_query, users)

fetch_users = "SELECT * FROM users"
my_users = cursor.execute(fetch_users)
for user in my_users:
    print(user)

connection.commit()
connection.close()