#4.2.4
#Write a recursive function to find the sum of all digits of a given number until a single-digit number remains

def digit_sum(n):
    if n < 10:
        return n

    total = sum(int(d) for d in str(n))
    return digit_sum(total)

num = int(input("Enter number: "))
print(digit_sum(num))
