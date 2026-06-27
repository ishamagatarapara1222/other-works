'''
Q.6
Write a Program in Python to create a menu-driven telecom calling system using the match case feature.

For example:
Press 1 for English
Press 2 for Hindi
Press 3 for Gujarati
Extend this program by adding a nested match case for each menu item’s appropriate subtype selection by the user.
'''
print("1. Press 1 for English.")
print("2. Hindi ke liye 2 dabaiye.")
print("3. Gujrati mate 3 dabavo.")

lang = int(input("Select Language:"))

match lang:

    case 1:
        print("English Menu:")
        print("1. Press one for Recharge.")
        print("2. Press two for Customer care.")

        english = int(input("Enter your choice:"))

        match english:

            case 1:
                print("Recharge selected.")
            case 2:
                print("Connecting to customer care....")
            case _:
                print("Invalid choice.")

    case 2:
        print("Hindi Menu:")
        print("1. Recharge ke liye ek dabaiye.")
        print("2. Grahak suraksha ke liye do dabaiye.")

        hindi = int(input("Apni Pasand darj kare:"))

        match hindi:

            case 1:
                print("Recharge select hua.")
            case 2:
                print("Grahak Suraksha se connect ho raha he....")
            case _:
                print("Amanya vikalp")
    case 3:
        print("Gujrati Menu:")
        print("1. Recharge karva mate ek dabavo.")
        print("2. Grahak suraksha mate be dabavo.")

        gujrati = int(input("Tamari choice dakhal karo:"))

        match gujrati:

            case 1:
                print("Recharge select thayu.")
            case 2:
                print("Grahak suraksh asathe connect thay rahyu chhe.")
            case _:
                print("Amany choice.")

    case _:
        print("Invalid choice.")

    
                

