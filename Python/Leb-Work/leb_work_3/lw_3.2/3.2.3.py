#3.2.3
'''
Create a list and a tuple both containing the same 3 items.

Try changing the first item of each.
Explain why the tuple gives an error.
'''

my_list = ["Pen", "Book", "Bag"]
my_tuple = ("Pen", "Book", "Bag")

my_list[0] = "Pencil"
print("List:", my_list)

try:
    my_tuple[0] = "Pencil"
except TypeError:
    print("Error: Tuple values cannot be changed")
