# Mid Level Question

# Problem Statement:
# Given a positive float number, compute its square root without using any built-in functions
# You can utilize the Babylonian method (or Heron's method) to achieve this

# Example Inputs and Outputs:
# Input:
# num = 9
# Output:
# 3.0 (or an approximation very close to 3.0)

# Input:
# num = 2
# Output:
# 1.41421356237 (or an approximation close to it)

# The function below computes the square root of a given number without any built in functions using the Babylonian method, explanation with space and time complexity below

def compute_square_root(num: float, tolerance: float = 1e-10) -> float:

    # Args:
    # num (float): The number to compute the square root for
    # tolerance (float): The acceptable error margin for the square root computation. Defaults to 1e-10

    # Returns:
    # float: The square root of the number

    # We start with an initial guess
    guess = num / 2.0

    while True:
        # Improve the guess
        better_guess = (guess + num / guess) / 2.0

        # If the change between our new guess and the old guess is smaller than our tolerance, break
        if abs(better_guess - guess) < tolerance:
            return better_guess

        # Update our guess
        guess = better_guess


# Sample Usage:
if __name__ == "__main__":
    number = 16
    result = compute_square_root(number)
    print(f"The square root of {number} is approximately {result}.")

    number = 2
    result = compute_square_root(number)
    print(f"The square root of {number} is approximately {result}.")


# Explanation:
# To compute the square root without built-in functions, we use the Babylonian method
# This iterative method works by continually refining an estimate until it gets very close to the actual square root

# Space Complexity:
# O(1) - Constant space is used as we only use a few variables to compute the result

# Time Complexity:
# O(log n) - In most cases, as with each iteration, our guess gets closer to the actual square root
