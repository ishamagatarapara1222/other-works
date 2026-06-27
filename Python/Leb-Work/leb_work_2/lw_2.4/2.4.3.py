#2.4.3 Print only consonants from "PYTHON"

word = "PYTHON"

for ch in word:
    if ch in "AEIOU":
        continue

    print(ch)

