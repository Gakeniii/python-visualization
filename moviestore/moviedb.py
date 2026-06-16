import sqlite3

conn = sqlite3.connect("moviestore.db")
cursor = conn.cursor()
print("db connected successfully")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS movies(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            genre TEXT NOT NULL,
            duration TEXT NOT NULL,
            year INTEGER NOT NULL,
            ratings REAL NOT NULL
        )
""")
conn.commit()
print("table created successfully")

def add_movies(title,genre,duration,year,ratings):
    cl_title = title.strip()
    cursor.execute(
        "INSERT INTO movies(title,genre,duration,year,ratings) VALUES(?,?,?,?,?)",
        (cl_title,genre,duration,year,ratings)
    )
    conn.commit()
    print(f"{title} added successfully")


def movie_exist(title):
    search_movie = title.lower().strip()
    cursor.execute("SELECT 1 FROM movies WHERE LOWER(title)=LOWER(?)", (search_movie,))
    return cursor.fetchone() is not None

def update_movies(title, new_title,new_genre,new_duration,new_year,new_ratings):
    cl_title = title.strip()

    cursor.execute(
        "UPDATE movies SET title=?,genre=?,duration=?,year=?,ratings=? WHERE LOWER(title)=LOWER(?)",
        (new_title,new_genre,new_duration,new_year,new_ratings,cl_title)
    )
    conn.commit()
    if cursor.rowcount > 0:
        print("Movie updated successfully!")
    else:
        print(f"Error: Movie '{title}' not found.")

def delete_movies(title):
    cl_title = title.strip()
    cursor.execute(
        "DELETE FROM movies WHERE LOWER(title)=LOWER(?)",(cl_title,)
    )
    conn.commit()
    if cursor.rowcount > 0:
        print("Movie deleted successfully!")
    else:
        print(f"Error: '{title}' not found.")

def search_movies(title):
    cl_title = title.strip()
    cursor.execute("SELECT * FROM movies WHERE LOWER(title)=LOWER(?)",(cl_title,))
    movie = cursor.fetchone()
    if movie:
        print("\n--- Movie Found ---")
        print(f"ID            : {movie[0]}")
        print(f"Movie Title   : {movie[1]}")
        print(f"Genre         : {movie[2]}")
        print(f"Duration      : {movie[3]}")
        print(f"Year          : {movie[4]}")
        print(f"Ratings       : {movie[5]}")
        print("------------------\n")
    else:
            print("Movie not found.")

def display_movies():
    cursor.execute("SELECT * FROM movies")
    movies = cursor.fetchall()
    
    if not movies:
        print("No movies available in the store.")
        return

    print("\n======= All Books =======")
    for m in movies:
        print("\n--- All books ---")
        print(f"ID: {m[0]}")
        print(f"Title: {m[1]}")
        print(f"Author: {m[2]}")
        print(f"Price: {m[3]}")
        print(f"Quantity: {m[4]}")
        print("------------------\n")
    print("=========================\n")