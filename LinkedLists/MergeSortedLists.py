# Mid Level Question

# Problem Statement:
# Given two sorted linked lists, merge them to form a single sorted linked list

# Example Input:
# list1: 1 -> 2 -> 4
# list2: 1 -> 3 -> 4

# Expected Output After Merging:
# Result: 1 -> 1 -> 2 -> 3 -> 4 -> 4

# The merge_sorted_lists() function merges two sorted linked lists into a single sorted linked list, explanation with space and time complexities below

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_sorted_lists(list1: ListNode, list2: ListNode) -> ListNode:
    dummy_start = ListNode(-1)          # Create a dummy starting node
    current_node = dummy_start          # Point to this dummy node to start merging

    while list1 and list2:              # As long as both lists have nodes
        if list1.val <= list2.val:     # Compare the values of current nodes of the two lists
            current_node.next = list1  # Attach list1's current node to the merged list
            list1 = list1.next         # Move to the next node in list1
        else:
            current_node.next = list2  # Attach list2's current node to the merged list
            list2 = list2.next         # Move to the next node in list2

        current_node = current_node.next  # Move to the newly added node in the merged list

    # If one list is exhausted, the other still might have elements. Attach the remaining elements
    if list1:
        current_node.next = list1
    else:
        current_node.next = list2

    # Return the merged list, starting from after the dummy node
    return dummy_start.next

# Explanation:
# We initiate the merging process with a dummy node to simplify the merging
# The `current_node` pointer keeps track of where we are in the merged list
# As we iterate through list1 and list2, we compare their current nodes' values and attach the node with the smaller value to the merged list
# Once we've exhausted one list, we simply attach the remainder of the other list to the merged list

# Space Complexity: O(1)
# We use a constant amount of extra space, primarily for the dummy node and the pointers

# Time Complexity: O(n + m)
# We traverse each of the two lists at most once. With n being the length of list1 and m being the length of list2,
# our time complexity is linear in the sum of the lengths of the two input lists
