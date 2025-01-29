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

def execute_modify_query(_cursor, _conn, query) -> None:
    '''
    # PEP8
    :param _cursor: sqlite cursor
    :param _conn:  sqlite connection
    :param query: sql string query
    :return: None
    '''
    _cursor.execute(query)
    _conn.commit()

# 4b
execute_modify_query(cursor, conn, '''DROP TABLE users''')

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
# 1. add function for execute_read_query
# 2. write in a loop, until 'exit', or once:
#      input username
#      input password
#      insert these values into the table
#          login_times = 0
# 3. write in a loop, until 'exit', or once:
#      input username
#      input password
#      check if the user-password correct
#         print "login was successful"
#       bonus:
#       if not, check if the user exist-
#         if so print "wrong pwd"
#         if not print "user does not exist"
#      after successful login (update query):
#         add 1 into the user login_amount