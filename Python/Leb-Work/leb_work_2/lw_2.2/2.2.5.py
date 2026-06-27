'''
Q.5
Write a Program in Python to create a menu-driven fast-food order system using the match case feature.

For example:
Press 1 to order a Sandwich
Press 2 to order a Pizza
Press 3 to order a Burger
Extend this program by adding a nested match case for each menu item’s subtype selection by the user.
For example:
Press 1 for Thin Crust Pizza
Press 2 for Cheese Burst Pizza
Press 3 for Fresh Dough Pizza
'''
print("1. Sandwich")
print("2. Pizza")
print("3. Burger")

choice = int(input("Enter your choice: "))

match choice:

    case 1:
        print("Sandwich types:")
        print("1. Grill Sandwich")
        print("2. Vegetable Sandwich")
        print("3. Aloo-Matar Sandwich")

        sandwich = int(input("Select Sandwich type:"))

        match sandwich:
            case 1:
                print("Grill Sandwich ordered.")
            case 2:
                print("Vegetable sandwich ordered.")
            case 3:
                print("Aloo-matar sandwich orderd.")
            case _:
                print("Invalid sandwich choice.")
                             
    case 2:
        print("Pizza Types:")
        print("1. Thin Crust Pizza")
        print("2. Cheese Burst Pizza")
        print("3. Fresh Dough Pizza")

        pizza = int(input("Select Pizza Type:"))

        match pizza:

            case 1:
                print("Thin Crust Pizza ordered.")
            case 2:
                print("Cheese Burst Pizza ordered.")
            case 3:
                print("Fresh Dough pizza ordered.")
            case _:
                print("Invalid pizza choice.")

    case 3:
        print("Burger Types:")
        print("1. Aloo-tikki Burger")
        print("2. Veggie Burger")
        print("3. Chiken Burger")

        burger = int(input("Select Burger Type:"))

        match burger:

            case 1:
                print("Aloo-tikki Burger ordered.")
            case 2:
                print("Veggie Burger ordered.")
            case 3:
                print("Chiken Burger ordered.")
            case _:
                print("Invalid Burger choice.")

    case _:
         print("Invalid choice!!!")
                     
