#4.1.10
'''
Implement a function that accepts product details like name, price, and quantity using **kwargs.

Return a formatted string showing the total cost of all products.
'''

def product_details(**kwargs):
    total = kwargs["price"] * kwargs["quantity"]

    return f"Product: {kwargs['name']}, Total Cost: {total}"

print(product_details(name="Pen", price=10, quantity=5))
