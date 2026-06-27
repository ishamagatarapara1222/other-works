#4.1.9
#Write a function that accepts **kwargs to print out a formatted description of a person (e.g., name, age, city).

def person_info(**kwargs):
    print("Person Details")

    for key, value in kwargs.items():
        print(key, ":", value)

person_info(name="Rahul", age=20, city="Surat")
