character_count = 0
word_count = 0
line_count = 0

with open("notes.txt", "r") as file:
    for line in file:
        line_count += 1
        character_count += len(line)
        
        # split() breaks the line into individual words
        words = line.split()
        word_count += len(words)

print("Total Lines:", line_count)
print("Total Words:", word_count)
print("Total Characters:", character_count)