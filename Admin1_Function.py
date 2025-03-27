import Database,random
from Database import flight_details,booking_details,user_data

def date_check(year,month,day):
    if year < 2023:
        print(f"\nYear {year} is over\n")
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

def flight_upload(): #2.Can upload flight details in the system
    try:
        print("\n1.Malaysia Airline\n2.Air Asia\n3.Me Airways\n4.APU Airways")
        airline_company = str(input("Which airline company: "))
        if airline_company == "1" or airline_company.lower() == "malaysia airline":
            airline_company = "Malaysia Airline"
            airline_id = "MAS1709"
            flight_uid = "MAS" + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
        elif airline_company == "2" or airline_company.lower() == "air asia":
            airline_company = "Air Asia"
            airline_id = "ZW1865"
            flight_uid = "AA" + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
        elif airline_company == "3" or airline_company.lower() == "me airways":
            airline_company = "Me Airways"
            airline_id = "ME2098"
            flight_uid = "MA" + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
        elif airline_company == "4" or airline_company.lower() == "apu airways":
            airline_company = "APU Airways"
            airline_id = "APU8760"
            flight_uid = "APU" + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
        else:
            print("\nInvalid airline company\n")
            return

        bc_seat = int(input("Total seats in business class: "))
        ec_seat = int(input("Total seats in economy class: "))
        bc_seat_left = bc_seat
        ec_seat_left = ec_seat        
        bc_seat_price = int(input("Business Class Seat Price: "))
        ec_seat_price = int(input("Economy Class Seat Price: "))  

        year = int(input("Departure Year: "))
        month = int(input("Departure Month: "))
        day = int(input("Departure Day: "))
        if date_check(year,month,day) != False:
            departure_date = (f"{day:02}/{month:02}/{year}")
        else:
            return
        
        departure_time = input("Departure time (24 hour format): ")
        if len(departure_time) != 4 or int(departure_time[:2]) not in range(0,25) or int(departure_time[2:]) not in range(0,60):
            print("\nInvalid time or format.\n")
            return
        else:
            departure_time = departure_time[:2] + departure_time[2:]
        
        year = int(input("Arrival Year: "))
        month = int(input("Arrival Month: "))
        day = int(input("Arrival Day: "))
        if date_check(year,month,day) != False:
            arrival_date = (f"{day:02}/{month:02}/{year}")
        else:
            return

        arrival_time = input("Arrival time (24 hour format): ")
        if len(arrival_time) != 4 or int(arrival_time[:2]) not in range(0,25) or int(arrival_time[2:]) not in range(0,60):
            print("\nInvalid time or format.\n")
            return
        else:
            arrival_time = arrival_time[:2] + arrival_time[2:]

        origin = input("Origin: ").capitalize()
        destination = input("Destination: ").capitalize() 
        status = "Active"

        flight_details.append({"Airline Company":airline_company,
                                "Airline ID":airline_id,
                                "Business Class Total Seat":bc_seat,
                                "Economy Class Total Seat":ec_seat,
                                "Business Class Seat Left":bc_seat_left,
                                "Economy Class Seat Left":ec_seat_left,
                                "Business Class Seat Price":bc_seat_price,
                                "Economy Class Seat Price":ec_seat_price,
                                "Departure Date":departure_date,
                                "Departure Time":departure_time,
                                "Arrival Date":arrival_date,
                                "Arrival Time":arrival_time,
                                "Origin":origin,
                                "Destination":destination,
                                "Status":status,
                                "Flight UID":flight_uid})
        
        with open(Database.flighttxt,"w") as file:        
            for dictionary in Database.flight_details:
                file.write(f"{dictionary}\n")
        file.close()
        print("\nUpdate successful.\n")

    except ValueError:
        print("\nNumbers only\n")
        return
    
def view_flight(): #3.Can view all flight. 
    list = ["Airline Company","Airline ID","BC total seat","EC total seat","BC seat left","EC seat left","BC seat price","EC seat price"]
    list2 = ["Departure Date","Departure Time","Arrival Date","Arrival Time","Origin","Destination","Status","Flight UID"]

    for dictionary in flight_details:
        ac = dictionary["Airline Company"]
        ai = dictionary["Airline ID"]
        bct = dictionary["Business Class Total Seat"]
        ect = dictionary["Economy Class Total Seat"]
        bcl = dictionary["Business Class Seat Left"]
        ecl = dictionary["Economy Class Seat Left"]
        bcp = dictionary["Business Class Seat Price"]
        ecp = dictionary["Economy Class Seat Price"]
        dd = dictionary["Departure Date"]
        dt = dictionary["Departure Time"]
        ad = dictionary["Arrival Date"]
        at = dictionary["Arrival Time"]
        ori = dictionary["Origin"]
        des = dictionary["Destination"]
        sta = dictionary["Status"]
        uid = dictionary["Flight UID"]

        no = -1 
        print("\n"+"=" * 145)
        for i in list:
            no += 1
            print(f"|{list[no]:^17}",end="")
        print("|\n"+"=" * 145)
        print(f"|{ac:^17}|{ai:^17}|{bct:^17}|{ect:^17}|{bcl:^17}|{ecl:^17}|{bcp:^17}|{ecp:^17}|")

        no1 = -1
        print("=" * 145)
        for i in list2:
            no1 += 1
            print(f"|{list2[no1]:^17}",end="")
        print("|\n"+"=" * 145)
        print(f"|{dd:^17}|{dt:^17}|{ad:^17}|{at:^17}|{ori:^17}|{des:^17}|{sta:^17}|{uid:^17}|")
        print("=" * 145 + "\n")

