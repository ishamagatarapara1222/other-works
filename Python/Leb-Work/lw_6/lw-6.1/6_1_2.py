#read and display the content
with open("sample.txt" , "r") as file:
    content = file.read()
    print("Old Content:", content)

#open in write mode('w') to over write the content
with open("sample.txt", "w") as file:
    file.write("Learning file handling in python is fun!")

print("File overwritten successfully!")

