# Entry - Mid Level Question

# Problem Statement:
# Given a list of size n, where each element appears at least once and there's a majority element that appears more than n/2 times,
# write a function that finds and returns this majority element

# The function aims to find the majority element in a list of numbers. The majority element is the number that appears more than half the time in the list

def majority_element(nums: [int]) -> int:
    count, current_candidate = 0, None
    for num in nums:
        if count == 0:
            current_candidate = num
        count += (1 if num == current_candidate else -1)
    return current_candidate


nums_list = [3, 3, 4, 2, 4, 4, 2, 4, 4]
majority_element(nums_list)   # Expected output: 4

# Explanation:
# It utilizes the Boyer-Moore Voting Algorithm. During the iteration, if the count drops to zero, we reset our current_candidate
# This algorithm works because there is always a majority element in the list, which will eventually have the highest count by the end of the loop

# Space Complexity: O(1)
# We are only using a constant amount of extra space regardless of the input size, specifically, the count and current_candidate variables

# Time Complexity: O(n)
# We go through the list of numbers exactly once. Each operation inside the loop runs in constant time
