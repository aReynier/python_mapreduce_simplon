import csv

# The goal of map reduce is to:
# have total view number per movie
def film_count():
    main()

def main():
    logs = 'logs_cinestream.csv'

    with open(logs, newline='') as file:
        rows = csv.DictReader(file)
        film_list = []
        for row in rows:
                film_list.append(map_fn(row))
    sorted_data = shuffle_fn(film_list)
    
    reduce_fn(sorted_data)


def map_fn(data):
    mapped_films = (data["film_title"], 1)

    return mapped_films


def shuffle_fn(data):
    shuffled_films = {}

    for value in data:
        if value[0] not in shuffled_films:
             shuffled_films[value[0]] = []
        shuffled_films[value[0]].append(value[1])

    return shuffled_films


def reduce_fn(data):
    for value in data:
        data[value] = sum(data[value])
    print(data)
film_count()
