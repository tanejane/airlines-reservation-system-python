from Database import user_data,usertxt,booking_details,bookingtxt
#menu
menu = {'A':'Set A - Bread with Juice',
        'B':'Set B - Prawn and Chicken Wanton Noodles',
        'C':'Set C - Chicken rice + Americano',
        'D':'Set D - Roasted Chicken with Black Pepper Sauce'}

def birthdate_check(year,month,day): 
    if year <1953 or year > 2006:      
        print(f"\nPlease enter a valid year!\nWe only accept the age range from 17 to 70 only!\n")
        return False
        

    month_list = {1:["January",31],2:["February",28],3:["March",31],4:["April",30],5:["May",31],6:["June",30],
                  7:["July",31],8:["August",31],9:["September",30],10:["October",31],11:["November",30],12:["December",31]} 

    if year % 4 == 0:
        month_list.update({2:["February",29]})  

    if month not in range(1,13):
        print("\nThere is only 12 months.\n") 
        return False
    else:
        month_name = month_list.get(month)[0]
        max_day = month_list.get(month)[1] 

    if day not in range(1,(max_day+1)):
        print(f"\nThere is only {max_day} days in {month_name}\n")
        return False

#view booking
def view_booking(email):
    found_info = False
    booking_id = input('Enter your booking ID: ').upper() #enter booking id 

    for user_info in user_data:
        for booking in booking_details:
            if (user_info.get('Email ID') == email 
                and booking.get("Booking ID") == booking_id 
                and booking.get("User ID") == user_info.get('User ID')
                ): #match the customer user id and booking id
                found_info = True
                break
    if found_info:
        if booking.get('Status') != 'Cancelled':   #if status is active then will print user booking details       
            
            print('='*10,"Here are your booking details",'='*10)
            print(f"Booking ID: {booking.get('Booking ID')}")
            print(f"Airline Company: {booking.get('Airline Company')}")
            print(f"Departure Date: {booking.get('Departure Date')}")
            print(f"Arrival Date: {booking.get('Arrival Date')}")
            print(f"Departure Time: {booking.get('Departure Time')}")
            print(f"Arrival Time: {booking.get('Arrival Time')}")
            print(f"Origin: {booking.get('Origin')}")
            print(f"Destination: {booking.get('Destination')}")
            print(f"Class: {booking.get('Class')}")
            print(f"Ticket: {booking.get('Ticket')}")
            return email
                    # exit the for loop if user ID is found    
        else:
            print(f'Booking ID {booking.get("Booking ID")} has been cancelled! No booking details shown!')
            return email
    else:
        print('Booking ID does not match!')
        return email
    
def update_booking(email):
    found_info = False
    option = input('Enter the booking ID to update (Booking ID): ').upper()
    for user_info in user_data:
        for booking in booking_details:
            if (user_info.get('Email ID') == email
                and booking.get("User ID") == user_info.get('User ID')
                and booking.get('Booking ID') == option
                ):#match the customer user id and booking id
                found_info = True
                break
            
    if found_info: 
        if booking.get('Status') != 'Cancelled' :    #if status is active then customer can update booking                                              
            print('=' * 10, 'Update Booking', '=' * 10)
            print('What information do you want to update?\n1 = Ticket\n2 = Class\n3 = Menu\n4 = Quit')
            new_update = input('Enter your option: ')

            if new_update == '1':
                new_ticket = input('Enter the new number of tickets: ') #tickets
                if new_ticket.isdigit():
                    booking['Ticket'] = new_ticket
                    print('Number of tickets updated successfully!')
                else:
                    print('Enter numbers only!')

            elif new_update == '2':                     #class
                new_class = input('Enter the new class (Economy or Business): ').capitalize()
                if new_class in ['Economy', 'Business']:
                    booking['Class'] = new_class
                    print('Class updated successfully!')
                else:
                    print('Invalid class!')

            elif new_update == '3':                        #menu
                new_menu = input('Enter a new set menu(A-D): ').upper()
                if new_menu in ('A','B','C','D'):
                    print('Order uploaded')
                    booking['Ordered Menu'] = menu[new_menu]
                else:
                    print('Invalid input!')

            elif new_update == '4':  #quit button
                print('Quit')
                return email

            else:
                print('Invalid option!')
        else: 
            print(f'Booking ID {booking.get("Booking ID")} has been cancelled!')

        with open(bookingtxt, 'w') as file:
            for info in booking_details:
                file.write(f"{info}\n")
            file.close()
        return email
    else:
        print('Booking ID not match with User ID!')
        return email

