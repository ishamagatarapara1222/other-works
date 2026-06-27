#Q.6 Implement a program to search for an element in a 1D array and return its index.

arr = [10, 20, 30, 40, 50]

element = 40

if element in arr:
    print("Index =", arr.index(element))
else:
    print("Element not found")
