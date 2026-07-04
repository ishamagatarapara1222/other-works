filename = input("Enter filename to open: ")
file = None

try:
    file = open(filename, "r")
    print(file.read())
except FileNotFoundError:
    print("Error: File was not found.")
finally:
    # This block runs no matter what, safely closing the file if it opened
    if file:
        file.close()
        print("File successfully closed.")