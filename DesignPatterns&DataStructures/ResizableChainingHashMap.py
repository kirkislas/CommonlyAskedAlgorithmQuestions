# High End Mid Level Question

# Problem Statement:
# Design and implement a hash map that supports the following operations:
# put(key, value): Insert or update a key-value pair into the hash map. If the value already exists, update the old value
# get(key): Returns the value to which the specified key is mapped or -1 if this map contains no mapping for the key
# remove(key): Removes the mapping of the specified value key if this map contains the mapping for the key
# Your hash map should handle potential collisions by implementing separate chaining
# Additionally, ensure that the hash map dynamically resizes itself when its load factor exceeds a specific threshold (e.g., 0.7)


# The following implementation is a demonstration of a hash map with Separate Chaining and Dynamic Resizing, Explanation with space and time complexities below

class ListNode:
    # A node for a singly-linked list used for Separate Chaining in our HashMap
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashMap:
    # A basic implementation of a HashMap with Separate Chaining and Dynamic Resizing

    def __init__(self, capacity=1000):
        self.capacity = capacity  # Total buckets in the HashMap
        self.data = [None] * capacity  # The HashMap data
        self.size = 0  # Number of key-value pairs

    def _hash(self, key):
        # Generate a hash for the given key
        return hash(key) % self.capacity

    def put(self, key, value):
        # Store a key-value pair into the HashMap
        index = self._hash(key)
        if not self.data[index]:
            # No collision, create a new entry
            self.data[index] = ListNode(key, value)
        else:
            # Collision occurred, use Separate Chaining
            current = self.data[index]
            while True:
                if current.key == key:
                    # Key already exists, update its value
                    current.value = value
                    return
                if not current.next:
                    break
                current = current.next
            # Append new key-value pair to the end of the list
            current.next = ListNode(key, value)
        self.size += 1

        # Check for resizing up
        if self.size / self.capacity > 0.7:
            self._resize(self.capacity * 2)

    def get(self, key):
        # Retrieve the value associated with the given key
        index = self._hash(key)
        current = self.data[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def remove(self, key):
        # Remove the key-value pair associated with the given key
        index = self._hash(key)
        current = self.data[index]
        prev = None
        while current:
            if current.key == key:
                if prev:
                    prev.next = current.next
                else:
                    # This is the head of the list
                    self.data[index] = current.next
                self.size -= 1

                # Check for resizing down
                if self.size / self.capacity < 0.2:
                    self._resize(self.capacity // 2)
                return
            prev, current = current, current.next

    def _resize(self, new_capacity):
        # Resize the HashMap to the new capacity and rehash all key-value pairs
        old_data = self.data
        self.data = [None] * new_capacity
        self.capacity = new_capacity
        self.size = 0
        for head in old_data:
            current = head
            while current:
                self.put(current.key, current.value)
                current = current.next


# Explanation:
# The HashMap class uses Separate Chaining to handle hash collisions
# Each bucket in the hash map contains a linked list of key-value pairs
# The hash function (_hash) determines the bucket where a key-value pair will be stored
# The put method inserts or updates a key-value pair
# The get method retrieves a value by its key
# The remove method deletes a key-value pair by its key
# The _resize method is used to dynamically resize the hash map based on the load factor

# Time Complexity:
# The average-case time complexity for put, get, and remove operations is O(1)
# However, in worst-case scenarios (like when there are many hash collisions),
# the time complexity can degrade to O(n) where n is the number of key-value pairs in a bucket

# Space Complexity:
# The space complexity is O(capacity + size), where capacity is the number of buckets in the hash map
# and size is the number of key-value pairs
