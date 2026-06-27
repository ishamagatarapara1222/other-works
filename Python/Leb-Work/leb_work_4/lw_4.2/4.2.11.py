#4.2.11
'''
Implement a program to modify a global variable that stores a username.

Use a function to update the name based on user input.
'''

username = "Admin"

def update_name():
    global username
    username = input("Enter new username: ")

update_name()

print("Updated username:", username)