#cancel booking
def cancel_booking(email):
    found_info = False
    option = input('Enter the booking ID to cancel (Booking ID): ').upper()    

    for user_info in user_data:   
        for booking in booking_details:
            if (user_info.get('Email ID') == email
                and booking.get("User ID") == user_info.get("User ID")
                and booking.get('Booking ID') == option
                ):#match the customer user id and booking id
                found_info = True
                break
               
    #if valid then cancel booking details
    if found_info:      
        if booking.get('Status') != 'Cancelled':         #if customer status is active then they can cancel 
            print('='*10,'Booking Cancellation','='*10)       
            booking['Status'] = 'Cancelled'           
            print("Booking cancelled successfully!\nThank you!")
        else:
            print(f'Booking ID {booking.get("Booking ID")} has been cancelled already!')
            return email
        with open(bookingtxt, 'w') as file: #write its status inside the txt file
            for info in booking_details:
                file.write(f"{info}\n")
        file.close()
        return email
            
    else:
        print("Booking ID not match with your user ID!")
        return email
       
#main of view,update and cancel booking #1.	Can view, update, and cancel own booking.
def booking_management(email): 
    while True:
        print('='*10,'Flight Booking','='*10)
        print('Do you want to view, update or cancel your booking?\n1 = View\n2 = Update\n3 = Cancel\n4 = Exit')   
        option = input('Choose an option: ')   
        if option == '1':
            email = view_booking(email)        
                              
        elif option == '2':
            email = update_booking(email)     
            
        elif option == '3':
            while True:
                ask=input('Are you sure you want to cancel your booking?(Yes/No): ')
                if ask.lower() == 'yes':
                    email = cancel_booking(email)
                    return email
                elif ask.lower() == 'no':
                    print('Thank you!')
                    return email                   
                else:
                    print('Invalid input!')  
        elif option == '4':
            print('Exited!')           
            return email
                  
        else:
            print('Invalid option')

#view personal information
def view_personalinfo(email): 
    found_info = False

    # Check whether the email is valid or not
    for user_info in user_data:
        if user_info.get("Email ID") == email:
            found_info = True
            break
        
    #if valid then print booking details
    if found_info:
        print('='*10, "Here are your personal information", '='*10)
        print(f"Name: {user_info.get('Name')}")
        print(f"User ID: {user_info.get('User ID')}")
        print(f"Email ID: {user_info.get('Email ID')}")
        print(f"Address: {user_info.get('Address')}")
        print(f"Contact Number: {user_info.get('Contact No')}")
        print(f"Gender: {user_info.get('Gender')}")
        print(f"Date of Birth: {user_info.get('BirthDate')}")
    return email
                    
