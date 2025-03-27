from Database import user_data
from Customer1_Function import view_flight_schedule,book_flight
from Customer2_Function import booking_management,personal_information,In_Flight_Menu,Self_Check_In

def customer(email):
    attempts = 0
    while True: 
        print('='*3,'Welcome to Malaysia Airlines!','='*3)
        print('Which services do you wish to proceed\n1 = View Flight Schedule\n2 = Book Flight\n3 = Booking management\n4 = Personal Information\n5 = Food Menu\n6 = Self-Check-In\n7 = Quit')          
        customer_option= str(input('Enter your option: '))
        if customer_option == '1':
            view_flight_schedule()
        elif customer_option == '2':
            book_flight()
        elif customer_option == '3':
            email = booking_management(email)
        elif customer_option == '4':
            email = personal_information(email)                  
        elif customer_option == '5':
            email = In_Flight_Menu(email)
        elif customer_option == '6':
            email = Self_Check_In(email)            
        elif customer_option == '7':
            print('\nHope you have a good experience with our airlines company. Have a nice day!\n')
            break
        else:
            print(f'Invalid input! {2-attempts} attempts left!')
            attempts += 1
            if attempts == 3:       
                break
    return email

        

