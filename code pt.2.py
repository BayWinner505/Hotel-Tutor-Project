import csv
def exit():
    print("Exiting the program.")
    quit()
def menu():
    choice = input("Choose an option:\n1. Guest Details\n2. Hotel Room Details\n3. Bookings\n4. Billing & Payments\n5. Record Keeping\n6. Exit\n")
    if choice == "1":
        guest_details()
    elif choice == "2":
        hotel_room_details()
    elif choice == "3":
        bookings()
    elif choice == "4":
        billing_payments()
    elif choice == "5":
        record_keeping()
    elif choice == "6":
        exit()  
    else:
        print("Invalid choice. Please try again.")
        menu()

def guest_details():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    found = False
    with open("guest.csv", 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            if row[0] == first_name and row[1] == last_name:
                found = True
                print("Guest found.")
                print("Bookings:")
                print("-------------")
                for booking in row[2:]:
                    print(booking)
                print("-------------")
                print("You are now getting taken to the Main Menu")
                menu()
    if not found:
        print("Guest not found.")
        print("You are now getting taken to the Main Menu")
        menu()
def hotel_room_details():
    room = int(input("What room would you like to see details for?\n 1.Standard Room\n 2.Moderate Room\n 3.Deluxe Room\n 4.Suite\n 5. Main Menu \nWhat room would you like to see details for? "))
    if room == 1 :
        print(" It is a type of single room, which allows for 1 person to stay in the room. It is available for 1 night and costs £50 per night.")
    elif room == 2 :
        print("It is a moderate room which allows for 2 people to stay in the room. It is available for 1 night and costs £55 per night.")
    elif room == 3:
        print("This is a deluxe room which allows for 3 people to stay in the room. It is available for 1 night and costs £65 per night.")
    elif room == 4 :
        print("The is a suite room which allows for 4 people to stay in the room. It is available for 1 night and costs £100 per night.")
    elif room == 5 :
        print("You are now exiting to the main menu")
        menu()

def bookings():
    fname = input("Enter your First name: ")
    lname = input("Enter your Last name: ")
    room_type = input("Enter the room type booked: ")
    people = int(input("Enter the number of people staying: "))
    with open("guest.csv", mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([fname, lname, room_type, people])
        print("Personal details saved successfully.")
        print("You are now exiting to the main menu")
        menu()

def billing_payments():
    fname = input("Enter your First name: ")
    lname = input("Enter your Last name: ")
    room_cost = float(input("Enter the cost of the room per night: "))
    days_staying = int(input("Enter the number of days staying: "))
    total_room_cost = room_cost * days_staying
    print(f"Total room cost: £{total_room_cost}")
    services_cost = float(input("Enter the total cost of additional services: "))
    total_cost = total_room_cost + services_cost
    print(f"Total cost including services: £{total_cost}")
    payment = float(input("Enter payment amount: £"))
    if payment >= total_cost:
        change = payment - total_cost
        print(f"Payment successful. Change: £{change}")
        print("You are now exiting to the main menu")
        menu()
    else:
        print("Insufficient payment. Please provide more funds.")
        print("You are now exiting to the main menu")
        menu()

def record_keeping():
    with open("guest.csv", 'r') as file:
        csv_reader = csv.reader(file)
        print("Guest Records:")
        print("--------------")
        for row in csv_reader:
            print("Name:", row[0], row[1])
            print("Room Type:", row[2])
            print("Number of People:", row[3])
            print("--------------")
            print("You are now exiting to the main menu")
        menu()


menu()
