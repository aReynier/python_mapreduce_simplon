import csv
logs = 'logs_cinestream.csv'


# The goal of map reduce is to:
# have total view lenght per genre
def genre_duration():
    sorted_film = shuffle_fn(map_fn())
    reduce_fn(sorted_film)

def map_fn():
    with open('logs_cinestream.csv', newline='') as file:
        rows = csv.DictReader(file)
        film_list = []
        for row in rows:
            film_list.append({'genre':row['genre'], 'duree_visionnee_sec':row['duree_visionnee_sec']})
    return film_list

def shuffle_fn(film_list):
    film_duration_sorted = sorted(film_list, key=lambda d: int(d['duree_visionnee_sec']))
    film_genre_sorted = sorted(film_duration_sorted, key=lambda d: d['genre'])
    return film_genre_sorted

def reduce_fn(films_list_sorted):
    genres = []
    for film_list_sorted in films_list_sorted:
        genres.append(film_list_sorted['genre'])
    unique_genres = list(set(genres))
    print(unique_genres)
    duration_per_genre = []
    for unique_genre in unique_genres:
        duration = 0
        for film_list_sorted in films_list_sorted:
            if (film_list_sorted['genre'] == unique_genre):
                duration += int(film_list_sorted['duree_visionnee_sec'])

        duration_per_genre.append([unique_genre, duration])
    print(duration_per_genre)
    

genre_duration()


