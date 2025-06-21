movies = [
    ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1])
]

def caluclate_movie_average_rating(ratings = []):
    if not ratings:
        return 0
    return sum(ratings) / len(ratings)



sorted_movie = []
for movie in movies:
    average_rating = caluclate_movie_average_rating(movie[2])
    sorted_movie.append((movie[0], movie[1], average_rating))

sorted_movie.sort(reverse=True)

print('==========================Movies List:==========================')
index = 1
for movie in sorted_movie:
    if movie[2] > 6:
        print(f"{index}. {movie[0]} ({movie[1]}) - Average Rating: {movie[2]:.2f} ★")
        index+= 1
print('==================================================================')