search_word = input("Enter the word to search for: ")
line_number = 1
found = False

with open("sample.txt", "r") as file:
    for line in file:

        if search_word.lower() in line.lower():
            print(f"Word found on Line {line_number}")
            found = True
        line_number += 1

if not found:
    print("Word not found in the file.")