message = "\nwelcome to seat booking system\n"
message+= '-'*15
message+='\n enter one of the following \n'
message+='\nchoose "exit" to exit\n'
message+='1. display all booked seats\n'
message+='2. check avaliability \n'
message+='3. Add a booking\n'
message+='4. Cancel a booking\n'
message+='5.Print all booked seats\n'
message+='6.simple summary\n'

seats = list(())





promot = input(message)
while promot != 'exit':
    if promot == '1':
        for i in seats:
            print(f"Row {i[0]}, Seat {i[1]}")
        if not seats:
            print("No seats are booked.")
    elif promot == '2':
        row = input("Enter row number: ")
        seat = input("Enter seat number: ")
        if(row == '' or seat == ''):
            print("please enter valid row and seat")
            continue
        if(row.isdigit() == False or seat.isdigit() == False):
            print("please enter valid row and seat")
            continue

        if (row, seat) in seats:
            print(f"Row {row}, Seat {seat} is booked.")
        else:
            print(f"Row {row}, Seat {seat} is available.")
    elif promot == '3':
        row = input("Enter row number: ")
        seat = input("Enter seat number: ")
        if(row == '' or seat == ''):
            print("please enter valid row and seat")
            continue
        if(row.isdigit() == False or seat.isdigit() == False):
            print("please enter valid row and seat")
            continue
        seats.append((row, seat))
        print(f"Seat booked at Row {row}, Seat number {seat}")
    elif promot == '4':
        row = input("Enter row number to cancel: ")
        seat = input("Enter seat number to cancel: ")
        if(row == '' or seat == ''):
            print("please enter valid row and seat")
            continue
        if(row.isdigit() == False or seat.isdigit() == False):
            print("please enter valid row and seat")
            continue

        if (row, seat) in seats:
            seats.remove((row, seat))
            print(f"Booking canceled for row {row} and seat {seat}")
        else:
            print("no booking for provided row and seat")
    elif promot == '5':
        if seats:
            print("list of booked seats:")
            for i in seats:
                print(f"Row {i[0]}, Seat {i[1]}")
        else:
            print("no seats are booked.")

    elif promot == '6':
        print(f"Total number of booked seats: {len(seats)}")
        row_counts = [0,0,0,0,0,0,0,0,0,0]

        for row, seat in seats:
            row_counts[int(row)] += 1


        print("\nNumber of seats booked per row: ")
        for i in range(0,len(row_counts)):
            print(f"row {i}: {row_counts[i]} seats are booked")


    else:
        print("invalid option, try again")
    promot = input(message)
    
