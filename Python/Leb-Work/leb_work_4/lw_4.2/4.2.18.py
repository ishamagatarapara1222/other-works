#4.2.18
'''
Create a function that takes a list of words and returns two lists: one with words starting with vowels and the other
with words starting with consonants
'''

def separate_words(words):
    vowels = []
    consonants = []

    for word in words:
        if word[0].lower() in "aeiou":
            vowels.append(word)
        else:
            consonants.append(word)

    return vowels, consonants

words = ["Apple", "Banana", "Orange", "Mango", "Umbrella"]

v, c = separate_words(words)

print("Vowel words:", v)
print("Consonant words:", c)
