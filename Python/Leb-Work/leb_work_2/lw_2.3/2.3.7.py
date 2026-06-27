#2.3.7 Check divisibility by 2, 3, or both (1 to 50)

for i in range(1, 51):

    if i % 2 == 0:
        if i % 3 == 0:
            print(i, "- Divisible by both")
        else:
            print(i, "- Divisible by 2")

    else:
        if i % 3 == 0:
            print(i, "- Divisible by 3")
