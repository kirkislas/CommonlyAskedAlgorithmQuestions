# Entry Level Question

# Problem Statement:
# Write a function that takes a string as an input and returns the string reversed without using any built-in functions or modules

# This is a function that reverses its string input without any built in functions or modules, code explanation with space & time complexity below

def reverse_string(s: str) -> str:
    return s[::-1]


# expected output from function call = 'krik' (my first name backwards)
reverse_string('kirk')

# Explanation
# s[::] or s[::1] will start from the beginning and go to the end, resulting in the original string (since the default step is +1)
# s[::-1] will start from the end and go to the beginning because the step is negative, effectively reversing the string

# Space Complexity: O(n)
# Strings in Python are immutable. So when you reverse a string using slicing, a new string is created to hold the reversed content
# This means the space taken is directly proportional to the size of the input string, leading to a space complexity of O(n)

# Time Complexity: O(n)
# The operation goes through each character of the string once. So if the length of the string is n,
# the time complexity is O(n)
