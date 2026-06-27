#while_5. Prime number check

num = int(input("Enter a number: "))

if num <= 1:
    print("Not prime")
else:
    i = 2
    is_prime = True

    while i < num:
        if num % i == 0:
            is_prime = False
            break
        i += 1

    if is_prime:
        print("Prime number")
    else:
        print("Not prime")
