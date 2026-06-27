#4.2.5
#Create a recursive function to print all prime numbers between two given numbers.

def is_prime(n, i=2):
    if n < 2:
        return False

    if i * i > n:
        return True

    if n % i == 0:
        return False

    return is_prime(n, i + 1)

def print_primes(start, end):
    if start > end:
        return

    if is_prime(start):
        print(start)

    print_primes(start + 1, end)

print_primes(1, 20)
