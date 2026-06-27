#15. Check if string is palindrome

word = input("Enter a word:")
reversed_word = word[::-1]

if word == reversed_word:
    print("It is a palindrome.")
else:
    print("It's not palindrome.")
