#3.2.1
'''
Create a list of 5 fruits. Print the second and last fruit.

Add "Mango" to the list.
Remove the first element.
Sort the list alphabetically.
Reverse it.
'''

fruits = ["Apple", "Banana", "Grapes", "Orange", "Kiwi"]

print("Second fruit:", fruits[1])
print("Last fruit:", fruits[-1])

fruits.append("Mango")
print("After adding Mango:", fruits)

fruits.pop(0)
print("After removing first fruit:", fruits)

fruits.sort()
print("Sorted list:", fruits)

fruits.reverse()
print("Reversed list:", fruits)
