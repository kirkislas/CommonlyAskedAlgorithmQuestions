# Mid Level Question

# Problem Statement:
# Given a singly linked list, write a function to retrieve the kth to last element of the list
# The function should return the kth to last node. If the list has fewer than k nodes, return None

# This function retrieves the kth to last element of a singly linked list using a two-pointer approach, code explanation with space and time complexity below

class ListNode:     # This class defines the structure of the nodes within the linked list
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next  # This sets the next node in the linked list


def kth_to_last(head: ListNode, k: int) -> ListNode:
    first, second = head, head  # Initializing two pointers to the head of the linked list

    for _ in range(k):  # Move the first pointer k nodes ahead
        if not first:  # Check if we've reached the end of the linked list
            return None
        first = first.next  # Move the first pointer to the next node

    # Traverse the remaining list with both pointers
    while first:  # Loop until the first pointer reaches the end of the list
        # Move both pointers one step at a time
        first, second = first.next, second.next

    return second  # At this point, the second pointer points to the kth to last element

# Explanation:
# The first pointer advances k nodes from the head. If first becomes None at any point during this traversal, then the list has fewer than k nodes, and we return None
# With the first pointer k nodes ahead, both first and second pointers traverse the list simultaneously. When first reaches the end, the second pointer will be at the kth to last node
# We return the second pointer, which points to the desired kth to last node

# Space Complexity: O(1)
# The space consumption is constant since we're using a fixed amount of extra space, irrespective of the input linked list's size

# Time Complexity: O(n)
# In the worst-case scenario, we're traversing the list twice: once to move the first pointer k nodes ahead, and the second time (with both pointers) until the end. This results in a linear time complexity relative to the number of nodes (n) in the list
