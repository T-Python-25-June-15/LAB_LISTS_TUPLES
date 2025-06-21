#List of movies, where each movie is represented as (title,relase year,ratings).
movies = [
    ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1])
]

#List to store movies that have arerge rate > 6.
movies_rate =[]
# Calculate the average rateing
for title,year,rating in movies:
    average_rate = sum(rating) / len(rating)

    if average_rate > 6:
       movies_rate.append((title,year,round(average_rate,2)))

# Sort list of movies ba average rating in descinding order .      
movies_rate.sort(key=lambda i: i[2], reverse=True)

# Display the results.
for i,(title,year,average_rate) in enumerate(movies_rate, start=1):
    print(f"{i}. {title} ({year}) - Average rateing: {average_rate} ★" )


