import sqlite3

# connect to a database
connection = sqlite3.connect('data.db')

# responsible for executing SQL queries
cursor = connection.cursor()

# create query
create_table = 'CREATE TABLE users (id int, username text, password text)'

# run query
cursor.execute(create_table)

# user object
user = (1, 'alex', 'password')

# insert query
insert_query = 'INSERT INTO users VALUES (?, ?, ?)'

# insert with data
cursor.execute(insert_query, user)

# runs multiple queries
users = [
    (2, 'jennifer', 'password'),
    (3, 'shiloh', 'password'),
    (4, 'luna', 'password')
]

cursor.executemany(insert_query, users)

select_all = 'SELECT * FROM users'
for row in cursor.execute(select_all):
    print(row)


# writes to disk
connection.commit()

# closes the connection
connection.close()
