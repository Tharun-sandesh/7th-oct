import math

def is_prime(n):
    # Primes must be greater than 1
    if n <= 1:
        return False
    # 2 is the only even prime number
    if n == 2:
        return True
    # Eliminate all other even numbers immediately
    if n % 2 == 0:
        return False
    
    # Only check odd divisors up to the square root of n
    # This is an O(sqrt(n)) approach
    limit = int(math.sqrt(n)) + 1
    for i in range(3, limit, 2):
        if n % i == 0:
            return False
            
    return True

# Testing the function
number = 29
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")