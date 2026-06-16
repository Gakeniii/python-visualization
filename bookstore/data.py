import os
import json

FILENAME = "books.json"

def load_book():
    if os.path.exists(FILENAME):
        with open(FILENAME,'r')as file:
            return json.load(file)
    return[]

def save_book(books):
    with open(FILENAME, 'w')as file:
        return json.dump(books,file, indent=4)


def add_book(books,title,author,price,quantity):
    book = {
        "id": len(books) + 1,
        "title": title,
        "author": author,
        "price": price,
        "quantity": quantity
    }
    books.append(book)
    print(f"\n{title} added successfully")

def display_book(books):
    if not books:
        print("No books available")
        return
    
    for book in books:
        print("\n------------------------------------------\n")
        print(f"Book title  : {book['title']}")
        print(f"Author      : {book['author']}")
        print(f"Price       : {book['price']}")
        print(f"Quantity    : {book['quantity']}")
        print("\n------------------------------------------\n")

def book_exists(books,title):
    search_title = title.lower().strip()
    for book in books:
        if book['title'].lower().strip() == search_title:
            return True
    return False

def update_book(books,title, new_title, new_author, new_price, new_quantity):
    search_title = title.lower().strip()
    found = False

    for book in books:
        if book['title'].lower().strip() == search_title:
            print("\n------------------------------------------\n")
            
            if new_title: book['title'] = new_title
            if new_author : book['author']= new_author
            if new_price : book['price'] = new_price
            if new_quantity : book['quantity'] = new_quantity
            
            print("Book updated successfully!")
            print(f"New title   : {book['title']}")
            print(f"New Author  : {book['author']}")
            print(f"New Price   : {book['price']}")
            print(f"New Quantity: {book['quantity']}\n")
            found = True
            break
    if not found:
        print(f"Error: Book '{title}' not found.")


def search_book(books,title):
    found = False
    for book in books:
        if book['title'].lower() == title.lower():
            print("\n------------------------------------------\n")
            print("Book found successfully!")
            print(f"Book title: {book['title']}")
            print(f"Book author: {book['author']}")
            print(f"Price: {book['price']}")
            print(f"Quantity: {book['quantity']}\n")
            found = True
            break

    if not found:
        print(f"{title} not found")

def delete_book(books,title):
    search_title = title.strip().lower()
    found = False

    for book in books:
        if book['title'].strip().lower() == search_title:
            print("\n------------------------------------------\n")
            print(f"Deleting book: {book['title']}")
            books.remove(book)
            print("Book deleted successfully!\n")
            found = True
            break
    if not found:
        print(f"Error: Book '{title}' not found.")