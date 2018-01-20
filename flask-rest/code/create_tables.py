import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

create_table = 'CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY_KEY, username TEXT, password TEXT)'
cursor.execute(create_table)

create_table = 'CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY_KEY, name TEXT, price REAL)'
cursor.execute(create_table)
cursor.execute("INSERT INTO items VALUES (1, 'test', 10.99)")


connection.commit()
connection.close()
