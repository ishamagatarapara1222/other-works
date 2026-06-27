#4.2.13
#Develop a program to demonstrate the difference between local and global variables with the same name.

 name = "Global"

def show():
    name = "Local"

    print("Inside function:", name)

show()

print("Outside function:", name)
