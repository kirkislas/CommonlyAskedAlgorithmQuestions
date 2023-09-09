# Mid Level Question

# Problem Statement:
# Write a function to compute the nth number in the Fibonacci sequence using a recursive approach
# The Fibonacci sequence starts with two numbers, 0 and 1, and each subsequent number is the sum of the two preceding ones
# Your function should be able to handle values of n where 0 <= n <= 30
# Provide an explanation of the logic behind your solution and analyze its space and time complexities

# The following function calculates the nth number in the Fibonacci sequence recursively, explanation with space and time complexities below

def fibonacci(n: int) -> int:
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


n = 10
print(fibonacci(n))

# Expected Output: 55

# Explanation:
# The function calculates the nth number in the Fibonacci sequence recursively
# The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding ones, usually starting with 0 and 1
# For example, the 10th number in the Fibonacci sequence is 55

# Space Complexity: O(n)
# Each function call is added to the call stack, and in the worst case, the stack will have a depth of n

# Time Complexity: O(2^n)
# The time complexity of the recursive fibonacci function has an exponential time complexity because it recalculates the same Fibonacci numbers multiple times
