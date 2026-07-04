# 'rb' stands for Read Binary
with open("sample.txt", "rb") as file:
    binary_content = file.read()
    print(binary_content)