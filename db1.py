import sqlite3

def connect():
    connection = sqlite3.connect("books.db")
    cur = connection.cursor() #open connection

    cur.execute("CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
    connection.commit()
    connection.close()

def insert(title, author, year, isbn):
    connection = sqlite3.connect("books.db")
    cur = connection.cursor() #open connection

    cur.execute("INSERT INTO books VALUES (NULL, ?,?,?,?)", (title, author, year, isbn))

    connection.commit()  #commit changes to db
    connection.close()  #close connection

def view():
    connection = sqlite3.connect("books.db")
    cur = connection.cursor() #open connection

    cur.execute("SELECT * FROM books")
    rows = cur.fetchall()

    cur.close()
    return rows

def search(title="", author="", year="", isbn=""):  ##empty strings are to prevent required parameter fields if user doesn't pass any
    connection = sqlite3.connect("books.db")
    cur = connection.cursor() #open connection

    cur.execute("SELECT * FROM books WHERE title = ? OR author = ? OR year = ? OR isbn = ?", (title, author, year, isbn))
    rows = cur.fetchall()

    cur.close()
    return rows

def delete(id):
    connection = sqlite3.connect("books.db")
    cur = connection.cursor() #open connection

    cur.execute("DELETE FROM books WHERE id = ?", (id,))

    connection.commit()  #commit changes to db
    connection.close()  #close connection

def update(id, title, author, year, isbn):
    connection = sqlite3.connect("books.db")
    cur = connection.cursor() #open connection

    cur.execute("UPDATE books SET title = ?, author = ?, year = ?, isbn = ? WHERE id = ?", (title, author, year, isbn, id))

    connection.commit()  #commit changes to db
    connection.close()  #close connection


connect()
# update(3, "Goodwill Hunting", "Tim Sykes", 1854, 29294)
# update(4, "Harry Potter and the Half Blood Prince", "J.K. Rowling", 2005, 999999)
# print(view())
