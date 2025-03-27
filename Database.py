import ast,os

usertxt = ("./userdata.txt")    # gets current python workspace directory + the txt file
flighttxt = ("./flight.txt")
bookingtxt = ("./booking.txt")

user_data = []      # Mulitple dictionaries will be stored in list
flight_details=[]
booking_details = []

def load_database():
    try:
        if os.path.exists(usertxt):     #check if file exists
            print("Found userdata")
        else:
            print('User data not found! Creating a new one...')
            with open(usertxt,"w") as file:
                file.write(str({"Email ID":"admin@gmail.com",
                                "Password":"admin",
                                "Status":"Admin",
                                "Name":"admin",
                                "Address":"admin",
                                "Contact No":"0101010102",
                                "Gender":"male",
                                "BirthDate":"30/08/2004",
                                "User ID":"admin"}) + "\n" +
                                
                            str({"Email ID":"customer@gmail.com",
                                "Password":"customer",
                                "Status":"Customer",
                                "Name":"customer",
                                "Address":"customer",
                                "Contact No":"0101010101",
                                "Gender":"male",
                                "BirthDate":"15/5/2004",
                                "User ID":"customer"}) + "\n")
                            
                    
        with open(usertxt,"r") as file:
            for line in file:
                dictionary = ast.literal_eval(line)     #converts lines in txt file back to its original value
                user_data.append(dictionary)
        file.close()
                        
        if os.path.exists(flighttxt):
             print("Found flight details")
        else:
            print('Flight details not found! Creating a new one...')
            with open(flighttxt,"w") as file:
                file.write(str({"Airline Company":"Air Asia","Airline ID":"ZW1865",
                                "Business Class Total Seat":30,"Economy Class Total Seat":150,                                
                                "Business Class Seat Left":30,"Economy Class Seat Left":148,                                
                                "Business Class Seat Price":88,"Economy Class Seat Price":188,                                
                                "Departure Date":"30/10/2023","Departure Time":"2100",                                
                                "Arrival Date":"31/10/2023","Arrival Time":"0300",                               
                                "Origin":"Malaysia","Destination":"Japan",                               
                                "Status":"Active","Flight UID":"AA0001"})
                                +"\n"+
                            str({"Airline Company":"Me Airways","Airline ID":"ME2098",
                            "Business Class Total Seat":30,"Economy Class Total Seat":150,                                
                            "Business Class Seat Left":30,"Economy Class Seat Left":150,                                
                            "Business Class Seat Price":88,"Economy Class Seat Price":188,                                
                            "Departure Date":"25/11/2023","Departure Time":"1800",                                
                            "Arrival Date":"26/11/2023","Arrival Time":"0100",                               
                            "Origin":"Malaysia","Destination":"Thailand",                               
                            "Status":"Active","Flight UID":"MA0001"})
                                )  
                                
        with open(flighttxt,"r") as file:
            for line in file:
                dictionary = ast.literal_eval(line)
                flight_details.append(dictionary)  
        file.close()

        if os.path.exists(bookingtxt):
            print("Found booking data\n")
        else:
            print('Booking data not found! Creating a new one...')
            with open(bookingtxt,'w') as file:
                file.write(str({'User ID': 'customer', 'Status': 'Active', 'Booking ID': 'B4408', 'Airline Company': 'Air Asia', 
                                 'Departure Date': '30/10/2023', 'Arrival Date': '31/10/2023', 'Departure Time': '2100', 'Arrival Time': '0300', 
                                 'Origin': 'Malaysia', 'Destination': 'Japan', 'Flight UID': 'AA0001', 
                                 'Class': 'Economy', 'Ticket': 2, 'Ordered Menu': 'Set A - Bread with Juice'})
                           +"\n")
                           
        with open(bookingtxt,'r') as file:
            for line in file:
                dictionary = ast.literal_eval(line)
                booking_details.append(dictionary)
        file.close()
    except Exception as e:
        print(e)
