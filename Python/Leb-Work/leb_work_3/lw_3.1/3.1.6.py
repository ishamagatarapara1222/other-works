#3.1.6
'''
Split "apple,banana,grapes" into a list.
Join the list ["Python", "is", "awesome"] into a sentence using spaces.
Split a multiline string into separate lines and print them one by one.
'''

fruits = "apple,banana,grapes"
fruit_list = fruits.split(",")

print("List:", fruit_list)

words = ["Python", "is", "awesome"]
sentence = " ".join(words)

print("Joined sentence:", sentence)

text = """Hello
How are you
Python"""

lines = text.splitlines()

for line in lines:
    print(line)
