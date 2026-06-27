#7.2 : Bill generator (price + tax)

price = float(input("Enter item price:"))
tax_percent = float(input("Enter tex percentage(eg. 18): "))

tax_amount = ( price * tax_percent) / 100
total_bill = price + tax_amount

print("\n===============================\n")

print("Base price :", price)
print("Tax amount :", tax_amount)
print("Total bill =", total_bill)
