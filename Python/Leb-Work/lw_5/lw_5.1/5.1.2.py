#2. Develop a class Counter with an attribute count initialized to zero.

#Create methods to increment the count and display the value using self.

class Counter:
    def __init__(self):
        # Initializing count to zero
        self.count = 0

    def increment(self):
        self.count += 1

    def display_count(self):
        print(f"Current Count: {self.count}")

# Testing the Counter class
my_counter = Counter()
my_counter.display_count()  # Starts at 0

my_counter.increment()
my_counter.increment()
my_counter.display_count()  # Displays 2
