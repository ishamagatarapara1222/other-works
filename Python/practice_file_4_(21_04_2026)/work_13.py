#13. Count number of vowels in a string

sentence = input("Enter a sentence:").lower()
vowels = "aeiou"

count = 0

for char in sentence:
    if char in vowels:
        count = count + 1

print("Vowels found:", count)
    
