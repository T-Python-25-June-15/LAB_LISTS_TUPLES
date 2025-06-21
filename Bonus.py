# Movie Ratings Analysis
# Student: Hassan Abdullah Alseny
# Description:
# Calculate average ratings for movies,
# filter out low-rated ones, and display sorted results.

# Initial list of movies: (title, year, list of ratings)
movies = [
    ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1])
]


def calculateAverage(ratings):
    """
    Calculate the average of a list of ratings.
    Returns a float rounded to 2 decimal places.
    """
    total = 0
    for r in ratings:
        total = total + r

    count = len(ratings)
    average = total / count

    return round(average, 2)


def getMoviesWithAverage(movies_list):
    """
    Build a new list with (title, year, average) for each movie.
    """
    result = []

    for movie in movies_list:
        title = movie[0]
        year = movie[1]
        ratings = movie[2]

        avg = calculateAverage(ratings)

        result.append((title, year, avg))

    return result


def filterMovies(movies_list):
    """
    Filter movies with average rating >= 6.0
    """
    filtered = []

    for movie in movies_list:
        if movie[2] >= 6.0:
            filtered.append(movie)

    return filtered


def getAverageKey(movie):
    """
    Helper function to return the average rating from a movie tuple.
    """
    return movie[2]


def displayMovies(movies_list):
    """
    Display movies with numbering, title, year, and average rating.
    """
    if movies_list:
        print("\n--- Movie Ratings ---")

        index = 1

        for movie in movies_list:
            print(f"{index}. {movie[0]} ({movie[1]}) - Average rating: {movie[2]} ★")
            index = index + 1

    else:
        print("\nNo movies to display.")




movies_with_avg = getMoviesWithAverage(movies)

filtered_movies = filterMovies(movies_with_avg)

sorted_movies_ascending = sorted(filtered_movies, key=getAverageKey)

sorted_movies = sorted_movies_ascending[::-1]


displayMovies(sorted_movies)
