#lab list and tuples (wasan alqahtani)

#define a list of booking that contains booked seat tupels
booked_seats = [(1, 5), (1, 6), (2, 10), (3, 7), (4, 15)]

#function to take input from the user (row and seat)
def take_input():
      '''this function used to take input from the user and return the row and seat number that the user enter'''
      row = int(input("please enter row number (1 to 10): "))
      seat = int(input("please enter seat number (1 to 20): "))
      #if the user enter wrong number 
      while not (1 <= row <= 10 and 1 <= seat <= 20):
        print("wrong input try again")
        row = int(input("please enter row number (1 to 10): "))
        seat = int(input("please enter seaat number (1 to 20): "))

      return row, seat

#sort the list based on number of row 
def sort_bookings()->list:
    '''this function sort the list by row '''
    sorted_booking = sorted(booked_seats)
    return sorted_booking

#function to display all booked deats 
def Display_Allseats():
    '''this funstion used to print all the booked seat '''
    print ("\nBooked seats ")
    print("-"*40)
    #call sort function to sort the booked based on rows 
    sorted_booking = sort_bookings()
    #display all booked seats 
    for row, seat in sorted_booking:
        print (f"Row {row} , Seat {seat} ")

#function to check the availability
def check_availability(row,seat)->bool:
     '''this function used to check the availability of seat, its take row and seat number that the user enter and then return true if 
     its available and return false if its not'''
     #checkif the row and seat in the list or not
     if (row, seat) in booked_seats:
         return False
     else:
         return True

#function to add the book (row , seat) 
def add_booking(row,seat):
    '''this function takes row and seat number and add the seat that the user want but first 
    its will check the availability of the seat and added it to the list'''
    #call check the availability function before adding the booking 
    if check_availability(row,seat):
        #add the row and seat to the list 
        booked_seats.append((row,seat))
        print("your booked has been done successfully")
    else:
        print("this seat is already taken")

#function to cancle the booking
def cancle_booking(row,seat):
    '''this function takes row and seat that the user enter and then cancle it if its in the list 
    (by calling  check_availability function)'''
    #call check the availability function before cancle the booking 
    if not check_availability(row,seat):
        booked_seats.remove((row,seat))
        print("your cancelation hav been done successfully")
    else:
        print("there is no booked in this number of seat")


#function to count total number of booking and number of seats in each row 
def statistics_seat():
    '''this function print the total numbers of bookings and print total number of seats in each row '''
    # count the total number of booking by calling len 
    total_seats= len(booked_seats)
    print(f"\ntotal number of booked seats: {total_seats}\n")
    #creat a list of counts for each row index 0–9
    seats_perrow = [0,0,0,0,0,0,0,0,0,0]
    #count number of seats in each row 
    for row, seat in booked_seats:
        seats_perrow[row - 1] += 1
    # print the row number and total number of seats in each row 
    for elements in range(len(seats_perrow)):
        print(f"the row {elements+1} has {seats_perrow[elements]} seats")

#use loop to display the menue until the user enter 6 to exit 
while True:
    print ("\nWelcome To The Cinema Booking Program ")
    print("-"*40)
    print("1. Display all booked seats (sorted)")
    print("2. Check availability")
    print("3. Add a booking")
    print("4. Cancle a booking")
    print("5. Display Booked Seats in details (total number of seats and number of seats in each row)")
    print("6. Exit")
    print("-"*40)
    option= input("please enter a number from the list below: ")
    # use match and each case ( depend in what user enter ) called its function. 
    match option:
        case "1":
           Display_Allseats() 

        case "2":
           print ("\n Check Availability")
           print("-"*40)
           row, seat = take_input()
           if check_availability(row,seat):
               print("this set is available ")
           else:
             print("sorry, this seat is already taken ")

        case "3":
            print ("\n Add New Booking: ")
            print("-"*40)
            row, seat = take_input()
            add_booking(row,seat)
        case "4":
            print ("\n Cancle Booking: ")
            print("-"*40)
            print("choose which one you want to cancle")
            row, seat = take_input()
            cancle_booking(row,seat)

        case "5":
            print ("\n Statistics Of Bookings: ")
            print("-"*40)
            statistics_seat()

        case "6":
            #exit the loop and end the program 
            break      

        case _:
            # if the user enter wrong number 
            print("\n wrong number please try again \n")
