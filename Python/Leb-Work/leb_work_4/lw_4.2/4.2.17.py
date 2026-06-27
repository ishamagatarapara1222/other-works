#4.2.17
'''
Write a program where a function splits a given string into two parts: one containing only vowels and the other
containing all remaining characters. Return both parts.
'''

def split_string(text):
    vowels = ""
    others = ""

    for ch in text:
        if ch.lower() in "aeiou":
            vowels += ch
        else:
            others += ch

    return vowels, others

v, o = split_string("Programming")

print("Vowels:", v)
print("Others:", o)
