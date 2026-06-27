#7.4 : Even/Odd + positive/negative check

num = int(input("Enter a number:"))

if num%2 == 0 and num>0:
    print("your entered number is Even and Positive.")
elif num%2 == 0 and num<0:
    print("Your enterd number is Even and Nagative.")
elif num%2 != 0 and num>0:
    print("Your enterd number is Odd and Positive.")
elif num%2 != 0 and num<0:
    print("Your entered number is Odd and Nagative.")
else:
    print("Invalid input!!!")
    
