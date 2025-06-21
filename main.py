


booked_seats = [(1, 5), (4, 15) , (2, 10), (3, 7), (1, 6)]

# Function to check if a given row and seat are within valid cinema range
def check_range(row,seatNum):

    if 10 >= row >= 1 and 20 >= seatNum >= 1:  
       return True

    else:
        return False
    
def Display_booked_seats():
    for seat in booked_seats:
        print(f"Row {seat[0]}, Seat {seat[1]}")


def check_availability(row: int, seatNum: int):
    seat = (row,seatNum)
    if seat in booked_seats:
        return True # Return True if seat is booked, else False
    else:
        return False
   


def add_booking(row: int, seatNum: int):
    seat = (row,seatNum)

    if not check_availability(row, seatNum): # Check if seat is free
        booked_seats.append(seat)
        print("Your seat has been successfully booked.")
    else:
        print("ERROR: seat is not available") # Seat already booked

    


def cancel_booking(row: int, seatNum: int):
    seat = (row, seatNum)
    
    if check_availability(row, seatNum):
        booked_seats.remove(seat) 
        print("Your seat has been successfully removed.")

    else:
        print("ERROR: the seat is not exist")

 


def sorted_seats(): 

    sorted_seats = sorted(booked_seats)

    for row, seat in sorted_seats:
        print(f"Row {row}, Seat {seat}")



def num_of_seats_per_row():
    # Number of seats booked per row (rows 1 to 10)
    booked_per_row = [0] * 10  # Index 0 → Row 1, Index 9 → Row 10

    for row, seat in booked_seats:
        if 1<= row <= 10: 
            booked_per_row[row - 1] += 1

    print("Number of booked seats per row (rows 1 to 10):")
    for i, count in enumerate(booked_per_row): # Use enumerate to get both the index (i) and the count of booked seats in each row.
        print(f"Row {i + 1}: {count}")


# Function to print the menu options to the user
def print_menu():
    print("1. Display all booked seats")
    print("2. Check availability")
    print("3. Add a booking")
    print("4. Cancel a booking")
    print("5. Print all booked seats, sorted by row and then seat")
    print("6. Total number of booked seats")
    print("7. Number of seats booked per row")
    print("0. to exit")

print_menu()

choice = input("Enter your choice (1 to 7), or 0 to exit: ")
while choice != "0":
    match choice:
        case "1":
            Display_booked_seats()
        case "2":
            row = int(input("Enter row number (1 to 10): "))
            seat = int(input("Enter seat number (1 to 20): "))
            if check_range(row, seat):
                if check_availability(row, seat):
                    print("seat is booked")
                else:
                    print("seat is available")
            else:
                print("ERROR: Your row number or seat number out of range.")
        case "3":
            row = int(input("Enter row number to book (1 to 10): "))
            seat = int(input("Enter seat number to book (1 to 20): "))
            if check_range(row, seat):
                add_booking(row,seat)
            else:
                print("ERROR: Your row number or seat number out of range.")
        case "4":
            row = int(input("Enter row number to remove (1 to 10): "))
            seat = int(input("Enter seat number to remove (1 to 20): "))
            if check_range(row, seat):
                cancel_booking(row,seat)
            else:
                print("ERROR: Your row number or seat number out of range.")
        case "5":
            sorted_seats()
        
        case "6":
            print("Total number of booked seats:",len(booked_seats))
        case "7":
            num_of_seats_per_row()
        case "0":
            break

    print("-"*25)
    print_menu()

    choice = input("Enter your choice (1 to 7), or 0 to exit: ")
