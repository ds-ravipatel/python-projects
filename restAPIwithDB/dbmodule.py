import sqlite3

def create():
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    create_query = 'CREATE TABLE users(id text, password text, phone text)'
    cur.execute(create_query)
    conn.commit()
    conn.close()

#create()
def insert(id_, pass_, phone_):
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    insert_query = "INSERT INTO users VALUES(?,?,?)"
    cur.execute(insert_query, (id_, pass_, phone_))
    conn.commit()
    conn.close()
    return 'Record Inserted'

#insert('Ravi', 'Ravi123', '123456')

def select(id_, pass_):
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    select_query = "SELECT * FROM users WHERE id = ? and password = ?"
    cur.execute(select_query, (id_, pass_))
    all_users = cur.fetchall()
    conn.close()
    return all_users
'''
print(select())
insert('Manoj', 'Manya123', '123456')
print(select())
'''

def update_password(id_, pass_):
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    update_query = "UPDATE users set password = ? WHERE id = ?"
    cur.execute(update_query, (pass_, id_))
    conn.commit()
    conn.close()
    return f'Password Updated for id - {id_}'
'''
print(select())
update_password('Manoj', '123Manya123')
print(select())
'''