#3.1.3 Implement a program to:
'''
Take a string as input.
Print the string reversed.
Print whether it is a palindrome.
'''

text = input("Enter a string: ")

reverse_text = text[::-1]

print("Reversed string:", reverse_text)

if text == reverse_text:
    print("Palindrome")
else:
    print("Not a palindrome")
