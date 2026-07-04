# Creating a custom exception class by inheriting from standard Exception
class InsufficientBalanceError(Exception):
    pass

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientBalanceError("You do not have enough money in your account!")
    
    balance -= amount
    print(f"Withdrawal successful! Remaining balance: {balance}")
    return balance

# Testing valid and invalid inputs
account_balance = 500

print("--- Testing Invalid Input ---")
try:
    account_balance = withdraw(account_balance, 600)
except InsufficientBalanceError as e:
    print("Error:", e)

print("\n--- Testing Valid Input ---")
try:
    account_balance = withdraw(account_balance, 200)
except InsufficientBalanceError as e:
    print("Error:", e)