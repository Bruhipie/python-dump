import random, time


##INITIALIZATION
balance=15000
flight_name=''
flights=[]
departure=str(input("\nYour departure point is: "))
arrival=str(input("Your arrival point is: "))


##GENERATION OF FLIGHT INFORMATION
for i in range(4):
    a=str(random.randint(0,1000))
    flight_name+=departure[0].upper()+arrival[0].upper()+a
    flights.append(flight_name)
    flight_name=''

route=departure+' to '+arrival
t=time.ctime()

flights_info = {
    flights[0]: {'route': route, 'departure_time': '08:00', 'arrival_time': '10:30', 'cost':3530},
    flights[1]: {'route': route, 'departure_time': '12:00', 'arrival_time': '14:30','cost':5170},
    flights[2]: {'route': route, 'departure_time': '15:30', 'arrival_time': '16:00','cost':7320},
    flights[3]: {'route': route, 'departure_time': '17:00', 'arrival_time': '19:30','cost':10190}
}


##BEAUTIFULLY PRINTING INFORMATION
print("\n{:<15} {:<25} {:<15} {:<15} {:<15}".format(
    "Flight Number", "Route", "Departure Time", "Arrival Time", "Cost"))
print("-" * 85)

for flight_code, info in flights_info.items():
    print("{:<15} {:<25} {:<15} {:<15} {:<15}".format(
        flight_code, info['route'], info['departure_time'], info['arrival_time'], "₹{:.2f}".format(info['cost'])))


##ACTUAL BOOKING STAGE
print("\nEnter the flight number you want to book: ", end='')
booking=input()
if booking not in flights:
    print("Enter valid flight number!")
    exit()
else:
    print("You have selected flight", booking)
    preference=input("Which seat would you prefer? (w=Window, a=Aisle, m=Middle Seat): ")


#PAYMENT AND STUFF
email=input("Enter your e-mail: ")
book_cost=flights_info[booking]['cost']
print("\nHow would you like to pay?")
print("1. UPI\n2. Credit Card\n3. Wallet\n")
choice=int(input("Enter your choice: "))
if choice==1:
    print("Kindly pay the cost amount to the UPI ID: AirSchool@oksbi.gpay")
    time.sleep(10)
elif choice==2:
    cc=int(input("Enter your credit card number: "))
    if len(str(cc))>=17 or len(str(cc))<16:
        print("Enter valid credit card!")
        exit()
    else:
        cvv=int(input("Enter your 3-digit cvv: "))
        doe=input("Enter date of expiry: ")
elif choice==3:
    print("Current balance is: ", balance)
    print("Balance after booking:", balance-book_cost)
print("Please wait while we proceed with your transaction.")
time.sleep(5)


#FINALE
print("Your ticket has been booked!")
time.sleep(5)
ref_number="FLIGHT"+str(random.randint(10000,100000))+str(booking)
print("\nYour reference number is: ", ref_number, ".\nSave it for future purposes", sep='')
print("The itinerary has been sent to your email, kindly take it to the airport during check-in.")
print("AirSchool wishes you a happy journey!")