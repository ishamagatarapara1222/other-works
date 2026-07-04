
# Step 1: Read from source
with open("source.txt", "r") as source_file:
    data = source_file.read()

# Step 2: Write to backup
with open("backup.txt", "w") as backup_file:
    backup_file.write(data)

print("File copied successfully!")