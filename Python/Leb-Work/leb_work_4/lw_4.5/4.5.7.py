#7.  Develop a program to sort a list of dictionaries by a specific key using the sorted() function.

# List of dictionaries
students = [
    {"name": "Rahul", "age": 21},
    {"name": "Anjali", "age": 19},
    {"name": "Vikram", "age": 22},
    {"name": "Sanya", "age": 20}
]
print("Original List of Dictionaries:")
for s in students:
    print(s)

# Sorting by the key 'age'
sorted_students = sorted(students, key=lambda x: x['age'])

print("\nSorted List of Dictionaries by 'age':")
for s in sorted_students:
    print(s)
