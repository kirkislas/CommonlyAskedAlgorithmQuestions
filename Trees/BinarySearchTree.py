# High End Mid Level Question

# Problem Statement:
# Implement a basic Binary Search Tree (BST) that supports insertion, deletion, and lookups

# Requirements:
# The BST should be able to insert values
# The BST should be able to delete values
# The BST should be able to search for a value and return a boolean indicating its presence
# Define a TreeNode structure that should have references to its left child, right child, and a value

# This is a simple implementation of a binary search tree with methods for insertion, deletion, and lookups. Explanation with space and time complexity below

class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def search(root, key):
    # Base Cases: root is null or key is present at root
    if root is None or root.val == key:
        return root

    # Key is greater than root's key
    if root.val < key:
        return search(root.right, key)

    # Key is smaller than root's key
    return search(root.left, key)


def insert(root, key):
    # If the tree is empty, assign a new node address to the root
    if root is None:
        return TreeNode(key)

    # Otherwise, recur down the tree
    if key < root.val:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)

    # return the (unchanged) node pointer
    return root


def minValueNode(root):
    current = root
    # loop down to find the leftmost leaf
    while (current.left is not None):
        current = current.left

    return current


def deleteNode(root, key):

    # Base Case
    if root is None:
        return root

    # If the key to be deleted is smaller than the root's
    # key then it lies in the left subtree
    if key < root.val:
        root.left = deleteNode(root.left, key)

    # If the key to be delete is greater than the root's key
    # then it lies in the right subtree
    elif (key > root.val):
        root.right = deleteNode(root.right, key)

    # If key is same as root's key, then this is the node
    # to be deleted
    else:

        # Node with only one child or no child
        if root.left is None:
            temp = root.right
            root = None
            return temp

        elif root.right is None:
            temp = root.left
            root = None
            return temp

        # Node with two children: Get the inorder successor
        # (smallest in the right subtree)
        temp = minValueNode(root.right)

        # Copy the inorder successor's content to this node
        root.val = temp.val

        # Delete the inorder successor
        root.right = deleteNode(root.right, temp.val)

    return root


# Using the functions created above
root = None
keys = [20, 8, 22, 4, 12, 10, 14]

# Construct the BST
for key in keys:
    root = insert(root, key)

# Search in the BST
key = 10
found_node = search(root, key)

if found_node:
    print(f"Node with key {key} found in the tree.")
else:
    print(f"Node with key {key} not found in the tree.")

# Delete a node from the BST
key = 8
root = deleteNode(root, key)

# Search in the BST
key = 8
found_node = search(root, key)

if found_node:
    print(f"Node with key {key} found in the tree.")
else:
    print(f"Node with key {key} not found in the tree.")

# Expected output: Node with key 10 found in the tree. Node with key 8 not found in the tree.

# Explanation:
# TreeNode: A class that initializes a node with a given key, with left and right children set to None
# search(): A function that searches for a key in the binary search tree rooted at a given node. If the key is present, it returns the node. Otherwise, it returns None.
# insert(): A function that inserts a key into the binary search tree rooted at a given node and returns the root of the modified tree.
# minValueNode(): A helper function that returns the node with the minimum value in a binary search tree.
# deleteNode(): A function that deletes a key from the binary search tree rooted at a given node and returns the root of the modified tree.

# Space & Time Complexities: O(h) for all functions, which is the recursive call stack space
# They all have a worst-case scenario of traversing through the height of the tree, which results in a time and space complexity of O(h)
