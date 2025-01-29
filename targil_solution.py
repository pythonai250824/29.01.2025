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
    execute a modify query (insert, update, delete)
    # PEP8
    :param _cursor: sqlite cursor
    :param _conn:  sqlite connection
    :param query: sql string query
    :return: None
    '''
    _cursor.execute(query)
    _conn.commit()

def execute_read_query(_cursor, query) -> list:
    '''
    execute a read query (select)
    :param _cursor: sqlite cursor
    :param _conn:  sqlite connection
    :param query: sql string query
    :return: list of dict
    '''
    _cursor.execute(query)
    _rows = _cursor.fetchall()
    _answer = []
    for _row in _rows:
        _answer.append(dict(_row))
    return _answer

def print_color(message, color="red"):
    match color:
        case "red":
            COLOR = '\033[31m'
            RESET = '\033[0m'
        case "blue":
            COLOR = '\033[34m'
            RESET = '\033[0m'
        case _:
            COLOR = '\033[31m'
            RESET = '\033[0m'
    print(f"{COLOR}{message}{RESET}")


# 4b
execute_modify_query(cursor, conn, '''DROP TABLE IF EXISTS users''')

execute_modify_query(cursor, conn, '''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username text UNIQUE NOT NULL,
    pwd text NOT NULL check(length(pwd) >= 4),
    login_times integer default 0
)
''')

# 4b
execute_modify_query(cursor, conn,'''
    INSERT INTO users (username, pwd, login_times)
    values 
    ('itay', '1234', 100),
    ('danny', 'abcd', 999),
    ('sharon', '1111', 3033);
''')

# 4a
answer = execute_read_query(cursor, '''select * from users;''')

print('------------ new user registration')
while True:
    username: str = input('username? [type "exit" to quit] ')
    if username.lower() == "exit":
        break
    result = execute_read_query(cursor, f'select * from users where username="{username}";')
    if result:
        print_color(f"Oooops: the user '{username}' already exists", "red")
        print('try again ...')
        continue

    pwd: str = input('pwd? ')
    try:
        execute_modify_query(cursor, conn,'''
        INSERT INTO users (username, pwd)
        values ''' + f"('{username}', '{pwd}')" )
        print_color("user inserted...", "blue")

    except Exception as e:
        # print in red -- for fun
        print_color(f"Ooooops: {e}", "red")
        print('try again ...')

print('------------ login')
while True:
    username: str = input('username? [type "exit" to quit] ')
    if username.lower() == "exit":
        break
    result = execute_read_query(cursor, f'select * from users where username="{username}";')
    if not result:
        print_color(f"Oooops: the user '{username}' does not exist", "red")
        print('try again ...')
        continue

    pwd: str = input('pwd? ')
    # option 1
    if pwd == result[0]['pwd']:
        # login succeed
        # break
        pass

    # option 2
    result = execute_read_query(cursor, f'select * from users where username="{username}"' +
                                        f' and pwd="{pwd}";')
    if not result:
        print_color(f"Oooops: wrong password for user '{username}'", "red")
        print('try again ...')
        continue
    print_color(f"login succeeded for user {username}...", "blue")
    execute_modify_query(cursor, conn,
        f"update users" + \
        f" set login_times = login_times + 1" + \
        f" where username='{username}' and pwd='{pwd}'")
    break

# 5 close connection
conn.close()

# 1. add function for execute_read_query -- Done.
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