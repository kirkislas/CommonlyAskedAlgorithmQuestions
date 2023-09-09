# Entry to Mid Level Concept

# Problem Statement:
# You are given two fundamental data structures: a Stack and a Queue
# Implement both using Python lists
# Describe the main differences between them and provide real-life scenarios or examples where each would be applicable
# Determine and explain the space and time complexities of your implementations

# Explanation and Demonstration of STACKS & QUEUES with their space and time complexities below

# A Stack is a data structure that follows the Last-In-First-Out (LIFO) principle
# Equal to the real life scenario of: The last guest to arrive at a party being the first to leave
# This means that the last element added to the stack is the first element to be removed
# Think of a stack as a pile of plates. You add (push) a plate to the top and remove (pop) from the top

# A Queue is a data structure that follows the First-In-First-Out (FIFO) principle
# Equal to the real life scenario of: Sending employees home based on the order of who came into work first
# This means that the first element added to the queue is the first element to be removed
# Think of a queue as a line of people waiting for the bus. The first person to arrive waits at the front and is the first to board the bus


# STACK Implementation using List:
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def size(self):
        return len(self.items)


# QUEUE Implementation using List:
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def size(self):
        return len(self.items)


# SAMPLE USAGE:
stack = Stack()
stack.push("A")
stack.push("B")
print("Stack after pushes: A, B")
print("Top of Stack:", stack.peek())  # Expected: B

queue = Queue()
queue.enqueue("1")
queue.enqueue("2")
print("\nQueue after enqueues: 1, 2")
print("Front of Queue:", queue.peek())  # Expected: 1

# Where might we use each
# Stacks - scenarios like function calls (call stacks), parsing expressions, backtracking algorithms, etc
# Queues - scenarios like order processing, task scheduling, breadth-first search in graphs, etc

# Space Complexity:
# The space complexity for both the stack and the queue is O(n), where n is the number of items stored

# Time Complexity:
# For the implementations provided:
# Stack operations (push, pop, peek, is_empty, size) all operate in O(1) time
# Queue operations (enqueue, dequeue, peek, is_empty, size):
# Enqueue is O(n) because we're inserting at the beginning of a list
# Dequeue, peek, is_empty, and size are O(1)
