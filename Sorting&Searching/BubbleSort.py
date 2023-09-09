# Entry Level Question

# Problem Statement:
# Given an unsorted list of integers, implement the Bubble Sort algorithm to sort the list in ascending order

# The function below takes in an array (arr) and it will sort it by bubbling the smaller elements to the top of the list, explanation with space and time complexities below

def bubbleSort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place, no need to check them
        for j in range(0, n-i-1):
            # Traverse the array from 0 to n-i-1. Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


arr = [64, 34, 25, 12, 22, 11, 90]
bubbleSort(arr)
print(arr)

# Expected Output: [11, 12, 22, 25, 34, 64, 90]

# Explanation:
# Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in the wrong order
# It's similar to when you slowly ascend to the surface of the water, bubbles of air form and ascend to the surface
# The smaller elements rise to the top of the list in this same way

# Space Complexity: O(1)
# It's a in-place sorting algorithm, no additional space is needed except for the temporary variable used for swapping

# Time Complexity: O(n^2)
# The algorithm runs two nested loops over the dataset, the outer loop runs n times and the inner loop runs n times for each iteration of the outer loop, giving a worst-case time complexity of O(n^2)
