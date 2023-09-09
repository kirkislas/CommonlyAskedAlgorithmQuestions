# Mid Level Question

# Problem Statement:
# Write a function that rotates a list of integers to the right by a given number of steps

# The function rotates an input list of integers to the right by an input integer, code explanation with space and time complexity below

def rotate(nums: [int], k: int) -> None:
    # Adjust k to be within the range of the list length
    k %= len(nums)
    # Rotates the list to the right, nums[k:] + nums[:k] would rotate it left
    nums[:] = nums[-k:] + nums[:-k]


nums_list = [1, 2, 3, 4, 5, 6, 7]
rotate(nums_list, 3)
print(nums_list)  # Expected output: [5,6,7,1,2,3,4]

# Explanation:

# First, we adjust k to ensure it's within the bounds of the list's length (using the modulo operator)
# Next, we modify the list in place to rotate it:
# nums[-k:] gets the last k elements of the list
# nums[:-k] gets all elements of the list except the last k
# By concatenating these two slices, we achieve the desired rotation

# Space Complexity: O(n)
# Although we modify the list in place, slicing creates temporary lists. In the worst case (for example: k=1), both slices combined will hold all n elements of the original list

# Time Complexity: O(n)
# Both slicing and list concatenation operations have a linear time complexity in the size of the resulting list. Since the total length of the concatenated result is n, the overall time complexity is O(n)
