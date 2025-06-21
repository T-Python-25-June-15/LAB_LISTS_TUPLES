# bonus lab wasan alqahtani 


#create function to sort the movie by rating
def sort_movies(average_movie):
    '''this function take an arguent of list and then sort the list based on greater averge '''
    arraylength= len(average_movie)
    for row in range(arraylength):
        for column in range(len(average_movie) - row - 1):
            if average_movie[column][2] < average_movie[column + 1][2]:
               # Swapping
                 average_movie[column], average_movie[column + 1] = average_movie[column + 1], average_movie[column]

# create list of movie and the list conatins a tuple of each movie 
movies = [
    ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1])
]

#create new list that have the movie name and the year and the average rate 
average_movie=list()
for rating in movies:
    therate = rating[2]
    average = round(sum(therate)/len(therate),2)
    average_movie.append((rating[0],rating[1],average,))

number:int = 0 
#call sorte_movie function to sort the list before printing 
sort_movies(average_movie)

#print the movies that the rate is above 6
for element in average_movie:
    #check if the rate is above 6
    if(element[2]>6):
       number += 1
       print(f"{number}. {element[0]} ({element[1]}) - Average rate: {element[2]} *")