#2.3  :  Calculate area of rectangle/circle

choice = input("Enter your choice (Rectangle/Circle): ")

if choice == "rectangle":
    l = float(input("Enter legth:"))
    w = float(input("Enter width:"))
    print("Area of rectangle:" , l*b)

elif choice == "circle":
    r = float(input("Enter radius:"))
    print("Area of circle = ", 3.14 * r * r)

              
