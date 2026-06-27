#for_6. Find largest number in a list

numbers = list(map(int, input("Enter numbers sepreted by space:").split()))

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("Largest number is :", largest)
                   
