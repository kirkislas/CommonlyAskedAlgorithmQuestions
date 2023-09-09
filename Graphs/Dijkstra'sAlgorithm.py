# High End Mid Level Question

# Problem Statement:
# Given a weighted graph and a starting node, implement Dijkstra's Algorithm to find the shortest path from the starting node to all other nodes in the graph

# Example Input:
# Graph:
# {
#    'A': {'B': 1, 'C': 4},
#    'B': {'A': 1, 'C': 2, 'D': 5},
#    'C': {'A': 4, 'B': 2, 'D': 1},
#    'D': {'B': 5, 'C': 1}
# }
# Start Node: 'A'

# Example Output:
# {'A': 0, 'B': 1, 'C': 3, 'D': 4}

# The following code is an implementation of Dijkstra's Algorithm which finds the shortest path from a starting node to all other nodes in a weighted graph, explanation with space and time complexities below

# provides functions for using lists as priority queues (used for always selecting the next node to explore based on the shortest known distance to it)
import heapq


def dijkstra(graph, start):
    # Args:
    # graph (dict): The graph represented as an adjacency list
    # start (str): The starting node
    # Returns:
    # dict: A dictionary with nodes as keys and their shortest distance from the start node as values

    # The shortest known distance from start to each node
    shortest_distance = {node: float('infinity') for node in graph}
    shortest_distance[start] = 0

    # Priority queue for nodes to check, initialized with the start node
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # If current distance is larger than recorded, skip
        if current_distance > shortest_distance[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # If this path is shorter, update shortest distance and enqueue neighbor
            if distance < shortest_distance[neighbor]:
                shortest_distance[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return shortest_distance


# Sample Usage:
if __name__ == "__main__":
    sample_graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1}
    }
    print(dijkstra(sample_graph, 'A'))


# Explanation:
# Dijkstra's algorithm is used to find the shortest path from a starting node to all other nodes
# in a weighted graph. The algorithm works by iteratively selecting the node with the shortest
# known distance from the starting node and updating the distances of its neighbors

# Space Complexity:
# O(n + m*log(m)) where n is the number of nodes and m is the number of edges in the graph
# This comes from storing shortest distances for all nodes (O(n)) and the priority queue
# which can store all edges in the worst case (O(m*log(m)) due to insertion in a binary heap)

# Time Complexity:
# O(n*log(n) + m*log(n)) where n is the number of nodes and m is the number of edges in the graph
# The reason is that every node is inserted into the priority queue once (O(n*log(n))) and
# each edge is considered once (O(m*log(n)) because in the worst case we can insert every edge into the priority queue)
