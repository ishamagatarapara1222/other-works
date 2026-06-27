#5. Implement a class Account with a private attribute balance.

#Create methods to deposit and withdraw money.

#Add a method to display the balance.

#Ensure balance cannot be accessed directly


class Account:
    def __init__(self, initial_balance=0):
        # Private attribute to prevent direct external modification
        self.__balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Invalid deposit amount!")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn: {amount}")
        elif amount > self.__balance:
            print("Insufficient balance!")
        else:
            print("Invalid withdrawal amount!")

    def display_balance(self):
        print(f"Available Balance: {self.__balance}")

# Testing the Bank Account
acc = Account(1000)
acc.display_balance()

acc.deposit(500)
acc.withdraw(300)
acc.display_balance()

# Demonstrating that external direct access fails safely
print("\nAttempting direct private access:")
try:
    print(acc.__balance)
except AttributeError as error:
    print(f"[ACCESS DENIED] AttributeError: {error}")
