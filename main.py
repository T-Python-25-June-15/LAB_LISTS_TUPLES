
# Define list of bookd seat repesented as tuples (row,seat).
booked_seats = [(1, 5), (1, 6), (2, 10), (3, 7), (4, 15)]

# Display all booked seats.
def display_seats():
    """
    Displays all currently booked seats

    Parameters:
        None

    Returns:
        None
    """
    print("booked seats :")
    for i in booked_seats:
        print(f"Row {i[0]}, Seat {i[1]}")

# Check availability.
def cheak_seats():
    """
    Checks whether a seat is available or already booked.

    Parameters:
        None

    Returns:
        None
    """

    row = int(input("Enter number of row : "))
    seat = int(input("Enter number of seat : "))

    if (row, seat) in booked_seats:
        print("The seat is reserved!")
    else:
        print("The seat is available!")
        answer=str(input("Do you want to book it ? 'yes or no'"))
        if answer == "yes":
           booked_seats.append((row,seat))
           print("Seat booked successfully.")
        else:
           print(" ")
           


# Add seats by user. 
def add_seats():
    """
    Add a booking to the booked_seats list.
    If the seat is available, it is added to the booking list.
    If the seat is already booked, a message is printed.

    Parameters:
        None

    Returns:
        None
    """
    row = int(input("Enter number of row : "))
    seat = int(input("Enter number of seat : "))

    if (row, seat) in booked_seats:
           print("Seat is alredy booked.")
    else:
        booked_seats.append((row,seat))
        print("Seat booked successfully.")

# Cancel a booking.
def cancel_book():
   """
    Cancels a booking by removing the seat from the booked_seats list.
    If the seat is found, it is removed. If not, a message is shown.

    Parameters:
        None

    Returns:
        None
   """
   
   row = int(input("Enter number of row : "))
   seat = int(input("Enter number of seat : "))

   if (row, seat) in booked_seats:
        booked_seats.remove((row,seat))
        print("Booking is canclled.")
   else:
       print("This seat not booked")


# Display all booked list sorted by row.
def display_sorted():
    """
    Displays all booked seats sorted by row number and then seat number.

    Parameters:
        None

    Returns:
        None
    """
    sorted_seat= sorted(booked_seats) 
    print("Sorted booking:")
    for row,seat in sorted_seat:
        print(f"Row{row}, Seat{seat}")


# display total number of booked seat and show list of numbers booked seats in each row. 
def show_statistics():
    """
    Displays total number of booked seats and the number of booked seats per row.

    Parameters:
        None

    Returns:
        None
    """
    total = len(booked_seats)
    print("The total numbers of booked seats :",total)
    print("List of booked steats in each row:")

    row_count = [0] * 10
    for row,seat in booked_seats:
        row_count[row - 1] += 1 

    for i in range(10):
        print(f"Row {i+1}| {row_count[i]} seats booked")

# display map of booked seats for each row .
def display_map(booked_seats, total_rows=10, seats_row=20):
    """
    Displays a seating map for the cinema.
    Booked seats are shown with 'X'.
    Available seats are shown with 'O'.

    Parameters:
        booked_seats (list of tuples): List of booked seats in (row, seat).
        total_rows (int): Total number of rows in the cinema (default = 10).
        seats_row (int): Number of seats in each row (default = 20).

    Returns:
        None 
    """
    seats = "     " + " ".join([str(i).rjust(2) for i in range(1, seats_row + 1)])
    print(seats)

    # Print each row with seat status.
    for row in range(1, total_rows + 1):
        row_display = []
        for seat in range(1, seats_row + 1):
            if (row, seat) in booked_seats:
                row_display.append("X")
            else:
                row_display.append("O")
        print(f"Row {str(row).rjust(2)}: " + " ".join(row_display))

# loop to repeat the menu.
while True:
    # Display the menu.
    print("-" * 26)
    print("      Cinema Booking")
    print("-" * 26)
    print("========== MENU ===========")
    print("1. Show booked seats.")
    print("2. Check seat availability.")
    print("3. Add booking.")
    print("4. Cancel a booking.")
    print("5. show sorted booked.")
    print("6. show statistics.")
    print("7. show map of sorted booked.")
    print("Type 'exit' to quit.")

    user_choice=input("Enter your chioce: ")
    # Menu options handling based on user input.
    if user_choice == "1":
        display_seats()
    elif user_choice == "2":
        cheak_seats()
    elif user_choice =="3":
        add_seats()
    elif user_choice == "4":
        cancel_book()
    elif user_choice == "5":
        display_sorted()
    elif user_choice == "6": 
        show_statistics()
    elif user_choice == "7": 
        display_map(booked_seats)
    elif user_choice == "exit":
        print("Exiting..")
        break
    else:
        print("Invalid choice. Try again.")


