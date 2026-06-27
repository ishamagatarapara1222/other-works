#4.1.4
#Write a UDF that takes a string as input and returns the frequency of each character in the string as a dictionary.

def char_frequency(text):
    freq = {}

    for ch in text:
        freq[ch] = freq.get(ch, 0) + 1

    return freq

s = input("Enter a string: ")
print(char_frequency(s))