def flight_delete(): #6.Can delete in-flight service information.
    bookingid = str(input("Enter the booking ID of the user to delete its ordered menu: ")).upper()

    found = False
    for booking in booking_details:
        if booking['Booking ID'] == bookingid:
            found = True
            try:
                booking.pop('Ordered Menu')
                print("\nCustomer's ordered menu has been removed\n")
            except KeyError:
                print(f"\nThis customer did not order any food for booking {booking['Booking ID']}\n")
    
    if not found:
        print(f"\nBooking ID {bookingid} invalid or not found\n")

    with open(Database.bookingtxt,"w") as file:
        for dictionary in Database.booking_details:
            file.write(f"{dictionary}\n")
    file.close()

def flight_modify(): #5.Can update/modify flight details if required. 
    view_flight()
    try:
        flightuid = str(input("Enter the flight UID of the flight you want to modify: ")).upper()

        modify = False 
        for dictionary in flight_details:
            if dictionary["Flight UID"] == flightuid:
                modify = True
        
        if modify != True:
            print("\nFlight not found\n")
            return

        for attempt in range(0,3):      
            print("\n1.Airline Company\n2.Business Class Total Seat\n3.Economy Class Total Seat\n4.Business Class Seat Price\n5.Economy Class Seat Price\n6.Departure Date\n7.Departure Time\n8.Arrival Date\n9.Arrival Time\n10.Origin\n11.Destination")
            option = str(input("What do you want to change: "))
            change = False
        
            if option == "1" or option.lower() == "airline company":          
                key = "Airline Company"
                key2 = "Airline ID"    
                print("\n1.Malaysia Airline\n2.Air Asia\n3.Me Airways\n4.APU Airways") 
                airline_company = str(input("Change to which airline company: "))
                if airline_company == "1" or airline_company.lower() == "malaysia airline":
                    value = "Malaysia Airline"
                    value2 = "MAS1709"
                    change = True
                    break
                elif airline_company == "2" or airline_company.lower() == "air asia":
                    value = "Air Asia"
                    value2 = "ZW1865"
                    change = True
                    break
                elif airline_company == "3" or airline_company.lower() == "me airways":
                    value = "Me Airways"
                    value2 = "ME2098"
                    change = True
                    break
                elif airline_company == "4" or airline_company.lower() == "apu airways":
                    value = "APU Airways"
                    value2 = "APU8760"
                    change = True
                    break
                else:
                    print("\nInvalid airline company\n")
                    break
                
            elif option == "2" or option.lower() == "business class total seat":
                key = "Business Class Total Seat"
                key2 = "Business Class Seat Left"
                value = int(input("Business class total seat change to: "))
                
                list = []
                for dict in booking_details:
                    if dict["Flight UID"] == flightuid and dict["Class"] == "Business":
                        list.append(dict["Ticket"])

                total = 0
                for num in list:
                    total += num 

                if total < value: 
                    value2 = value - total
                    change = True
                    break
                else:
                    print("\nBookings more than total seats")        
            elif option == "3" or option.lower() == "economy class total seat":
                key = "Economy Class Total Seat"
                key2 = "Economy Class Seat Left"
                value = int(input("Economy class total seat change to: "))

                list = []
                for dict in booking_details:
                    if dict["Flight UID"] == flightuid and dict["Class"] == "Economy":
                        list.append(dict["Ticket"])
    
                total = 0
                for num in list:
                    total += num 

                if total < value: 
                    value2 = value - total
                    change = True
                    break
                else:
                    print("\nBookings more than total seats") 

            elif option == "4" or option.lower() == "business class seat price":
                key = "Business Class Seat Price"
                value = int(input("Business class seat price change to: "))
                change = True
                break
            elif option == "5" or option.lower() == "economy class seat price":
                key = "Economy Class Seat Price"
                value = int(input("Economy class seat price change to: "))
                change = True
                break

            elif option == "6" or option.lower() == "departure date":
                key = "Departure Date"
                year = int(input("Departure year change to: "))
                month = int(input("Departure month change to: "))
                day = int(input("Departure day change to: "))
                if date_check(year,month,day) != False:
                    value = (f"{day:02}/{month:02}/{year}")
                    change = True
                    break
                
            elif option == "7" or option.lower() == "departure time":
                key = "Departure Time"
                value = input("Departure time (24 hour format): ")
                if len(value) != 4 or int(value[:2]) not in range(0,25) or int(value[2:]) not in range(0,60):
                    print("\nInvalid time or format.\n")
                    break
                else:
                    value = value[:2] + value[2:]
                    change = True
                    break

            elif option == "8" or option.lower() == "arrival date":
                key = "Arrival Date"
                year = int(input("Arrival year change to: "))
                month = int(input("Arrival month change to: "))
                day = int(input("Arrival day change to: "))
                if date_check(year,month,day) != False:
                    value = (f"{day:02}/{month:02}/{year}")
                    change = True
                    break

            elif option == "9" or option.lower() == "arrival time":
                key = "Arrival Time"
                value = input("Departure time (24 hour format): ")
                if len(value) != 4 or int(value[:2]) not in range(0,25) or int(value[2:]) not in range(0,60):
                    print("\nInvalid time or format.\n")
                    break
                else:
                    value = value[:2] + value[2:]
                    change = True
                    break

            elif option == "10" or option.lower() == "origin":
                key = "Origin"
                value = input("Origin change to: ").capitalize()
                change = True
                break
            elif option == "11" or option.lower() == "destination":
                key = "Destination"
                value = input("Destination change to: ").capitalize()
                change = True
                break
            else:
                print(f"\nInvalid option. {2 - attempt} attempts left.\n")

    except ValueError:
        print("\nNumbers Only\n")
    
    if change == True:
        count = -1
        for dictionary in flight_details:
            count += 1
            if dictionary["Flight UID"] == flightuid:
                flight_details[count].update({key:value})
                if option == "1" or option.lower() == "airline company" or option == "2" or option.lower() == "business class total seat" or option == "3" or option.lower() == "economy class total seat":
                    flight_details[count].update({key2:value2})

        with open(Database.flighttxt,"w") as file:
            for dictionary in Database.flight_details:
                file.write(f"{dictionary}\n")
        file.close()
        
        print("\nChanges have been made\n")

