#3.3.1
'''
Create a set of integers: {1, 2, 3, 4, 5}

Add 6
Remove 3
Check if 2 is in the set
'''

numbers = {1, 2, 3, 4, 5}

numbers.add(6)
numbers.remove(3)

print("Set:", numbers)

if 2 in numbers:
    print("2 is in the set")
else:
    print("2 is not in the set")
