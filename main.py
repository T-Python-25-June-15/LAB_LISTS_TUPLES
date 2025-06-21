booked_seats = [(1, 5), (1, 6), (2, 10), (3, 7), (4, 15)]

while True:
    print("\n--- Cinema Booking Menu ---")
    print("1. Display all booked seats")
    print("2. Check seat availability")
    print("3. Add a booking")
    print("4. Cancel a booking")
    print("5. Print sorted booked seats")
    print("6. Show statistics")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == "1":
        for seat in booked_seats:
            print(f"Row {seat[0]}, Seat {seat[1]}")

    elif choice == "2":
        row = int(input("Enter row number: "))
        seat = int(input("Enter seat number: "))
        if (row, seat) in booked_seats:
            print("Seat is booked.")
        else:
            print("Seat is available.")

    elif choice == "3":
        row = int(input("Enter row number: "))
        seat = int(input("Enter seat number: "))
        if (row, seat) in booked_seats:
            print("Seat already booked.")
        else:
            booked_seats.append((row, seat))
            print("Booking added.")

    elif choice == "4":
        row = int(input("Enter row number: "))
        seat = int(input("Enter seat number: "))
        if (row, seat) in booked_seats:
            booked_seats.remove((row, seat))
            print("Booking cancelled.")
        else:
            print("Seat not booked.")

    elif choice == "5":
        for seat in sorted(booked_seats):
            print(f"Row {seat[0]}, Seat {seat[1]}")

    elif choice == "6":
        print("Total booked seats:", len(booked_seats))
        row_counts = [0] * 10
        for seat in booked_seats:
            row_counts[seat[0] - 1] += 1
        for i in range(10):
            print(f"Row {i+1}: {row_counts[i]} seats booked")

    elif choice == "7" or choice.lower() == "exit":
        break

    else:
        print("Invalid choice.")
