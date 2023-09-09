# Entry Level Question

# Problem Statement:
# Determine if an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward
# Negative numbers can also be considered for palindromic patterns, for example, -121 is not a palindrome because there's a negative sign, but 121 is a palindrome

# The function below takes in an integer and checks to see if it reads the same backwards as it does forwards (known as a palindrome), explanation with space and time complexity below

def is_palindrome(num: int) -> bool:
    # Args:
    # num (int): The integer to check
    # Returns:
    # bool: True if the integer is a palindrome, False otherwise

    # Convert the number to a string for easier comparison
    num_str = str(num)

    # Compare the string with its reverse
    return num_str == num_str[::-1]


# Sample Usage:
if __name__ == "__main__":
    test_number = 121
    print(f"Is {test_number} a palindrome? {is_palindrome(test_number)}")

    test_number = -121
    print(f"Is {test_number} a palindrome? {is_palindrome(test_number)}")

    test_number = 10
    print(f"Is {test_number} a palindrome? {is_palindrome(test_number)}")


# Explanation:
# To solve this, we convert the integer to a string and then check if
# the string reads the same forwards and backwards

# Space Complexity:
# O(n) - where n is the number of digits in the number. This is
# because we're converting the integer to a string

# Time Complexity:
# O(n) - where n is the number of digits in the number. We go
# through the string once to reverse it and check for palindrome
