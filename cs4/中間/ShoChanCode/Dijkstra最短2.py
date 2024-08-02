import heapq

def dijkstra(graph, start):
    # Priority queue to hold the vertices to visit, initialized with the start node
    queue = [(0, start)]
    heapq.heapify(queue)

    # Dictionary to hold the minimum distance to all nodes, initialized to infinity for all nodes except the start node
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0

    # Dictionary to hold the "previous node" information to reconstruct the path later
    previous_nodes = {node: None for node in graph}

    while queue:
        # Get the node in the queue with the smallest distance (priority queue)
        current_distance, current_node = heapq.heappop(queue)

        # Explore the neighbors of the current node
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            # If a shorter path to the neighbor is found
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(queue, (distance, neighbor))

    return distances, previous_nodes

def find_least_cost_path(graph, start, end):
    distances, previous_nodes = dijkstra(graph, start)
    path = []
    current_node = end

    # Reconstruct the path from end to start
    while current_node is not None:
        path.insert(0, current_node)
        current_node = previous_nodes[current_node]

    return path, distances[end]

# Define the graph
graph = {
    'u': {'a': 5, 'c': 11},
    'b': {'a': 6, 'd': 2, 'e': 13},
    'a': {'u': 5, 'c': 3, 'b': 6},
    'd': {'b': 2, 'c': 4, 'e': 5},
    'e': {'b': 13, 'd': 5},
    'c': {'u': 11, 'a': 3, 'd': 4},
}

# Find the least cost path from node u to each other node
distances_from_u = {}
for node in graph:
    if node != 'u':
        path, cost = find_least_cost_path(graph, 'u', node)
        distances_from_u[node] = cost

# Sort nodes based on their distances from 'u'
sorted_nodes = sorted(distances_from_u.items(), key=lambda x: x[1])

# Display the result
sorted_nodes.insert(0, ('u', 0))  # Adding 'u' with distance 0 at the beginning
print("Nodes sorted by least distance from 'u':")
for node, distance in sorted_nodes:
    print(f"Node {node}: {distance}")
