import sqlite3


def get_db():
    conn = sqlite3.connect('books.db')
    return conn


def create_tables():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    book_name TEXT NOT NULL, 
    publisher TEXT NOT NULL
    )
    ''')
    conn.commit()
    conn.close()


create_tables()