#4.2.3
#Develop a program using recursion to reverse a string.

def reverse_string(text):
    if len(text) == 0:
        return text

    return reverse_string(text[1:]) + text[0]

print(reverse_string("Python"))
