# Mid Level Question

# Problem Statement:
# Given a list of integers, return the list sorted in ascending order using the merge sort algorithm

# The function below takes in a list of elements (arr) and performs a merge sort on it, explanation with space and time complexities below

def merge_sort(arr):
    if len(arr) > 1:
        # Finding the mid of the array. mid = len(arr)//2 calculates the middle index of the list
        mid = len(arr)//2
        L = arr[:mid]  # Dividing the array elements into 2 halves
        R = arr[mid:]

        merge_sort(L)  # Sorting the first half
        merge_sort(R)  # Sorting the second half

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        # The first while loop merges the two halves together element by element until all the elements in one half have been merged
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):     # If there are still elements left in the L list after the first while loop, the second while loop will add them to the merged list
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):     # If there are still elements left in the R list after the first while loop, the third while loop will add them to the merged list
            arr[k] = R[j]
            j += 1
            k += 1

    return arr


arr = [12, 11, 13, 5, 6, 7]
sorted_arr = merge_sort(arr)
print(sorted_arr)

# Expected Output: [5, 6, 7, 11, 12, 13]


# Explanation:
# The merge_sort function takes a list of elements arr
# If the list has more than one element, it divides the list into two halves and recursively applies merge_sort to both halves
# Once the two halves are sorted, it merges them back together in the correct order

# Space Complexity: O(n)
# The algorithm uses extra space to create the temporary lists L and R

# Time Complexity: O(n log n)
# The list is repeatedly divided into two halves until the individual lists are small enough to be sorted directly, which takes log n divisions
# Then, the sorted sublists are repeatedly merged back together, which takes n merges. Therefore, the overall time complexity is n log n
