import sqlite3

conn = sqlite3.connect('bookstore.db')
cursor = conn.cursor()
print("connected to bookstore.db")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS booklist(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            price REAL NOT NULL,
            quantity INTEGER NOT NULL
    )
""")

conn.commit()
print("DB created successfully!")

def add_books(title,author,price,quantity):
    cl_title = title.strip()
    cursor.execute(
        "INSERT INTO booklist(title,author,price,quantity) VALUES(?,?,?,?)",
        (cl_title,author,price,quantity)
    )
    conn.commit()
    print(f"{title} added successfully")

def book_exist(title):
    search_book = title.lower().strip()
    cursor.execute("SELECT 1 FROM booklist WHERE LOWER(title)=LOWER(?)", (search_book,))
    return cursor.fetchone() is not None

def update_books(title, new_title, new_author, new_price, new_quantity):
    cl_title = title.strip()

    cursor.execute(
        "UPDATE booklist SET title=?, author=?, price=?, quantity=? WHERE LOWER(title)=LOWER(?)",
        (new_title,new_author,new_price,new_quantity,cl_title)
    )
    conn.commit()
    if cursor.rowcount > 0:
        print("Book updated successfully!")
    else:
        print(f"Error: Book '{title}' not found.")

def delete_books(title):
    cl_title = title.strip()
    cursor.execute(
        "DELETE FROM booklist WHERE LOWER(title)=LOWER(?)",(cl_title,)
    )
    conn.commit()
    if cursor.rowcount > 0:
        print("Book deleted successfully!")
    else:
        print(f"Error: Book '{title}' not found.")

def search_books(title):
    cl_title = title.strip()
    cursor.execute("SELECT * FROM booklist WHERE LOWER(title)=LOWER(?)",(cl_title,))
    book = cursor.fetchone()
    if book:
        print("\n--- Book Found ---")
        print(f"ID: {book[0]}")
        print(f"Title: {book[1]}")
        print(f"Author: {book[2]}")
        print(f"Price: {book[3]}")
        print(f"Quantity: {book[4]}")
        print("------------------\n")
    else:
            print("Book not found.")

def display_books():
    cursor.execute("SELECT * FROM booklist")
    books = cursor.fetchall()
    
    if not books:
        print("No books available in the store.")
        return

    print("\n======= All Books =======")
    for book in books:
        print("\n--- All books ---")
        print(f"ID: {book[0]}")
        print(f"Title: {book[1]}")
        print(f"Author: {book[2]}")
        print(f"Price: {book[3]}")
        print(f"Quantity: {book[4]}")
        print("------------------\n")
    print("=========================\n")