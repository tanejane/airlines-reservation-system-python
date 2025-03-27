from Database import booking_details,flight_details
from Admin1_Function import view_flight

def view_all_bookings():#1.Can view all booking of customers.
    print()
    for booking in booking_details:
        for key, value in booking.items(): #print booking details
            print(f"{key:20} = {value}")
        print() #add an empty line between

def cancel_flight():#2.Can cancel the flight schedule.
    view_flight()

    flight_uid = input("Please enter the flight UID that you wish to cancel: ").upper()
    found_UID = False  #the system has not found the corresponding flight UID yet

    if len(flight_uid) == 0: #no input from user
        print('Please do not leave it blank. Enter flight ID that wish to cancel.\n')
              
    else:
        for flight in flight_details:
            if flight_uid == flight.get('Flight UID'):
                found_UID = True #the flight UID has been found and ready to be canceled
                flight['Status'] = 'Cancelled'
                break

        for dict in booking_details:
            if dict['Flight UID'] == flight_uid:
                dict['Status'] = 'Cancelled' #Cancel bookings of customer whose flight is cancelled
        
        if found_UID: #found_UID=True
            for flight in flight_details:
                print("Updated Flight Schedule:") #display the updated flight schedule with 'Cancel' status
                print("="*80)
                for key, value in flight.items():
                        print(f"{key:20} = {value}")
                print("")

        else: 
            print("Flight not found! Please enter a valid flight ID.\n") #wrong input entered

import random
def generate_flight_ticket():#3.Can generate flight tickets for each customer.
    booking_id = input("Enter the Booking ID: ").upper()

    if len(booking_id) == 0:
        print('Please do not leave it blank.\n')

    else:
        found_booking = None #used to track whether a booking with the specified ID has been found in the list.

        for data in booking_details:
            if booking_id == data["Booking ID"] and data["Status"] == "Active":
                found_booking = data
                break
            elif booking_id == data["Booking ID"] and data["Status"] == "Cancelled":
                print(f"\nYour booking {data['Booking ID']} has been cancelled.\n")
                return

        if found_booking: #check whether bookings are found
            for detail in flight_details:
                if detail['Flight UID'] == found_booking['Flight UID'] and detail['Status'] == 'Active':
                    total_business_seats = detail['Business Class Total Seat']
                    total_economy_seats = detail['Economy Class Total Seat']
                    break
                
            print("\nFlight Ticket")
            print("="*50)
            for key, value in found_booking.items(): #print booking details
                print(f"{key:20} = {value}")
            
            for data in booking_details:
                if booking_id == data['Booking ID']:
                    if data['Class'] == 'Business': #business
                        tickets = data['Ticket']

                        if tickets <= total_business_seats:
                            for customer in range(1, tickets + 1): #assign seats to customers
                                print(f"Ticket {customer} - Seat B{random.randint(1,total_business_seats+1)}")
                        break
                    
                    else: #data['Class'] == 'economy'
                        if booking_id == data['Booking ID']:
                            if data['Class'] == 'Economy':
                                tickets = data['Ticket']
    
                        if tickets <= total_economy_seats:
                            for customer in range(1, tickets + 1): #assign seats to customers
                                print(f"Ticket {customer} - Seat E{random.randint(1,total_economy_seats+1)}")
                        break
            print("Safe flight. Enjoy your trip!\n")

        else: 
            print(f"Booking ID {booking_id} not found.\n")
        
from datetime import datetime
def generate_bill():#4.Can generate bills for each customer.
    user_id = str(input("Enter the user ID: "))

    user_found = False
    for data in booking_details: 
        if user_id == data['User ID'] and data['Status'] == 'Active':
            user_found = True
            for dict in flight_details:
                if dict['Status'] == 'Active' and dict['Flight UID'] == data['Flight UID']:
                    bcprice = dict['Business Class Seat Price']
                    ecprice = dict['Economy Class Seat Price']
                    break
                    
            if data['Class'] == 'Business':
                price = data['Ticket'] * bcprice
            else:  # data['Class'] == 'Economy'
                price = data['Ticket'] * ecprice

            print("\nFlight Bill")
            print("=" * 50)
            for key, value in data.items():
                print(f"{key:30} = {value}")

            print("=" * 50)
            print(f"Price = RM {price}")
            current_datetime = datetime.now()
            formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
            print("Current Datetime:", formatted_datetime)
            print("Have a nice day! Enjoy the trip.\n")
        elif user_id == data['User ID'] and data['Status'] == 'Cancelled':
            print(f'\nYour booking {data["Booking ID"]} has been cancelled\n')
            return
    if user_found == False:
        print("User ID not found. Enter a valid User ID.\n")


