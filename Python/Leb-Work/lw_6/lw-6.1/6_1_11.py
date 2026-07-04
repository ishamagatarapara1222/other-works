# 1. 'w' Mode (Write - overwrites/creates file)
file = open("demo.txt", "w")
file.write("Hello from write mode.\n")
file.close()

# 2. 'r' Mode (Read - reads existing file)
file = open("demo.txt", "r")
print("Read mode output:", file.read())
file.close()

# 3. 'a' Mode (Append - adds to the end)
file = open("demo.txt", "a")
file.write("Hello from append mode.\n")
file.close()

# 4. 'r+' Mode (Read and Write)
file = open("demo.txt", "r+")
print("r+ read:", file.read())
file.write("Adding text using r+.\n")
file.close()

# 5. 'w+' Mode (Write and Read - clears file first!)
file = open("demo.txt", "w+")
file.write("Fresh start with w+.\n")
file.seek(0) # Go back to start to read it
print("w+ read:", file.read())
file.close()

# 6. 'a+' Mode (Append and Read)
file = open("demo.txt", "a+")
file.write("Adding text with a+.\n")
file.seek(0) # Go back to start to read it
print("a+ read:", file.read())
file.close()