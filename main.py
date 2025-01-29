# 1 import
import sqlite3

# 2 create connector
# create if not exist
conn = sqlite3.connect('29_01_2025.db')

# feature: allow access column by name
# row['order_price'] instead of row[3]
# black-box
conn.row_factory = sqlite3.Row

# 3 create cursor
cursor = conn.cursor()

# 4b
cursor.execute('''DROP TABLE users''')
conn.commit()

# 4b
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username text UNIQUE NOT NULL,
    pwd text NOT NULL check(length(pwd) >= 4),
    login_times integer
)
''')

# write the data into the db file
conn.commit()

# 4b
cursor.execute('''
    INSERT INTO users (username, pwd, login_times)
    values 
    ('itay', '1234', 100),
    ('danny', 'abcd', 999),
    ('sharon', '1111', 3033);
''')

# write the data into the db file
conn.commit()

# 4a
cursor.execute('''
select * from users;
''')

rows = cursor.fetchall()
answer = []
total = 0
for row in rows:
    # we did -- conn.row_factory = sqlite3.Row
    # recommended when we do not
    # want to make a list of ALL rows
    # or a dict PER row
    # and not access column by number
    print(row['username'])
    total += int(row['login_times'])

    # convert each row to --> list,tuple,dict
    # answer.append(list(row))
    # answer.append(tuple(row))
    answer.append(dict(row))

print('total is', total)
print(answer)

# 5 close connection
conn.close()
