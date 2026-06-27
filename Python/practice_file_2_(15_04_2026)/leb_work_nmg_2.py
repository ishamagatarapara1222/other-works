#2. Computer guesses user’s number (Binary Search Logic)

low = 1
high = 100

print("Think of a number between 1 and 100.")

while low <= high:
    mid = (low + high) // 2
    print("Is your number",mid,"?")

    response = input("Enter 'h' (too high), 'l' (too law), 'c' (correct):").lower()

    if response == 'c':
        print("I gussed your number.")
        break
    elif response == 'h':
        high = mid-1
    elif response == 'l':
        low = mid +1
    else:
        print("Invalid Input!")
        
