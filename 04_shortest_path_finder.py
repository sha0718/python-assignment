import heapq

def dijkstra(graph, start, destination):
    """
    Finds the shortest path between two cities using Dijkstra's algorithm.
    
    :param graph: Dictionary where keys are city names and values are dictionaries of neighbors and distances.
    :param start: Starting city
    :param destination: Destination city
    :return: Tuple of (shortest path as a list, total distance)
    """
    
    # Priority queue to select the city with the minimum distance
    heap = [(0, start, [])]  # (current_distance, current_city, path_so_far)

    # Visited dictionary to keep track of the shortest distance to each city
    visited = {}

    while heap:
        (current_distance, current_city, path) = heapq.heappop(heap)

        # If this city is already visited with a shorter path, skip
        if current_city in visited:
            continue

        # Mark city as visited with the shortest distance
        visited[current_city] = current_distance
        path = path + [current_city]

        # If we've reached the destination, return the result
        if current_city == destination:
            return path, current_distance

        # Explore neighbors
        for neighbor, distance in graph[current_city].items():
            if neighbor not in visited:
                heapq.heappush(heap, (current_distance + distance, neighbor, path))

    # If destination is not reachable
    return None, float('inf')


# Example graph input
cities = {
    'A': {'B': 5, 'C': 10},
    'B': {'A': 5, 'C': 3, 'D': 9},
    'C': {'A': 10, 'B': 3, 'D': 1},
    'D': {'B': 9, 'C': 1}
}

start_city = 'A'
destination_city = 'D'

# Run the algorithm
shortest_path, total_distance = dijkstra(cities, start_city, destination_city)

# Print result
if shortest_path:
    print(f"Shortest path from {start_city} to {destination_city}: {' -> '.join(shortest_path)}")
    print(f"Total distance: {total_distance}")
else:
    print(f"No path found from {start_city} to {destination_city}.")
