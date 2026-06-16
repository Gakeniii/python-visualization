from bookdb import add_books,update_books,delete_books,search_books,display_books,book_exist

def menu():
    print("=======Gakeni's bookstore========")
    print("1. Display books")
    print("2. Add book")
    print("3. Update book")
    print("4. Delete book")
    print("5. Search book")
    print("6. Exit")

def main():
    while True:
        menu()
        choice = input("Pick a choice between 1-6: ")

        if choice == "1":
            display_books()
        elif choice =="2":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            price = float(input("Enter book price: "))
            quantity = int(input("Enter book quantity: "))
            add_books(title,author,price,quantity)
        elif choice == "3":
            title = input("Enter book title:")
            if not book_exist(title):
                print(f"Error:{title} not found!")
            else:
                new_title = input("Enter new title(Enter to skip): ")
                new_author = input("Enter book author: ")
                new_price = float(input("Enter book price: "))
                new_quantity = int(input("Enter book quantity: "))
                update_books(title, new_title, new_author,new_price,new_quantity)
        elif choice == "4":
            title = input("Enter book title: ")
            delete_books(title)
        elif choice == "5":
            title = input("Enter book title: ")
            search_books(title)
        else:
            print("Thank you for visiting🥰")
            break
main()