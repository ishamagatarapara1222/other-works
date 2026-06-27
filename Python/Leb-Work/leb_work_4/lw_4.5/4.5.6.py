#6. Implement a program to sort a list of tuples based on the second element of each tuple using the sorted() function


# List of tuples: (Item Name, Price/Score)
items = [("Apple", 50), ("Banana", 20), ("Cherry", 80), ("Date", 40)]
print("Original List of Tuples:")
print(items)

# The lambda function tells sorted() to look at index 1 (the second element)
sorted_items = sorted(items, key=lambda x: x[1])

print("\nSorted List by Second Element:")
print(sorted_items)