def menu_customer(): #7.Can search specific in-flight menus for specific customers. 
    list = []
    count = 0
    for dict in user_data:
        if dict["Status"] != "Admin":
            count += 1
            list.append(dict["User ID"])
            print(f"[{count}] {dict['User ID']}")
       
    userid = str(input("Enter the user ID of user you wish to check: "))
    if userid not in list:
        print("\nUser not found\n")
    else:
        booking = False
        for details in booking_details:
            if details["User ID"] == userid and details["Status"] != "Cancelled" and details.get('Ordered Menu') != None:
                booking = True
                print(f"\n{'User ID':15}:{details['User ID']}")
                print(f"{'Booking ID':15}:{details['Booking ID']}")
                print(f"{'Ordered Menu':15}:{details['Ordered Menu']}\n")

        if booking == False:
            print("\nThis customer does not have any food ordered\n")
        
def flight_search(): #4.Can view the AirlineID, AirlineName and the total number of flights for each Airline. 8.Can search the Airline with the most frequencies of flights.  
    list = []
    list2 = []
    MalaysiaAirline = 0 
    AirAsia = 0
    MeAirways = 0
    APUAirways = 0 

    for dict in flight_details:
        if dict.get("Airline Company") == "Malaysia Airline":
            MalaysiaAirline += 1
        elif dict.get("Airline Company") == "Air Asia":
            AirAsia += 1
        elif dict.get("Airline Company") == "Me Airways":
            MeAirways += 1
        elif dict.get("Airline Company") == "APU Airways":
            APUAirways += 1

    print(f"\nMalaysia Airline [MAS1709] has {MalaysiaAirline} flights")
    print(f"Air Asia [ZW1865] has {AirAsia} flights")
    print(f"Me Airways [ME2098] has {MeAirways} flights")
    print(f"APU Airways [APU8760] has {APUAirways} flights")

    list.append(MalaysiaAirline)
    list.append(AirAsia)
    list.append(MeAirways)
    list.append(APUAirways)

    for i in range(0,len(list)):
        for j in range(i+1,len(list)):
            if list[i] >= list[j]:
                list[i],list[j] = list[j],list[i]

    if MalaysiaAirline == list[3]:
        list2.append("Malaysia Airline")
    if AirAsia == list[3]:
        list2.append("Air Asia")
    if MeAirways == list[3]:
        list2.append("Me Airways")
    if APUAirways == list[3]:
        list2.append("APU Airways")
    
    print()
    for i in range(0,len(list2)):
        if i == 1 or i == 3:
            print(" & ",end="")
        print(list2[i],end="")  
    print(f" have {list[3]} flights which is the most frequent\n")



            



