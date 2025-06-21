MAX_ROWS:int = 10
MAX_SEATS:int  = 15
all_seats:list = list()
available_seats:list = list()
booked_seats:list = [(1,5), (1,6), (2,10), (3,7), (4,15)]
list_loop:bool =      True 
menu:str = f"""
1: Display all booked seats
2: Check availability
3: Add a booking
4: Cancel a booking
5: Display all booked seats (sorted)
6: Show statistics
7: exit"""

def createAllSeatsList():
    """Creates a list of all possible seats in the cinema (from row 1 to MAX_ROWS, and seat 1 to MAX_SEATS)."""
    for row in range(1,MAX_ROWS+1):                  
        for seat in range(1,MAX_SEATS+1):                
            all_seats.append((row,seat))

def createAvailableSeatsList():
    """Updates the available_seats list by excluding seats that are already booked."""
    available_seats.clear()
    for available_row in all_seats:        
        if available_row not in booked_seats:
            available_seats.append(available_row)

def displayBookedSeats():
    """Displays all currently booked seats in 'Row X, Seat Y' format."""
    print("\nAll Booked Seats:")    
    if len(booked_seats) > 0:        
        for seat in booked_seats:
            print(f"Row {seat[0]}, Seat {seat[1]}")
    else:
        print("No seats are booked.")

def checkAvailability(row:int, seat:int):
    """Checks whether a specific seat (row, seat) is booked or available."""
    if (row,seat) in booked_seats:
        print(f"Seat in Row {row}, Seat {seat} is BOOKED")
    elif (row,seat) in available_seats:        
        print(f"Seat in Row {row}, Seat {seat} is AVAILABLE")
    else:
        print("Invalid seat!")

def addBooking(row:int, seat:int):
    """Attempts to add a booking if the seat is available. Updates the availability list after booking."""
    if (row,seat) in available_seats:
        booked_seats.append((row,seat))
        print(f"Seat Row {row}, Seat {seat} booked successfully!")
        createAvailableSeatsList()
    elif (row,seat) in booked_seats:
        print(f"Seat in Row {row}, Seat {seat} is already booked.")
    else:
        print("Invalid seat!")

def cancelBooking(row:int, seat:int):
    """Cancels a booking if the seat is currently booked. Updates the availability list after cancellation."""
    if (row,seat) in booked_seats:
        booked_seats.remove((row,seat))
        createAvailableSeatsList()        
        print(f"Booking canceled for Row {row}, Seat {seat}.")    
    else:
        print("Seat is not currently booked.")

def displaySortedBookedSeats():
    """Displays all booked seats sorted by row and then seat number."""
    sortedSeats:list = sorted(booked_seats)
    if len(booked_seats) > 0:
        for seat in sortedSeats:
            print(f"Row {seat[0]}, Seat {seat[1]}")
    else:
        print("No seats are booked.")

def createStatistics():
    """Displays the total number of booked seats and the number of seats booked per row."""
    print(f"Total booked seats: {len(booked_seats)}")
    counts:list = [0] * MAX_ROWS
    for seat in booked_seats:
        row_index = seat[0] - 1
        counts[row_index] += 1
    print("Seats booked per row:")
    for i in range(MAX_ROWS):
        print(f"Row {i + 1}: {counts[i]}")

print(f"{40*"*"}\nWELCOME TO CINEMA BOOKING SYSTEM\n{40*"*"}")
createAllSeatsList()
createAvailableSeatsList()    

while list_loop:     
    choice = input(f"{menu} \nEnter your choice: ")
    match choice:
        case "1":
            displayBookedSeats()
        case "2":
            user_chosen_row =  int(input(f"Enter row number (1 - {MAX_ROWS}): Row "))
            user_chosen_seat =  int(input(f"Enter seat number (1 - {MAX_SEATS}): Seat "))
            checkAvailability(user_chosen_row,user_chosen_seat)
        case "3":
            user_chosen_row =  int(input(f"Enter row number (1 - {MAX_ROWS}): Row "))
            user_chosen_seat =  int(input(f"Enter seat number (1 - {MAX_SEATS}): Seat "))
            addBooking(user_chosen_row,user_chosen_seat)
        case "4":
            user_chosen_row =  int(input(f"Enter row number (1 - {MAX_ROWS}): Row "))
            user_chosen_seat =  int(input(f"Enter seat number (1 - {MAX_SEATS}): Seat "))
            cancelBooking(user_chosen_row,user_chosen_seat)
        case "5":
            displaySortedBookedSeats()
        case "6":
            createStatistics()
        case "exit" | "7":
            list_loop = False
            print("Thank you for using the Cinema Booking System!")
        case _:
            print("Invalid choice. Try again.")