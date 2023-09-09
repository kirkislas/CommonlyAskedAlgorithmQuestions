# Mid Level Question

# Problem Statement:
# Given an integer n, determine if it is a prime number
# A prime number is a natural number greater than 1 that is not a product of two smaller natural numbers
# In other words, it has only two divisors: 1 and itself

# The following function determines if an input integer is a prime number, explanation with space and time complexity below

def is_prime(n: int) -> bool:

   # Determines if a number is prime

    # Args:
    # n (int): The number to check
    # Returns:
    # bool: True if the number is prime, False otherwise

    # Base cases
    if n <= 1:
        return False
    if n <= 3:
        return True

    # If n is divisible by 2 or 3, it is not prime
    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        # If n is divisible by i or i+2, it's not prime
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True


# Sample Usage:
if __name__ == "__main__":
    number = 29
    print(f"Is {number} prime? {'Yes' if is_prime(number) else 'No'}.")

    number = 15
    print(f"Is {number} prime? {'Yes' if is_prime(number) else 'No'}.")


# Explanation:
# A prime number is a number that is divisible only by 1 and itself
# To determine if a number is prime, we can test if it is divisible by any number
# between 2 and the square root of the number. If it is divisible, then it's not prime

# Space Complexity:
# O(1) - We are using a constant amount of space

# Time Complexity:
# O(sqrt(n)) - In the worst case, we loop up to the square root of the number to check for divisibility
