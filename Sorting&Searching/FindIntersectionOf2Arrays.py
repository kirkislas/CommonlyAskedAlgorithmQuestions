# Mid Level Question

# Problem Statement:
# Given two lists of integers, return a list containing the integers which appear in both lists
# The returned list should not contain any duplicates

# This function takes two lists of integers and returns a list of integers which are present in both lists, explanation with space and time complexities below

def intersection(nums1, nums2):
    # convert both lists to sets to remove duplicates and then find the intersection of the two sets
    return list(set(nums1) & set(nums2))


nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
print(intersection(nums1, nums2))

# Expected Output: [2]

# Explanation:
# This function takes two lists of integers and returns a list of integers which are present in both lists
# By converting the lists to sets, we remove any duplicate values
# The '&' operator is used to find the intersection of the two sets
# Finally, the result is converted back to a list and returned

# Space Complexity: O(n + m)
# where n and m are the lengths of nums1 and nums2 respectively. In the worst case, all elements are distinct,
# so we would need to store all of them in the sets

# Time Complexity: O(n + m)
# Similar to the space complexity, in the worst case we need to iterate over each element in both lists, giving a time complexity of O(n + m)
