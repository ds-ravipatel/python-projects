import sqlite3

def create_db():
    conn = sqlite3.connect('BookData.db')
    c = conn.cursor()
    create_tab_query = "CREATE TABLE books(isbn integer, title text, author text, year integer)"
    c.execute(create_tab_query)
    conn.commit()
    conn.close()

#create_db()

def insert(isbn, title, author, year):
    conn = sqlite3.connect('BookData.db')
    c = conn.cursor()
    insert_query = "INSERT INTO books values(?, ?, ?, ?)"
    c.execute(insert_query, (isbn, title, author, year))
    conn.commit()
    conn.close()

#insert(1,'Harry Puttar 1', 'JK Rowling', 2000)

def delete(isbn):
    conn = sqlite3.connect('BookData.db')
    c = conn.cursor()
    delete_query = "DELETE FROM books where isbn = ?"
    c.execute(delete_query, (isbn,))
    conn.commit()
    conn.close()


def search(isbn= 0, title= "", author= '', year= 0):
    conn = sqlite3.connect('BookData.db')
    c = conn.cursor()
    search_query = "SELECT * FROM books where isbn = ? OR title = ? OR author = ? OR year = ?"
    c.execute(search_query, (isbn, title, author, year))
    result = c.fetchall()
    conn.commit()
    conn.close()
    return result

def update(isbn, title):
    conn = sqlite3.connect('BookData.db')
    c = conn.cursor()
    update_query = "UPDATE books SET title = ? where isbn = ?"
    c.execute(update_query, (title, isbn))
    conn.commit()
    conn.close()

def selectall():
    conn = sqlite3.connect('BookData.db')
    c = conn.cursor()
    search_query = "SELECT * FROM books"
    c.execute(search_query)
    result = c.fetchall()
    conn.commit()
    conn.close()
    return result

