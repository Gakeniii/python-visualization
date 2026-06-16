from moviedb import add_movies,delete_movies,display_movies,search_movies,update_movies,movie_exist

def show_menu():
    print("========= Movie shop =========")
    print("1. Display books")
    print("2. Add movie")
    print("3. Update movie")
    print("4. Delete movie")
    print("5. Search movies")
    print("6. Exit")

def main():
    while True:
        show_menu()
        choice = input("Pick an option between 1-6: ")

        if choice == "1":
            display_movies()
        elif choice =="2":
            title = input("Enter movie title: ")
            genre = input("Enter genre: ")
            duration = input("Enter duration: ")
            year = int(input("Enter movie year: "))
            ratings = float(input("Enter movie ratings: "))
            add_movies(title,genre,duration,year,ratings)
        elif choice == "3":
            title = input("Enter movie title: ")
            if not movie_exist(title):
                print(f"Error: {title} not found")
            else:
                new_title = input("Enter new title(Enter to skip): ")
                new_genre = input("Enter genre: ")
                new_duration = input("Enter duration: ")
                new_year = input("Enter movie year: ")
                new_ratings = input("Enter movie ratings: ")
                update_movies(title, new_title, new_genre, new_duration, new_year, new_ratings)
        elif choice == "4":
            title = input("Enter title: ")
            delete_movies(title)
        elif choice == "5":
            title = input("Enter title: ")
            search_movies(title)
        else:
            print("Thank you for visiting 🥰")
            break
main()
