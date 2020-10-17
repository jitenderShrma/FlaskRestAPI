import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

user_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
post_table = "CREATE TABLE IF NOT EXISTS posts (id INTEGER PRIMARY KEY, title text, desc text)"

cursor.execute(user_table)
cursor.execute(post_table)
# insert_query = "INSERT INTO posts VALUES(NULL, ?, ?)"
# fetch_query = "SELECT * FROM posts"

# result = cursor.execute(fetch_query)

# cursor.execute(insert_query, ('demo', 'description goes here'))
connection.commit()
connection.close()