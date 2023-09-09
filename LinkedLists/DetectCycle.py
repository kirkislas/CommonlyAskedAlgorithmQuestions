# Mid Level Question

# Problem Statement:
# Determine if a given singly-linked list contains a cycle using Floyd's cycle-finding algorithm

# This function checks if a linked list has a cycle using Floyd's cycle-finding algorithm, explanation with space and time complexity below

class ListNode:   # This class defines the structure of the nodes within the linked list
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next  # This sets the next node in the linked list

# Each node has a value (val) and a reference to the next node (next). This structure allows us to chain nodes together to form a linked list


# Creating the linked list A -> B -> C -> D -> E -> F -> None

A = ListNode("A")
B = ListNode("B")
C = ListNode("C")
D = ListNode("D")
E = ListNode("E")
F = ListNode("F")

A.next = B
B.next = C
C.next = D
D.next = E
E.next = F


# Function that checks if a linked list has a cycle using Floyd's cycle-finding algorithm

def has_cycle(head: ListNode) -> bool:
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


# Expected Output: False (will return True if repeat list node appears)

has_cycle(E)


# Explanation:
# The two pointers, slow & fast, traverse the list. slow moves one node at a time, while fast moves two
# If there's a cycle, fast will eventually catch up to slow & they'll point to the same node
# If there's no cycle, fast will reach the end of the list

# Space Complexity: O(1)
# Only a constant amount of space is used regardless of the size of the input linked list

# Time Complexity: O(n)
# In the worst case scenario, the fast pointer traverses the list twice as fast as the slow pointer and we will go through the list in a linear fashion
