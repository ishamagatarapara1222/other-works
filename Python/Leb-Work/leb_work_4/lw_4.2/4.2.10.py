#4.2.10
'''
Write a program where a global variable is updated inside a function to keep track of the sum of all numbers entered
by the user.
'''

total = 0

def add_number(num):
    global total
    total += num

add_number(10)
add_number(20)
add_number(30)

print("Total =", total)
