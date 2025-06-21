#1. List of movies 
movies:list = [ ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]), 
          ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]), 
          ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]), 
          ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]), 
          ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]), 
          ("The Room", 2003, [1, 2, 3, 4, 5, 1]) ]

#List to save average   
filterd_movies:list = list()

#2. Calculates the average rating for each movie
for movie in movies:
    sum = 0
    total = 0
    average = 0
    for rate in movie[2]:
        sum += rate
        total += 1
    average = round((sum / total),2)
    #3. Filters in movies with an average rating >= 6.0.
    if average >= 6.0:
        filterd_movies.append((movie[0],movie[1],average))

#4. Displays the movies
count = 0
sorted(filterd_movies[2])
for i in filterd_movies:
    count += 1
    print(f"{count}. {i[0]} ({i[1]}) - Avergae rating: {i[2]}")