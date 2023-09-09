# Mid Level Question

# Problem Statement:
# Given a sorted array of integers and a target integer, implement the binary search algorithm to find the index of the target within the array
# If the target is not found in the array, return -1

# The function below takes in a sorted array (arr) & a target value (x) and demonstrates a binary search to find the index of x within arr, explanation with space and time complexities below

def binary_search(arr, x):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        # Check if x is present at mid
        if arr[mid] == x:
            return mid
        # If x is greater, ignore the left half
        elif arr[mid] < x:
            left = mid + 1
        # If x is smaller, ignore the right half
        else:
            right = mid - 1
    # If we reach here, then the element was not present
    return -1


arr = [2, 3, 4, 10, 40]
x = 10
result = binary_search(arr, x)
# expected output: 3 (10 is at index 3 in arr)

# Explanation
# The function takes a sorted array (arr) and a target value (x) as input
# It initializes two pointers, left and right, to the start and end of the array, respectively
# In a loop, it calculates the middle index of the current subarray, and compares the middle element to the target value
# If the middle element is equal to the target, it returns the middle index
# If the middle element is less than the target, it updates the left pointer to be one more than the middle index
# If the middle element is greater than the target, it updates the right pointer to be one less than the middle index
# It repeats these steps until the left and right pointers cross each other, or the target element is found
# If the pointers cross each other, it means the target element is not present in the array, and the function returns -1

# Space Complexity: O(1)
# The space consumption is constant since we're using a fixed amount of extra space

# Time Complexity: O(log n)
# The time complexity of binary search is logarithmic. At each step, we reduce the size of the array we have to search by half
