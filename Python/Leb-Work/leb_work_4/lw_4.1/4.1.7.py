#4.1.7
'''
Implement a function that takes a list of student names using *args and prints each name on a new line.

Additionally check if the list is empty and display a suitable message.
'''

def student_names(*args):
    if len(args) == 0:
        print("No names found")
    else:
        for name in args:
            print(name)

student_names("Amit", "Riya", "Karan")
