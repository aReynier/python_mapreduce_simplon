import csv
logs = 'logs_cinestream.csv'


# The goal of map reduce is to:
# have total view number per movie
def film_count():
    sorted_film = shuffle_fn(map_fn())
    reduce_fn(sorted_film)

def map_fn():
    with open('logs_cinestream.csv', newline='') as file:
        rows = csv.DictReader(file)
        film_list = []
        for row in rows:
                film_list.append(row['film_title'])
    return film_list

def shuffle_fn(film_list):
    film_list.sort()
    return film_list

def reduce_fn(film_list_sorted):
    unique_films_list = list(set(film_list_sorted))
    films_count = []
    for unique_film_list in unique_films_list:
         count = film_list_sorted.count(unique_film_list)
         films_count.append([unique_film_list, count])
    print(films_count)
film_count()


def genre_duration():
    # sorted_film = shuffle_fn(map_fn())
    # reduce_fn(sorted_film)
    map_fn()

def map_fn():
    with open('logs_cinestream.csv', newline='') as file:
        rows = csv.DictReader(file)
        film_list = []
        for row in rows:
                film_list.append([row['genre'], row['duree_visionnee_sec']])
    return film_list

def shuffle_fn(film_list):
    film_list.sort()
    print(film_list)
    return film_list

# def reduce_fn(film_list_sorted):
#     film_list_sorted
#     unique_films_list = list(set(film_list_sorted))
#     films_count = []
#     for unique_film_list in unique_films_list:
#          count = film_list_sorted.count(unique_film_list)
#          films_count.append([unique_film_list, count])
#     print(films_count)

genre_duration()


