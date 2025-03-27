import Admin1_Function,Admin2_Function

def admin():
    while True:
        print("""1. Upload flight details
2. View all flights
3. Delete in flight service information
4. Modify flight details
5. View total number of flights for each airline and the most frequent flights
6. Search specific in flight menus for specific customers
7. View all bookings
8. Cancel flight schedule
9. Generate flight tickets for customer
10. Generate bills for customer
11. Delete flight details
12. Search booking of specific customer
13. Generate a report
14. View all cancelled bookings
15. Exit           
              """)
        
        choice = None

        choice = str(input("What would you like to do: "))
        if choice == "1":
            Admin1_Function.flight_upload()
        elif choice == "2":
            Admin1_Function.view_flight()
        elif choice == "3":
            Admin1_Function.flight_delete()
        elif choice == "4":
            Admin1_Function.flight_modify()
        elif choice == "5":
            Admin1_Function.flight_search()
        elif choice == "6":
            Admin1_Function.menu_customer()
        elif choice == "7":
            Admin2_Function.view_all_bookings()
        elif choice == "8":
            Admin2_Function.cancel_flight()
        elif choice == "9":
            Admin2_Function.generate_flight_ticket()
        elif choice == "10":
            Admin2_Function.generate_bill()
        elif choice =="11":
            Admin2_Function.delete_details()
        elif choice == "12":
            Admin2_Function.search_bookings()
        elif choice == "13":
            Admin2_Function.generate_report()
        elif choice == "14":
            Admin2_Function.view_cancelled_bookings()
        elif choice == "15":
            print("\nThank you!\n")
            break
        else:
            print("\nInvalid choice. Please enter a number from 1 to 15 only\n")
                