def delete_details():#5.Can delete flight details
    deletedetails = str(input("Enter the Flight UID that you wish to delete: ")).upper()
    found = False 

    for details in flight_details:
        if deletedetails == details.get('Flight UID'):
            flight_details.remove(details)  #remove all the details directly

            print(f"Flight details with Flight UID {deletedetails} has been successfully deleted.")
            print("Updated flights details:")
            print("="*70)
            for flight in flight_details:
                for key, value in flight.items():
                    print(f"{key:30} = {value}")
                print("")  #add an empty line between 

            found = True #when user input was found and deleted, found is set to True 
            break   #exit the loop after deleting the entry
                    #once found=True, no need to continue iterating
    
    if not found: #when user input not in list
        print(f"Flight with Flight UID '{deletedetails}' not found.\n")

def search_bookings():#6.Can search booking of specific customers.
    user_id = input("Please enter the User ID of the customer that wish to check: ")
    found_user = False

    for userdata in booking_details:
        if user_id == userdata.get('User ID'):
            found_user = True #when a matching user is found to track whether the user was found

    if found_user:
        print("\nBooking Details:")
        print("="*40)
        for userdata in booking_details:
            if user_id == userdata['User ID']:
                for key, value in userdata.items(): #to iterate over the key-value pairs in booking details
                     print(f"{key:20}: {value}")
                print()
        
    if not found_user:
        print(f"No bookings found matching '{user_id}'. Please enter a valid User ID.\n")
    
def generate_report():#7.Can generate a report.
    print("\nAirlines Company Report") #header
    print("="*100)
    print("1.Malaysia Airline (MAS1709)\n2.Air Asia (ZW1865)\n3.Me Airways (ME2098)\n4.APU Airways (APU8760)\n5.Type anything to go back to menu")

    option = str(input("Choose airlines company between 1 and 4: "))

    if option == "1":
        ac = "Malaysia Airline"
    elif option == "2":
        ac = "Air Asia"
    elif option == "3":
        ac = "Me Airways"
    elif option == "4":
        ac = "APU Airways"
    else:
        print("\nEnter 1 to 4 only\n")
        return
       
    found_flight = False
    
    for details in flight_details:
        if details['Airline Company'] == ac:
            found_flight = True
    
    if found_flight == False:
        print(f"\nThere is no flights for {ac} Company.\n")
        return

    list=[]
    for details in flight_details:
        if details['Airline Company'] == ac and details['Status'] == "Active":
            business_sold = (details['Business Class Total Seat'] - details['Business Class Seat Left']) * details['Business Class Seat Price']
            economy_sold = (details['Economy Class Total Seat'] - details['Economy Class Seat Left']) * details['Economy Class Seat Price']   
            list.append(business_sold)
            list.append(economy_sold)

            print(f"\n {ac} ({details['Airline ID']}) ({details['Flight UID']}) Report")
            print("="*100)
            print("Flights Information:")  #flight information
            print(f"Total Seats in Business Class: {details.get('Business Class Total Seat')}")
            print(f"Total Seats in Economy Class: {details.get('Economy Class Total Seat')}")
            print(f"Seats Bought in Business Class: {details['Business Class Total Seat'] - details['Business Class Seat Left']}")
            print(f"Seats Bought in Economy Class: {details['Economy Class Total Seat'] - details['Economy Class Seat Left']}")
            print(f"Price for Business Class: RM {details.get('Business Class Seat Price')}")
            print(f"Price for Economy Class: RM {details.get('Economy Class Seat Price')}")
            print(f"Revenue: RM {business_sold + economy_sold}")
                
    total_revenue = 0
    for revenue in list:
        total_revenue += revenue
    print(f"\nTotal revenue for {details['Airline Company']}: RM {total_revenue}\n")
            
def view_cancelled_bookings(): #8.Can view all cancelled booking.
    found_cancel = False
    for info in booking_details:
        if info.get('Status') == 'Cancelled':
            for key, value in info.items():
                print (f"{key:20} = {value}")
            print("")
            found_cancel = True

    if not found_cancel:
        print ("There is no cancelled booking.\n")
            