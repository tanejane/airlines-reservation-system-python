from Database import user_data,booking_details,bookingtxt,flight_details,flighttxt

def view_flight_schedule(): #1.Can view all flight. 
    number = 0
    print()
    for info in flight_details:
        number += 1  # Increment the number for the next flight
        flight_schedule = {
            'No': str(number),# Add the 'No' key with the current number value
            'Airline Company': info['Airline Company'],
            'Departure Date': info['Departure Date'],
            'Arrival Date' : info['Arrival Date'],
            'Departure Time': info['Departure Time'],
            'Arrival Time' : info['Arrival Time'],
            'Origin': info['Origin'],
            'Destination': info['Destination'],
            'Status' : info['Status'],
            'Flight UID':info['Flight UID']
        }        
        if info.get('Status') != 'Cancelled':
            for key,value in flight_schedule.items():
                print(f"{key:20}: {value}")
            print()


            
import random
def book_flight(): #4.Booking flight on any of the airlines company by entering booking details  
    view_flight_schedule()
    try:
        option = int(input('Enter the number to book the flight(No.): '))
        if 1 <= option <= len(flight_details):
            ticket = int(input('How many ticket do you want?: '))      
            if ticket == 0:
                print('Please enter a valid amount!') 
                return           
            flight_class = input('What class do you want?(Economy or Business): ').lower().capitalize()
            if flight_class != 'Economy' and flight_class != 'Business':
                print('\nInvalid class!\n')
                return

            user_id = input('Enter your user ID: ')

            booking = False
            for user_info in user_data:
                if user_info["User ID"] == user_id:
                    # Find the corresponding flight_details_1 entry based on the selected option
                    selected_flight_details = flight_details[option - 1]                       
                    booking_id = f'B{random.randint(1000,9999)}' #random generate booking ID
                    customer_booking = {
                        'User ID': user_info['User ID'],
                        'Status':'Active',
                        'Booking ID':booking_id,
                        'Airline Company': selected_flight_details['Airline Company'],
                        'Departure Date': selected_flight_details['Departure Date'],
                        'Arrival Date':selected_flight_details['Arrival Date'],
                        'Departure Time': selected_flight_details['Departure Time'],
                        'Arrival Time':selected_flight_details['Arrival Time'],
                        'Origin': selected_flight_details['Origin'],
                        'Destination': selected_flight_details['Destination'],
                        'Flight UID': selected_flight_details['Flight UID'],
                        'Class' : flight_class,
                        'Ticket' : ticket
                    }
                    booking_details.append(customer_booking)
                    booking = True
                    update_seats_left_after_booking(customer_booking)
                    print('\nBooking successful!')
                    print(f"Here's your booking ID {booking_id}\n")    

                    with open(bookingtxt, 'w') as file:  
                        for info in booking_details:
                            file.write(f"{info}\n")
                    with open(flighttxt, 'w') as file:  
                        for info in flight_details:
                            file.write(f"{info}\n")
                    break

            if booking != True:
                print("\nUser ID does not match!\n")
        else:
            print("\nInvalid option! Please select a valid option from the flight schedule.\n")
    except ValueError:
        print('\nPlease type number!\n')
 
def update_seats_left_after_booking(customer_booking):
    """
    Update the number of seats left in flight_details_1 after a successful booking.
    """
    for flight in flight_details:
        if flight['Flight UID'] == customer_booking['Flight UID']:
            fclass = (customer_booking["Class"])
            class_key = f'{fclass} Class Seat Left'
            flight[class_key] -= customer_booking['Ticket']
            break




        




