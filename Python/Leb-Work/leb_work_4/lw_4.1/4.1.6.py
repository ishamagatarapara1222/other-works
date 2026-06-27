#4.1.6
#Write a Python function that accepts an arbitrary number of integer arguments and returns their sum and product.

def sum_product(*args):
    total = sum(args)

    product = 1
    for num in args:
        product *= num

    return total, product

s, p = sum_product(2, 3, 4)

print("Sum =", s)
print("Product =", p)

 