#update personal information
def update_personalinfo(email):   
    found_info = False
    # Check whether the email is valid or not
    for user_info in user_data:
        if user_info.get("Email ID") == email:
            found_info = True
            break

    if found_info: #if its true then they can update personal info
        print('='*10,'Update Personal Information','='*10,'\nWhich information do you want to update?')
        print('1 = Name\n2 = User ID\n3 = Email ID\n4 = Address\n5 = Contact Number\n6 = Gender\n7 = Date of Birth\n8 = Password')
        user_update = str(input('Enter your option: '))
        if user_update == '1':#name
            new_name = input('Enter your new name: ')
            if len(new_name)!= 0 :
                user_info['Name'] = new_name
                print('Update successful!') 
            elif new_name.isdigit():
                print('Enter your new name in alpahabet form!')
            else:
                print(('Enter your new name!'))
        elif user_update == '2':#userid
            new_userID = input('Enter your new user ID: ')
            user_id_exists = False
            for info in user_data:
                if info['User ID'] == new_userID:
                    user_id_exists = True
                    break

            if not user_id_exists:
                if len(new_userID) != 0:
                    old_userID = user_info['User ID'] 
                    user_info['User ID'] = new_userID
                    print('Update successful!')
                    for booking in booking_details:    #booking also need to change since they were linked tgt
                        if booking['User ID'] == old_userID:
                            booking['User ID'] = new_userID              
                else:
                    print('Please enter your new user ID!')           
            else:
                print("\nThis user ID is already in use.\n")
                                                                 
        elif user_update == '3':#email
            new_email = input('Enter your new email ID(@gmail.com): ')
            email_id_exists = False
            for info in user_data:
                if info['Email ID'] == new_email:
                    email_id_exists = True
                    break

            if not email_id_exists:
                if new_email[-10:] == "@gmail.com":
                    user_info['Email ID'] = new_email            
                    print('Update successful! ')   
                    email = new_email   
                else:
                    print("Please enter new email in @gmail.com format!")
            else:
                print("\nThis email ID is already in use.\n")
        
        elif user_update == '4':#address
            new_address = input('Enter your new address: ')
            if len(new_address)!= 0:
                user_info['Address'] = new_address
                print('Update successful!') 
            else:
                print('Please enter your new address!')        
        elif user_update == '5':#contact
            new_contact = input('Enter your new contact number(xxxxxxxxxx): ')
            if len(new_contact) in [10,11]:
                user_info['Contact Number'] = new_contact 
                print('Update successful!')        
            else:   
                print('Please type in valid phone number!')               
        elif user_update == '6':#gender
            new_gender = input('Enter your new gender: ').lower()
            if new_gender == 'male' or new_gender == 'female':
                user_info['Gender'] = new_gender
                print('Update successful!')  
            else:
                print('Gender not available!')             
        elif user_update == '7':#birthdate
            new_year = int(input(" New Birth Year: "))
            new_month = int(input("New Birth Month: "))
            new_day = int(input("New Birth Day: "))  
            if birthdate_check(new_year,new_month,new_day) != False:                  
                new_birthdate = (f"{new_day:02d}/{new_month:02d}/{new_year}")        
                user_info['BirthDate'] = new_birthdate 
                print('Update successful!')                           
        elif user_update == '8':#password
            new_password1 = input('Enter your new password: ')
            if len(new_password1) == 0 :
                    print('Please enter your new password!')
            else:
                new_password2 = input('Enter your new password again: ')
            if new_password1 == new_password2:
                user_info['Password'] = new_password1
                print('Update successful!') 
            else:
                print('Password not match!')
        else:
            print('Please select a valid option!')

        with open(usertxt,'w') as file:#rewrite into txt file
            for info in user_data:
                file.write(f'{info}\n')
        file.close() 
        with open(bookingtxt,'w') as file:#rewrite into txt file
            for info in booking_details:
                file.write(f'{info}\n')
        file.close() 
    return email
                
#delete personal info
def delete_personalinfo(email): 
    found_info = False

    # Check whether the email is valid or not
    for user_info in user_data:
        if user_info.get("Email ID") == email:
            found_info = True
            break

    if found_info:       
        for booking in booking_details[:]: #remove all customer booking if they delete personal info
            if booking.get('User ID') == user_info.get('User ID'):   #if customer user id match in booking and user txt file        
                booking_details.remove(booking)                      # it will remove the customer personal info and booking
           
        user_data.remove(user_info)
        print("Personal information deleted successfully!\nEnter '7' to quit and login or register again!\n") 

        with open (usertxt,'w') as file:
            for info in user_data:
                file.write(f'{info}\n')
        file.close()
        
        with open (bookingtxt,'w') as file:
            for info in booking_details:
                file.write(f'{info}\n')
        file.close()
                  
