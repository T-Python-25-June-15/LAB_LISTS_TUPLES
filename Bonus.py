movies = [
    ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1])
]


list_average_rate = []
for movie in movies:
    title = movie[0]
    year = movie[1]
    rating = movie[2]
    avg = round(sum(rating) / len(rating), 2)
    list_average_rate.append((title,year,avg))

filtered_movies = []
for movie in list_average_rate:
    if movie[2] > 6:
        filtered_movies.append(movie)


def get_average(movie_tuple):
    return movie_tuple[2]

filtered_movies.sort(key=get_average,reverse=True)

for index in range(len(filtered_movies)):
    title = filtered_movies[index][0]
    year = filtered_movies[index][1]
    avg = filtered_movies[index][2]
    print(f"{index + 1}. {title} ({year}) - Average rating: {avg} ★")
