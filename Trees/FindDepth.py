# Mid Level Question

# Problem Statement:
# Given the root of a binary tree, determine its maximum depth
# The maximum depth or height of a tree is the number of nodes along the longest path from the root node down to the farthest leaf node

# The function maxDepth(node) below calculates the depth of a binary tree, explanation with space and time compexity below

class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def maxDepth(node):
    if node is None:
        return 0
    else:
        # Compute the depth of each subtree
        l_depth = maxDepth(node.left)
        r_depth = maxDepth(node.right)

        # Use the larger one
        if l_depth > r_depth:
            return l_depth + 1
        else:
            return r_depth + 1


# Example Usage
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print("Height of tree is %d" % (maxDepth(root)))

# Explanation
# The maxDepth function calculates the depth of a binary tree
# The depth of a binary tree is the maximum distance from the root node to any leaf node
# It recursively calculates the depth of the left and right subtrees of a node and
# returns the maximum of these depths plus one for the current node

# Space Complexity: O(h)
# Where h is the height of the tree. This space is required for the system stack during the recursive calls

# Time Complexity: O(n)
# Where n is the number of nodes in the tree, as each node is visited once
