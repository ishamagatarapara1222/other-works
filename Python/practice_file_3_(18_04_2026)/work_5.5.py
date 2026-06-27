#5.5 : Discount calculation using assignment operators

price = 1000
discount_rate = 0.20 # 20% discount


discount_amount = price * discount_rate


price -= discount_amount

print(f"Discount applied: {discount_amount}")
print(f"Final price to pay: {price}")
