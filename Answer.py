booked_seats = [(1, 5), (1, 6), (2, 10), (3, 7), (4, 15)]

def Display_all_booked_seats():
    print()
    print("-"*15)
    print("These are the booked seats:")
    for seats in booked_seats:
            print(f"Row {seats[0]}, Seat {seats[1]}")
    print("-"*15)

def Check_availability():
    print()
    print("-"*15)
    print("To check if the seat you want is availabiliy please do the following:")
    User_Row = int(input("Enter the row numbers to check if it booked or Available: "))
    User_Seat = int(input("Enter the seat numbers to check if it booked or Available: "))
    checking = (User_Row , User_Seat)
    print(checking)
    if checking in booked_seats:
        print("The row and seat you choose is booked")
    else:
        print("The row and seat you choose is Available")
    print("-"*15)


def Add_a_booking():
    print()
    print("-"*15)
    global booked_seats
    Add_booking_user_row = abs(int(input("Enter the row you want to seat at, Remember the rows are from 1 to 20: ")))
    Add_booking_user_seat = abs(int(input("Enter the seat number that you want to seat at, Remember the seats numbers are from 1 to 20: ")))
    checking = (Add_booking_user_row , Add_booking_user_seat)
    if Add_booking_user_row > 20 or Add_booking_user_seat > 20:
        print("The seats and rows are from 1 to 20")
    elif checking in booked_seats:
        print("The row and seat you choose is already booked")
    else:
        booked_seats.append(checking)
        print(f"Thank you are booking at Vox Cinema \n your row is {Add_booking_user_row} seat number {Add_booking_user_seat}")
        print("-"*15)
         
def Cancel_a_booking():
    print()
    print("-"*15)
    print("To cancel a booking please do the following:")
    cancel_booking_user_row = abs(int(input("Enter the row, Remember the rows are from 1 to 20: ")))
    cancel_booking_user_seat = abs(int(input("Enter the seat number, Remember the seats numbers are from 1 to 20: ")))
    checking = (cancel_booking_user_row , cancel_booking_user_seat)
    if cancel_booking_user_row > 20 or cancel_booking_user_seat > 20:
        print("The seats and rows are from 1 to 20")
    elif checking not in booked_seats:
        print("The row and seat you just typed isn't booked")
    else:
        index_of_seat = booked_seats.index(checking)
        del booked_seats[index_of_seat]
        print(f"You canceled the booking of row {cancel_booking_user_row} and seat number {cancel_booking_user_seat}")
    print("-"*15)



def Print_all_booked_seats():
    print()
    print("-"*15)
    print(sorted(booked_seats))
    print("-"*15)
         

def Calculate_and_display():
    print()
    print("-"*15)
    print(f"The total number of booked seat is {len(booked_seats)}")
    row_count = [0] * 20
    for row,seat in booked_seats:
        if 1 <= row <= 20:
            row_count[row-1] +=1
    print("Number of seats booked per row (row index 1 - 20):")
    for index, count in enumerate(row_count):
        print(f"Row {index + 1}: {count} seats booked")
    print("-"*15)

#I added this : it would show you the seat that is available or taken per a row as a map
def view_seat_map():
    print()
    print("="*50)
    print(" "*20 + "Screen")
    print("="*50)
    for row in range(1, 21):
        seat_row = ""
        for seat in range(1, 21):
            if(row, seat) in booked_seats:
                seat_row +="X "
            else:
                seat_row +="O "
        print(f"Row {str(row).rjust(2)}: {seat_row}")
    print("="*50)
    print("Just so you know: O = Available, X = Booked")
    print("="*50)


User_Choose = input("Welcome to Vox Cinema \n 1) Display all booked seats \n 2)Check availability \n 3)Add a booking \n 4)Cancel a booking type  \n 5)Print all booked seats \n 6)Calculate and display \n 7)View seat map \n Please choose what you want to do: ").lower()

while User_Choose != "exit":
    if User_Choose == "1":
        Display_all_booked_seats()
        print()
        User_Choose = input("Welcome to Vox Cinema \n 1) Display all booked seats \n 2)Check availability \n 3)Add a booking \n 4)Cancel a booking type  \n 5)Print all booked seats \n 6)Calculate and display \n 7)View seat map \n Please choose what you want to do: ").lower()
    elif User_Choose == "2":
        Check_availability()
        print()
        User_Choose = input("Welcome to Vox Cinema \n 1) Display all booked seats \n 2)Check availability \n 3)Add a booking \n 4)Cancel a booking type  \n 5)Print all booked seats \n 6)Calculate and display \n 7)View seat map \n Please choose what you want to do: ").lower()
    elif User_Choose == "3":
        Add_a_booking()
        print()
        User_Choose = input("Welcome to Vox Cinema \n 1) Display all booked seats \n 2)Check availability \n 3)Add a booking \n 4)Cancel a booking type  \n 5)Print all booked seats \n 6)Calculate and display \n 7)View seat map \n Please choose what you want to do: ").lower()
    elif User_Choose == "4":
        Cancel_a_booking()
        print()
        User_Choose = input("Welcome to Vox Cinema \n 1) Display all booked seats \n 2)Check availability \n 3)Add a booking \n 4)Cancel a booking type  \n 5)Print all booked seats \n 6)Calculate and display \n 7)View seat map \n Please choose what you want to do: ").lower()
    elif User_Choose == "5":
        Print_all_booked_seats()
        print()
        User_Choose = input("Welcome to Vox Cinema \n 1) Display all booked seats \n 2)Check availability \n 3)Add a booking \n 4)Cancel a booking type  \n 5)Print all booked seats \n 6)Calculate and display \n 7)View seat map \n Please choose what you want to do: ").lower()
    elif User_Choose == "6":
        Calculate_and_display()
        print()
        User_Choose = input("Welcome to Vox Cinema \n 1) Display all booked seats \n 2)Check availability \n 3)Add a booking \n 4)Cancel a booking type  \n 5)Print all booked seats \n 6)Calculate and display \n 7)View seat map \n Please choose what you want to do: ").lower()
    elif User_Choose == "7":
        view_seat_map()
        print()
        User_Choose = input("Welcome to Vox Cinema \n 1) Display all booked seats \n 2)Check availability \n 3)Add a booking \n 4)Cancel a booking type  \n 5)Print all booked seats \n 6)Calculate and display \n 7)View seat map \n Please choose what you want to do: ").lower()
    else:
        print()
        print("Wrong input, Please choose the number of the function that you want to do")
        User_Choose = input("Welcome to Vox Cinema \n 1) Display all booked seats \n 2)Check availability \n 3)Add a booking \n 4)Cancel a booking type  \n 5)Print all booked seats \n 6)Calculate and display \n 7)View seat map \n Please choose what you want to do: ").lower()

