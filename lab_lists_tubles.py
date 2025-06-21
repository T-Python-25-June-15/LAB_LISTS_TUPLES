booked_seats = [(1, 5), (1, 6), (2, 10), (3, 7), (4, 15)]

while True:
    print("\n--- CINEMA BOOKING SYSTEM ---")
    print("1. Show all booked seats")
    print("2. Check if seat is available")
    print("3. Book a seat")
    print("4. Cancel booking")
    print("5. Show sorted seats")
    print("6. Show statistics")
    print("Type 'exit' to quit")
    
    choice = input("\nWhat do you want to do? ")
    
    if choice == 'exit':
        print("Goodbye!")
        break
    
    elif choice == '1':
        # Display all booked seats
        print("\nBooked seats:")
        for row, seat in booked_seats:
            print(f"Row {row}, Seat {seat}")
    
    elif choice == '2':
        # Check availability
        row = int(input("Enter row (1-10): "))
        seat = int(input("Enter seat (1-20): "))
        
        if (row, seat) in booked_seats:
            print(f"Row {row}, Seat {seat} is BOOKED")
        else:
            print(f"Row {row}, Seat {seat} is AVAILABLE")
    
    elif choice == '3':
        # Add booking
        row = int(input("Enter row (1-10): "))
        seat = int(input("Enter seat (1-20): "))
        
        if (row, seat) in booked_seats:
            print("Sorry, this seat is already booked!")
        else:
            booked_seats.append((row, seat))
            print(f"Booked Row {row}, Seat {seat}")
    
    elif choice == '4':
        row = int(input("Enter row to cancel (1-10): "))
        seat = int(input("Enter seat to cancel (1-20): "))
        
        if (row, seat) in booked_seats:
            booked_seats.remove((row, seat))
            print(f"Cancelled Row {row}, Seat {seat}")
        else:
            print("This seat was not booked")
    
    elif choice == '5':
        sorted_seats = sorted(booked_seats)
        print("\nSorted booked seats:")
        for row, seat in sorted_seats:
            print(f"Row {row}, Seat {seat}")
    
    elif choice == '6':
        total = len(booked_seats)
        print(f"\nTotal booked seats: {total}")
        
        row_counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] 
        for row, seat in booked_seats:
            row_counts[row - 1] += 1
        
        print("Seats per row:")
        for i in range(10):
            print(f"Row {i + 1}: {row_counts[i]} seats")
    
    else:
        print("Invalid choice! Try again.")
    
    input("\nPress Enter to continue...")