#main for view,update and delete personal info  #2.Can view, update, and delete personal information.
def personal_information(email): 
    print('='*10,'Personal Information','='*10)
    print('Do you want to view, update or delete your personal information?\n1 = View\n2 = Update\n3 = Delete\n4 = Exit')
    while True:
        option = str(input('Choose an option: '))   
        if option == '1':
            email = view_personalinfo(email) 
            break                                                      
        elif option == '2':
            email = update_personalinfo(email)   
            break     
        elif option == '3':
            print('='*10,'Personal Information Deletion','='*10) 
            while True:              
                confirmation= input('Do you wish to delete your personal information?(Yes/No): ').lower()
                if confirmation.lower() == 'yes':
                    email = delete_personalinfo(email)
                    return
                elif confirmation.lower() == 'no':
                    print('Thank you')
                    return email
                else:
                    print('Invalid input')  
        elif option == '4':
            print('Exited!') 
            return email
        else:
            print('Invalid option')
    return email
    
#3.	Can view the in-flight menu and order the food. In-flight menu will provide the customer with the menu to be order before the flight.
def In_Flight_Menu(email): #inflight menu for customer
    booking_id = input('Enter booking ID: ').upper()
    for user_info in user_data:
        for booking in booking_details: #if their status is active, user id match and booking id is valid then print menu
            if (user_info.get('Email ID') == email
                and booking.get('User ID') == user_info.get('User ID') 
                and  booking.get('Status') != 'Cancelled' 
                and booking.get('Booking ID')==booking_id
            ):                              
                print('='*10,'Menu','='*10)                                   
                print("Here's the menu!")
                for value in menu.values():    ##print the menu
                    print(value)    
                print('Do you want to make an order?')
                while True:
                    ask = input('Yes or No?: ').lower()
                    if ask.lower() == 'yes':
                        order = input('Which set do you want to order? (A-D): ').upper()
                        if order in ('A','B','C','D'):
                            print('Order uploaded!')     
                            booking['Ordered Menu'] = menu[order]#after customer choose the set then it will append into the list
                            print(f"Ordered Menu: {booking['Ordered Menu']}")

                            with open (bookingtxt,'w') as file:#then write inside txtfile
                                for info in booking_details:
                                    file.write(f'{info}\n')
                            file.close()                       
                            return email                     
                        else:
                            print('Invalid input!')
                            return email                                       
                    elif ask.lower()=='no':     
                        print('Thank you!\nBack to Main Page.')
                        return email
                    else:
                        print('Invalid input')   
    else:
        print(f"{booking_id} is not your booking ID!")
        return email
         
#4.	Can do self-check-in and generate their boarding pass.
def Self_Check_In(email): #self check in and generate passd 
    booking_id = input('Enter booking ID: ').upper()
    for user_info in user_data:    
        for booking in booking_details:#if their status is active, user id match and booking id is valid then print menu
            if (user_info.get('Email ID') == email
                and booking.get('User ID') == user_info.get('User ID')
                and booking.get('Status') != 'Cancelled'
                and booking.get('Booking ID') == booking_id
            ):
                print('='*10,'Self Check In','='*10)
                print('Do you want to do self-check-in and generate your boarding pass?')
                while True:
                    option = input('Yes or No?: ').lower()
                    if option == 'yes':        
                        print('\nChecked In!\nHere are your boarding pass!')                
                        boarding_pass = f"""
    ----------BOARDING PASS---------- 
    User ID: {booking.get('User ID')}
    Booking ID: {booking.get('Booking ID')}
    Airline Company: {booking.get('Airline Company')}
    Departure Date: {booking.get('Departure Date')}
    Departure Time: {booking.get('Departure Time')}
    Origin: {booking.get('Origin')}
    Destination: {booking.get('Destination')}
    Class: {booking.get('Class')}
    Ordered Menu: {booking.get('Ordered Menu')}
    ---------------------------------
    """
                        print(boarding_pass)
                        return email
                    elif option == 'no':
                        print('Thank you!\nBack to Main Page.')   
                        return email 
                    else:
                        print('Invalid option!')
    else:
        print(f"{booking_id} is not your booking ID!")
        return email
     

        
