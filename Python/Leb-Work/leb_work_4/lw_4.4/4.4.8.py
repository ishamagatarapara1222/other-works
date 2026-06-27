#8. Print the first, last, and middle elements of the array.

# Sample array
array = [11, 22, 33, 44, 55, 66, 77]
print("Array:", array)

# 1. First element
first_element = array[0]

# 2. Last element
last_element = array[-1]

# 3. Middle element (using floor division to handle index accurately)
middle_index = len(array) // 2
middle_element = array[middle_index]

print("\nOutput:")
print(f"First Element : {first_element}")
print(f"Middle Element: {middle_element}")
print(f"Last Element  : {last_element}")
