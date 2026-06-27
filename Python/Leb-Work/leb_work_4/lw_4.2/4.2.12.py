#4.2.12
'''
Write a program with two functions: one to initialize a global variable and another to increment it by a user-defined
value.
'''

value = 0

def initialize():
    global value
    value = 100

def increment(num):
    global value
    value += num

initialize()
increment(50)

print(value)
