# Mid Level Question

# Problem Statement:
# Given two strings, find the length of the longest common subsequence (LCS) between them
# A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements

# Example:
# Input:
# string1 = "abcde"
# string2 = "ace"
# Output: 3

# The function below uses a 2D array to store the lengths of the longest common subsequences of substrings string1[0..i] and string2[0..j], explanation with space and time complexities below

def longestCommonSubsequence(string1: str, string2: str) -> int:
    length1, length2 = len(string1), len(string2)
    # Initialize a 2D array dp of size (length1+1)*(length2+1)
    dp = [[0] * (length2 + 1) for _ in range(length1 + 1)]

    # Loop i from 1 to length1 and j from 1 to length2
    for i in range(1, length1 + 1):
        for j in range(1, length2 + 1):
            # If characters are common, increment the value of dp[i][j] by 1
            if string1[i - 1] == string2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            # Otherwise, take the maximum of dp[i-1][j] and dp[i][j-1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Return dp[length1][length2]
    return dp[length1][length2]


# Example usage:
string1 = "abcde"
string2 = "ace"
print(longestCommonSubsequence(string1, string2))
# Expected Output: 3


# Explanation:
# The dp array is initialized with zeros.
# The outer loop iterates over each character in string1, and the inner loop iterates over each character in string2
# If string1[i-1] is equal to string2[j-1], it means that the current characters in both strings are the same, and hence, the count of LCS (Longest Common Subsequence) till now will increase by 1
# Otherwise, the count of LCS will be the maximum of the count obtained by excluding the current character of string1 or string2
# Finally, dp[length1][length2] will give the length of LCS of string1 and string2


# Space Complexity:
# We are using a 2D array of size (length_text1+1)*(length_text2+1) where length_text1 and length_text2
# are the lengths of text1 and text2 respectively. So, the space complexity is O(length_text1*length_text2)

# Time Complexity:
# We are looping through each character of text1 and text2, and for each pair of characters, we are doing
# a constant amount of work. So, the time complexity is O(length_text1*length_text2)
