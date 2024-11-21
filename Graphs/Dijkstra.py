import heapq
from collections import defaultdict


def dijkstra(graph, start):
    key = defaultdict(lambda: float('inf'))  # key[v] = shortest distance to v (default +inf)
    key[start] = 0
    len_v = {}  # Dictionary for storing the final lengths of shortest paths
    heap = []
    heapq.heappush(heap, (0, start))

    while heap:
        # Get the vertex with the minimum key
        current_dist, current_vertex = heapq.heappop(heap)

        # If the vertex has already been processed, skip it
        if current_vertex in len_v:
            continue

        # Fixing the length of the shortest path for the current vertex
        len_v[current_vertex] = current_dist

        for neighbor, weight in graph[current_vertex]:
            if neighbor not in len_v:  # If the neighbor has not been processed yet
                new_dist = current_dist + weight
                if new_dist < key[neighbor]:
                    key[neighbor] = new_dist
                    heapq.heappush(heap, (new_dist, neighbor)) # Inserting the updated value into the heap

    return len_v


graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 6)],
    'C': [('D', 3)],
    'D': []
}

start_vertex = 'A'
shortest_paths = dijkstra(graph, start_vertex)

print("Shortest distance from the vertex", start_vertex)
for vertex, distance in shortest_paths.items():
    print(f"To vertex {vertex}: {distance}")