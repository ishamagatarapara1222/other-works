#4.1.8
'''
Develop a program where a UDF accepts *args and filters out the strings from the arguments.

Return a tuple of filtered values (e.g., strings in one tuple, numbers in another)
'''

def filter_values(*args):
    strings = ()
    numbers = ()

    for item in args:
        if isinstance(item, str):
            strings += (item,)
        elif isinstance(item, (int, float)):
            numbers += (item,)

    return strings, numbers

s, n = filter_values("Hello", 10, "Python", 25)

print("Strings:", s)
print("Numbers:", n)
