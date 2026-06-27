#4.2.14
#Write a function that takes a list of integers and returns the sum, maximum, and minimum values as separate results.

def find_values(numbers):
    return sum(numbers), max(numbers), min(numbers)

s, mx, mn = find_values([10, 20, 30, 40])

print("Sum =", s)
print("Max =", mx)
print("Min =", mn)
