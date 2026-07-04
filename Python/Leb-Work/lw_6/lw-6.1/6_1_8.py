# 'r+' allows both reading and writing
with open("sample.txt", "r+") as file:
    # Read the existing content
    content = file.read()
    print("Current Content:", content)
    
    # Move to the end of the file to append new text cleanly
    file.seek(0, 2) 
    file.write(" This file was last modified by adding this sentence.")

print("File updated in read-write mode!")