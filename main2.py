import math
import itertools


def distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# Function to calculate the total distance of a path
def total_distance(points, order):
    dist = 0
    for i in range(len(order) - 1):
        dist += distance(points[order[i]], points[order[i + 1]])
    return dist

#  Greedy Algorithm for TSP
def greedy_tsp(graph, start):
    num_points = len(graph)
    # Start from the given starting point
    current_point = start
    # Initialize the order of points to visit
    order = [current_point]
    # Create a list to keep track of visited points
    visited = [False] * num_points
    visited[current_point] = True

    for _ in range(num_points - 1):
        min_dist = float('inf')
        nearest_point = None
        # Find the nearest unvisited point
        for i in range(num_points):
            if not visited[i]:
                dist = graph[current_point][i]
                if dist < min_dist:
                    min_dist = dist
                    nearest_point = i
        # Mark the nearest point as visited and update current point
        visited[nearest_point] = True
        current_point = nearest_point
        order.append(current_point)

    return order, total_distance(graph, order)

# Example usage:
# Example graph representing distances between points
# Replace this with your own graph representation
graph = [
    [0, 3, 2, 4, 5],
    [3, 0, 4, 2, 3],
    [2, 4, 0, 5, 6],
    [4, 2, 5, 0, 7],
    [5, 3, 6, 7, 0]
]

# Starting point
starting_point = 0

# Find the order of visiting points and the total distance using the Greedy Algorithm
order, total_dist = greedy_tsp(graph, starting_point)

print("Order of visiting points:", order)
print("Total distance:", total_dist)
