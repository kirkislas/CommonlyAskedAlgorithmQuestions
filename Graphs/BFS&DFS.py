# Mid Level Question

# Problem Statement:
# Implement a graph data structure and provide methods to perform Breadth-First Search (BFS) and Depth-First Search (DFS) traversals on it
# The graph should be represented using an adjacency list

# Example Input:
# Graph edges: (0,1), (0,2), (1,2), (2,0), (2,3), (3,3)
# Start vertex for BFS and DFS: 2

# Expected Output:
# Breadth First Traversal (starting from vertex 2): 2 0 3 1
# Depth First Traversal (starting from vertex 2): 2 0 1 3

# Below is an example of Breadth-First Search and Depth First Search for a graph, explanation with space and time complexities below

# used in this example for convenience, as it allows for automatic initialization of keys that don't already exist in the dictionary; making it easier to add edges to the graph
from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def BFS(self, s):
        visited = [False] * (max(self.graph) + 1)
        queue = []
        queue.append(s)
        visited[s] = True

        while queue:
            s = queue.pop(0)
            print(s, end=" ")

            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

    def DFS(self, s, visited=None):
        if visited is None:
            visited = [False] * (max(self.graph) + 1)
        visited[s] = True
        print(s, end=" ")

        for i in self.graph[s]:
            if visited[i] == False:
                self.DFS(i, visited)


# Example Usage
g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

print("Breadth First Traversal (starting from vertex 2):")
g.BFS(2)

print("\nDepth First Traversal (starting from vertex 2):")
g.DFS(2)

# Explanation:
# The Graph class contains methods for adding edges and performing BFS and DFS
# The BFS method traverses the graph in a breadth-first manner. It uses a queue to keep track of vertices to visit
# The DFS method traverses the graph in a depth-first manner. It uses a recursive approach

# Space Complexity:
# For BFS: O(V), where V is the number of vertices in the graph
# For DFS: O(V), where V is the number of vertices in the graph

# Time Complexity:
# For BFS: O(V+E), where V is the number of vertices and E is the number of edges in the graph
# For DFS: O(V+E), where V is the number of vertices and E is the number of edges in the graph
