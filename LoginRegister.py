import Admin,Database,Customer
from Database import user_data,usertxt
from Customer2_Function import birthdate_check

def start():
    while True:
        print("==Welcome Page==\n1.Login\n2.Register")
        
        action = str(input("Do you wish to login or register: "))
        if action == "1" or action.lower() == "login":
            login()
            break
        elif action == "2" or action.lower() == "register":
            register()
        else:
            print("\nInvalid Option\n")

def login(): #3.Can login to the system. 
    for attempts in range(0,3):
        login = None
        email = input("Enter your email: ")
        password = input("Enter your password: ")

        for dictionary in user_data:
            if dictionary.get("Email ID") == email and dictionary.get("Password") == password:
                login = True
                status = dictionary.get("Status")
                print("\nLogin successful.\n")

        if login == True:
            if status == "Admin":
                Admin.admin()
                break     
            else:
                email = Customer.customer(email)
                break
        else:
            print(f"\nIncorrect credentials. You have {2-attempts} attempts left!\n")

def register(): #2.Can do registration by providing their details 
    while True:
        register = True
        email = input("Enter your email (@gmail.com): ")
        if email[-10:] != "@gmail.com":
            print("Please enter email in @gmail.com format.")
            register = False
            start()
        
        for dictionary in user_data:
            if dictionary['Email ID'] == email:
                print("\nThis email Is already in use.\n")
                return False
        
        if register == True:
            name = (input("Name: "))
            if len(name) == 0:
                print ("Please enter your name.")
                start()
            elif name.isdigit():
                print ("Please enter your name in alphabet form.")
                start()
            while True:
                address = str(input("Address: "))
                if len(address) != 0:
                    break
                else:
                    print('Please enter your address!')
            while True:
                contact_no = (input("Contact Number(Exp:xxxxxxxxxx): "))
                if len(contact_no) in [10,11]:
                    break
                else:   
                    print('Please type in valid phone number!')
            while True:
                gender = str(input("Gender(Female/Male): ")).lower()
                if gender == 'male' or gender == 'female':
                    break
                else:
                    print('Gender not available!')                    
            while True:
                try:               
                    year = int(input("Birth Year: "))
                    month = int(input("Birth Month: "))
                    day = int(input("Birth Day: "))
    
                    if birthdate_check(year,month,day) != False:                  
                        birthdate = (f"{day:02}/{month:02}/{year}")
                        break
                except ValueError:
                    print ("Please enter valid number.") #if user enters non-numeric characters    
            while True:                     
                user_id = str(input("User ID: "))
                user_id_exists = False
                for info in user_data:
                    if info['User ID'] == user_id:
                        user_id_exists = True
                        break

                if not user_id_exists:
                    break
                else:
                    print("\nThis user ID is already in use.\n")
            password = input("Enter your password: ")
            password2 = input("Enter your password again: ")    #double confirm password
            if password == password2:
                user_data.append({"Email ID":email,"Password":password,"Status":"Customer",
                                    "Name":name,"Address":address,"Contact No":contact_no,
                                    "Gender":gender,"BirthDate":birthdate,"User ID":user_id})
                
                with open(usertxt,"w") as file:
                    for info in user_data:
                        file.write(str(info)+'\n')
                file.close()
                print("\nAccount registered successfully.Please login again.\n")
                break
            else:
                print("\nPassword does not match.\n")

Database.load_database()                            #find txt file , else create new one                                     
start()                                             #starts all the program

with open(Database.flighttxt,"w") as file:          # once program ends, rewrite all files and close it
    for dictionary in Database.flight_details:
        file.write(f"{dictionary}\n")
file.close()
with open(Database.usertxt,"w") as file:
    for dictionary in Database.user_data:
        file.write(f"{dictionary}\n")
file.close()
with open(Database.bookingtxt,"w") as file:
    for dictionary in Database.booking_details:
        file.write(f"{dictionary}\n")
file.close()

                
