import os
import json

FILENAME = "movies.json"

def load_movies():
    if os.path.exists(FILENAME):
        with open(FILENAME, 'r') as file:
            return json.load(file)
    return[]

def save_movies(movies):
    with open(FILENAME,'w') as file:
        return json.dump(movies,file,indent=4)


def add_movie(movies,title,genre,duration,year,ratings):
    movie={
        "id":len(movies)+1,
        "title": title,
        "genre": genre,
        "duration": duration,
        "year": year,
        "ratings": ratings
    }
    movies.append(movie)
    print(f"{title} added successfully")

def movie_exist(movies,title):
    search_movie = title.lower().strip()
    for m in movies:
        if m['title'].lower().strip() == search_movie:
            return True
    return False


def update_movie(movies,title, new_title, new_genre, new_duration, new_year, new_ratings):
    found = False
    search_movie = title.lower().strip()

    for m in movies:
        if m['title'].lower().strip() == search_movie:
            if new_title        : m['title'] = new_title
            elif new_genre      : m['genre']=new_genre
            elif new_duration   : m['duration']=new_duration
            elif new_year       : m['year']=new_year
            elif new_ratings    : m['ratings']=new_ratings

            print("---Book updated successfully!---")
            print(f"Movie title  : {m['title']}")
            print(f"Genre        : {m['genre']}")
            print(f"Duration     : {m['duration']}")
            print(f"Year         : {m['year']}")
            print(f"Ratings      : {m['ratings']}\n")
            found=True
            break

    if not found:
        print(f"{title} not found")

def display_movie(movies):
    if not movies:
        print("No movies available")

    for m in movies:
        print("\n-----------All movies-----------\n")
        print(f"Movie title :{m['title']}")
        print(f"Genre       : {m['genre']}")
        print(f"Duration    : {m['duration']}")
        print(f"Year        : {m['year']}")
        print(f"Ratings     : {m['ratings']}")
        print("\n------------------------------\n")

def delete_movie(movies,title):
    found = False
    del_movie = title.lower().strip()

    for m in movies:
        if m['title'].lower().strip() == del_movie:
            movies.remove(m)
            print(f"{title} deleted successfully")
            found = True
            break
    if not found:
        print(f"{title} not found")

def search_movie(movies,title):
    found = False
    search_movie = title.lower().strip()

    for m in movies:
        if m['title'].lower().strip() == search_movie:
            print("\n-----------All movies----------\n")
            print(f"Movie title :{m['title']}")
            print(f"Genre : {m['genre']}")
            print(f"Duration : {m['duration']}")
            print(f"Year : {m['year']}")
            print(f"Ratings : {m['ratings']}")
            print("\n------------------------------\n")
            found=True
            break
    if not found:
        print(f"{title} not found")