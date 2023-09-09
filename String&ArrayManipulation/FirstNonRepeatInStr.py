# Entry Level Question

# Problem Statement:
# Find and return the first non-repeated character in a given string

# This is a function that finds and returns the first non repeated character in any given string, code explanation with space & time complexity below

def first_non_repeated(s: str) -> str:
    character_count = {}
    for character in s:
        # For each character in the string, we check if it's already in the dictionary
        # If it is, it gets its count and adds 1; if not, it defaults to 0 (thanks to the get method's second argument) and then adds 1
        character_count[character] = character_count.get(character, 0) + 1
    for character in s:   # The second loop checks each character in the order they appear in the string to find and return the first one that's not repeated
        if character_count[character] == 1:
            return character
    return None


# Since 'k' and 'i' are both repeated at least once within the string, the expected output from function call = 'r' (3rd letter of full name)
first_non_repeated('kirkislas')


# Explanation:
# The first loop is necessary because it counts the occurrences of each character in the string.
# The second loop is necessary because it checks each character in its original order and returns the first one that appears only once.
# If no such character is found, the function returns None.

# Space Complexity: O(n)
# The space complexity is O(n) because in the worst-case scenario (all unique characters),
# the dictionary 'character_count' will store all characters in the string.
# Thus, the space taken grows linearly with the size of the input string.

# Time Complexity: O(n)
# The time complexity is O(n) because the function processes each character in the string twice
# (once for counting and once for checking). In big O notation, we consider the largest factor,
# so the complexity is O(n). The function doesn't have nested loops dependent on 'n', so the operations are linear.
