#for_3. Check palindrome number

num = input("Enter a number: ")

reverse = num[::-1]

if num == reverse:
    print("It is a palindrome")
else:
    print("It is not palindrome")
    
