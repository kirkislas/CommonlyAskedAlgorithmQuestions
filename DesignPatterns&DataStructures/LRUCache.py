# Mid Level Question

# Problem Statement:
# Design a data structure that follows the constraints of a Least Recently Used (LRU) Cache

# The LRU (Least Recently Used) Cache algorithm demonstrated below evicts the least recently used items first when the cache reaches its limit, explanation with space and time complexities below

class ListNode:     # Doubly Linked List Node used for LRU Cache
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.previous_node = None
        self.next_node = None


class LRUCache:     # Basic implementation of an LRU Cache

    def __init__(self, capacity: int):    # Initialize the LRU Cache with given capacity
        # :param capacity: Maximum number of key-value pairs the cache can hold
        self.capacity = capacity
        self.cache_data = dict()    # Stores reference to ListNode for O(1) access

        # Initialize dummy head and tail nodes for ease of operations
        self.head = ListNode(0, 0)
        self.tail = ListNode(0, 0)
        self.head.next_node = self.tail
        self.tail.previous_node = self.head

    def _remove_node(self, node):
        # Helper function to remove a node from the linked list
        node.previous_node.next_node = node.next_node
        node.next_node.previous_node = node.previous_node

    def _add_node_to_head(self, node):
        # Helper function to add a node right after the head node
        node.next_node = self.head.next_node
        node.previous_node = self.head
        self.head.next_node.previous_node = node
        self.head.next_node = node

    def get(self, key: int) -> int:
        # Get the value for the given key from cache
        # param key: Key for which value needs to be fetched
        # return: Value corresponding to the key. Returns -1 if key not found
        if key in self.cache_data:
            node = self.cache_data[key]
            self._remove_node(node)
            self._add_node_to_head(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        # Add the given key-value pair to the cache.
        # param key: Key of the key-value pair.
        # param value: Value of the key-value pair.
        # If key already in cache, remove it
        if key in self.cache_data:
            self._remove_node(self.cache_data[key])

        # Add the new key-value pair to the cache
        new_node = ListNode(key, value)
        self._add_node_to_head(new_node)
        self.cache_data[key] = new_node

        # If cache is full, remove the least recently used item
        if len(self.cache_data) > self.capacity:
            node_to_remove = self.tail.previous_node
            self._remove_node(node_to_remove)
            del self.cache_data[node_to_remove.key]


# Sample Input and Expected Output
if __name__ == "__main__":
    # Initialize an LRU Cache with a capacity of 2
    cache = LRUCache(2)

    # Put key-value pairs into the cache
    cache.put(1, 1)
    cache.put(2, 2)

    # Get value for key 1. Expected output: 1
    print(cache.get(1))

    # This operation will kick out key 1, as the capacity is 2
    cache.put(3, 3)

    # Get value for key 2. Expected output: -1 (not found)
    print(cache.get(2))

    # Update the value for key 3
    cache.put(3, 3)

    # Get value for key 3. Expected output: 3
    print(cache.get(3))


# Explanation:
# The ListNode class represents a node in a doubly-linked list
# The LRUCache class uses a doubly-linked list to keep track of the order of elements
# The head and tail are dummy nodes in the linked list
# If an element is accessed or added, it's moved to the head of the list
# If an element needs to be removed, it's removed from the tail of the list

# Time Complexity:
# Both get and put operations are O(1) since we use a dictionary for fast lookups
# and updates and a doubly-linked list for O(1) additions/removals

# Space Complexity:
# The space complexity is O(capacity) because that's the maximum number of elements the cache can store at any time
