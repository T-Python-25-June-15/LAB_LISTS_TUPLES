booked_seats = [(1, 5), (1, 6), (2, 10), (3, 7), (4, 15)]
def display_booked_seats():
    if not booked_seats:
        print("No seats are booked.")
    else:
        for seat in booked_seats:
            print(f"Row {seat[0]}, Seat {seat[1]}")
        print()

def check_availability():
    row = int(input("Enter row number (1-10): "))
    seat = int(input("Enter seat number (1-20): "))
    if (row, seat) in booked_seats:
        print("This seat is booked.")
    else:
        print("This seat is available.")

def add_booking():
    row = int(input("Enter row number (1-10): "))
    seat = int(input("Enter seat number (1-20): "))
    if (row, seat) in booked_seats:
        print("This seat is already booked.")
    else:
        booked_seats.append((row, seat))
        print("Booking successful.")

def cancel_booking():
    row = int(input("Enter row number (1-10): "))
    seat = int(input("Enter seat number (1-20): "))
    if (row, seat) in booked_seats:
        booked_seats.remove((row, seat))
        print("Booking cancelled.")
    else:
        print("Seat was not booked.")

def print_all_bookings():
    sorted_seats = sorted(booked_seats)
    if not sorted_seats:
        print("No seats are booked.")
    else:
        for seat in sorted_seats:
            print(f"Row {seat[0]}, Seat {seat[1]}")
        print()

def display_stats():
    print(f"Total booked seats: {len(booked_seats)}")
    row_counts = [0] * 10 
    for row, seat in booked_seats:
        row_counts[row - 1] += 1
    for i in range(len(row_counts)):
        count = row_counts[i]
        print(f"Row {i+1}: {count} seats booked")

def menu():
    print("\n -- Cinema Booking System -- ")
    print("1. Display all booked seats")
    print("2. Check seat availability")
    print("3. Add a booking")
    print("4. Cancel a booking")
    print("5. Print all booked seats ")
    print("6. Show info ")
    print("Type 'exit' to quit")

while True:
    menu()
    choice = input("Enter your choice: ")
    
    if choice == '1':
        display_booked_seats()
    elif choice == '2':
        check_availability()
    elif choice == '3':
        add_booking()
    elif choice == '4':
        cancel_booking()
    elif choice == '5':
        print_all_bookings()
    elif choice == '6':
        display_stats()
    elif choice == 'exit':
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please try again.")