#4. Write a program to create a class Book with private attributes title and author.

#Add public methods to set and get these attributes.

class Book:
    def __init__(self):
        # Private attributes are prefixed with double underscores
        self.__title = ""
        self.__author = ""

    # Setter methods to write private attributes
    def set_title(self, title):
        self.__title = title

    def set_author(self, author):
        self.__author = author

    # Getter methods to read private attributes
    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

# Testing encapsulation
my_book = Book()
my_book.set_title("Python Programming")
my_book.set_author("John Doe")

print("--- Book Details ---")
print("Title :", my_book.get_title())
print("Author:", my_book.get_author())
