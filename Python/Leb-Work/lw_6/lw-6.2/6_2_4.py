text = "Python"

try:
    index = int(input("Enter an index to check: "))
    letter = text[index]
except IndexError:
    print("Error: Index is out of range for this text!")
else:
    # This runs only if the index was valid
    print("The character at that index is:", letter)