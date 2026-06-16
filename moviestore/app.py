from data import add_movie,update_movie,delete_movie,display_movie,movie_exist,search_movie,load_movies,save_movies

def show_menu():
    print("========= Movie shop =========")
    print("1. Display books")
    print("2. Add movie")
    print("3. Update movie")
    print("4. Delete movie")
    print("5. Search movies")
    print("6. Exit")

def main():
    movies = load_movies()
    while True:
        show_menu()
        choice = input("Pick an option between 1-6: ")

        if choice == "1":
            display_movie(movies)
        elif choice =="2":
            title = input("Enter movie title: ")
            genre = input("Enter genre: ")
            duration = input("Enter duration: ")
            year = int(input("Enter movie year: "))
            ratings = float(input("Enter movie ratings: "))
            add_movie(movies,title,genre,duration,year,ratings)
            save_movies(movies)
        elif choice == "3":
            title = input("Enter movie title: ")
            if not movie_exist(movies,title):
                print(f"Error: {title} not found")
            else:
                new_title = input("Enter new title(Enter to skip): ")
                new_genre = input("Enter genre: ")
                new_duration = input("Enter duration: ")
                new_year = input("Enter movie year: ")
                new_ratings = input("Enter movie ratings: ")
                update_movie(movies,title, new_title, new_genre, new_duration, new_year, new_ratings)
                save_movies(movies)
        elif choice == "4":
            title = input("Enter title: ")
            delete_movie(movies,title)
            save_movies(movies)
        elif choice == "5":
            title = input("Enter title: ")
            search_movie(movies,title)
        else:
            print("Thank you for visiting 🥰")
            break
main()
