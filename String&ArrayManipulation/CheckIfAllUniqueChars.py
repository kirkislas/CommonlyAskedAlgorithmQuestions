# Entry Level Question

# Problem Statement:
# Determine if a given string has all unique characters

# This is a function that checks if an input string has all unique characters, code explanation with space and time complexity below

def has_all_unique_chars(s: str) -> bool:
    # Compares the length of s to the length of the unique characters within s
    return len(s) == len(set(s))


has_all_unique_chars('kirkislas')

# Explanation:
# set(s) returns all unique characters within s, we want the length of that
# We are comparing the length of the original input vs the length of unique characters within that original input
# If the numbers match up, s has all unique characters and the function will return True
# If they don't match, there are repeated characters within s and the function will return False

# Space Complexity: O(n)
# The function creates a set with unique characters from the string. In the worst case (all characters are unique),
# the size of the set will be equal to the size of the string, so space complexity is O(n)

# Time Complexity: O(n)
# The function processes each character in the string once when constructing the set, resulting in a linear time complexity
