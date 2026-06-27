#3.1.7
'''
Check if a string starts with "Hello" and ends with "World".
Remove all non-alphabetic characters from "Data123#Science!".
Reverse the string "Python".
'''

text = "Hello Everyone World"

print("Starts with Hello:", text.startswith("Hello"))
print("Ends with World:", text.endswith("World"))

text2 = "Data123#Science!"
result = ""

for ch in text2:
    if ch.isalpha():
        result += ch

print("Only letters:", result)

word = "Python"
print("Reversed:", word[::-1])
