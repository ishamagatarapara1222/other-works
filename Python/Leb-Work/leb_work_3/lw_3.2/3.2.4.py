#3.2.4

#Create a list of squares of numbers from 1 to 10 using list comprehension.

squares = [x * x for x in range(1, 11)]

print(squares)

'''
Create a new list that only contains even numbers from:

[1, 2, 3, ..., 20]
'''     

even_numbers = [x for x in range(1, 21) if x % 2 == 0]

print(even_numbers)

'''
Convert all strings in:

["hello", "WORLD", "PyThOn"]
to lowercase using list comprehension.
'''

words = ["hello", "WORLD", "PyThOn"]

lower_words = [word.lower() for word in words]

print(lower_words)

