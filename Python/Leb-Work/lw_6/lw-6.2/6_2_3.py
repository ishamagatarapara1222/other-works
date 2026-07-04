filename = input("Enter the filename to read: ")

try:
    file = open(filename, "r")
    content = file.read()
    file.close()
except FileNotFoundError:
    print("Error: The file does not exist!")
else:
    # This runs only if no exception happens above
    print("File Content:")
    print(content)