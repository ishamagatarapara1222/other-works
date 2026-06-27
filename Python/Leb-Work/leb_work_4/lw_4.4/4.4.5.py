#5. Take user input for a number. Check if it exists in the array. Print the index if found, else print "Not Found".

# Sample dataset array
array = [10, 20, 30, 40, 50, 60, 70]
print("Target Array:", array)

# Taking user input
search_element = int(input("Enter a number to search: "))

found = False
index_found = -1

# Iterating through the array to check existence and index
for i in range(len(array)):
    if array[i] == search_element:
        found = True
        index_found = i
        break  # Stop searching once found

# Output result
if found:
    print(f"Element found at index: {index_found}")
else:
    print("Not Found")
