from data import add_book,display_book,update_book,delete_book,search_book,load_book,save_book,book_exists
from bookdb import add_books,display_books,delete_books,update_books,search_books
def menu():
    print("=======Gakeni's bookstore========")
    print("1. Display books")
    print("2. Add book")
    print("3. Update book")
    print("4. Delete book")
    print("5. Search book")
    print("6. Exit")

def main():
    books = load_book()
    while True:
        menu()
        choice = input("Pick a choice between 1-6: ")

        if choice == "1":
            display_book(books)
            display_books()
        elif choice =="2":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            price = float(input("Enter book price: "))
            quantity = int(input("Enter book quantity: "))
            add_book(books,title,author,price,quantity)
            add_books(title,author,price,quantity)
            save_book(books)
        elif choice == "3":
            title = input("Enter book title: ")
            if not book_exists(books,title):
                print(f"Error:{title} not found!")
            else:
                new_title = input("Enter new title(Enter to skip): ")
                new_author = input("Enter book author: ")
                new_price = float(input("Enter book price: "))
                new_quantity = int(input("Enter book quantity: "))
                update_book(books,title, new_title, new_author,new_price,new_quantity)
                update_books(title, new_title, new_author,new_price,new_quantity)
                save_book(books)
        elif choice == "4":
            title = input("Enter book title: ")
            delete_book(books,title)
            save_book(books)
            delete_books(title)
        elif choice == "5":
            title = input("Enter book title: ")
            search_book(books,title)
            search_books(title)
        else:
            print("Thank you for visiting🥰")
            break
main()