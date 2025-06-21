# ============================================
# Cinema Booking Program
# Student: Hassan Abdullah Alseny
# Description:
#   A simple seat booking system using only lists and tuples.
#   Features:
#     - Display booked seats
#     - Check seat availability
#     - Add a booking
#     - Cancel a booking
#     - Display sorted booked seats
#     - Show booking statistics
#   Runs until the user types 'exit'.
# ============================================

booked_seats = [(1, 5), (1, 6), (2, 10), (3, 7), (4, 15)]


def displayBookedSeats():
    """
    Display all currently booked seats in the format:
    Row: X Seat: Y
    """
    if booked_seats:
        print("\n--- Booked Seats ---")
        
        for seat in booked_seats:
            print("Row:", seat[0], "Seat:", seat[1])
    else:
        print("\nNo seats booked yet.")


def checkAvailability():
    """
    Ask the user for a seat (row and seat number)
    and print if it is booked or available.
    """
    row, seat_num = getValidSeatInput()
    
    if (row, seat_num) in booked_seats:
        print(f"Row {row}, Seat {seat_num} is BOOKED.")
    else:
        print(f"Row {row}, Seat {seat_num} is AVAILABLE.")


def addBooking():
    """
    Ask the user for a seat (row and seat number)
    and add it to the booked list if it is not already booked.
    """
    row, seat_num = getValidSeatInput()
    
    if (row, seat_num) in booked_seats:
        print("Already booked.")
    else:
        booked_seats.append((row, seat_num))
        print("Seat booked.")


def cancelBooking():
    """
    Ask the user for a seat (row and seat number)
    and remove it from the booked list if it exists.
    """
    row, seat_num = getValidSeatInput()
    
    if (row, seat_num) in booked_seats:
        booked_seats.remove((row, seat_num))
        print("Booking cancelled.")
    else:
        print("That seat wasn't booked.")


def displaySortedSeats():
    """
    Display all booked seats sorted by row and then seat number.
    """
    if booked_seats:
        print("\n--- Sorted Booked Seats ---")
        sorted_seats = sorted(booked_seats)
        
        for seat in sorted_seats:
            print("Row:", seat[0], "Seat:", seat[1])
            
    else:
        print("\nNo seats booked yet.")


def showStatistics():
    """
    Calculate and display:
    - Total number of booked seats.
    - Number of seats booked per row (row 1 to 10).
    """
    total = len(booked_seats)
    print("\nTotal booked:", total)

    counts = [0] * 10
    for seat in booked_seats:
        counts[seat[0] - 1] = counts[seat[0] - 1] + 1

    i = 0
    while i < 10:
        print("Row", i + 1, ":", counts[i])
        i = i + 1


def getValidSeatInput():
    """
    Prompt the user to enter row and seat numbers.
    Validates that the input is a number and within the allowed range.
    Returns:
        tuple: (row, seat_num)
    """
    while True:
        row_input = input("Enter row (1-10): ").strip()
        seat_input = input("Enter seat (1-20): ").strip()

        if row_input.isdigit() and seat_input.isdigit():
            
            row = int(row_input)
            
            seat_num = int(seat_input)
            
            if 1 <= row <= 10 and 1 <= seat_num <= 20:
                return row, seat_num

        print("Invalid input, try again.")


# Main menu loop
while True:
    
    print("\n--- Cinema Booking ---")
    print("1. Display booked seats")
    print("2. Check availability")
    print("3. Add booking")
    print("4. Cancel booking")
    print("5. Display sorted seats")
    print("6. Show statistics")
    print("Type 'exit' to quit")

    choice = input("Your choice: ").strip().lower()

    if choice == "1":
        displayBookedSeats()

    elif choice == "2":
        checkAvailability()

    elif choice == "3":
        addBooking()

    elif choice == "4":
        cancelBooking()

    elif choice == "5":
        displaySortedSeats()

    elif choice == "6":
        showStatistics()

    elif choice == "exit":
        print("Bye!")
        break

    else:
        print("Invalid option.")
