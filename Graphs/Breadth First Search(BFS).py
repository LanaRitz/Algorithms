import collections

def bfs_shortest_path(graph, start, goal):
    queue = collections.deque([start])
    visited = set([start])
    parent = {start: None}

    print(f"Starting BFS from '{start}' to find shortest path to '{goal}'")

    while queue:
        vertex = queue.popleft()
        print(f"Visiting node '{vertex}', Queue: {list(queue)}")

        if vertex == goal:
            print("Goal reached!")
            break

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = vertex
                queue.append(neighbor)
                print(f"Visited '{neighbor}', added to queue with parent '{vertex}'")

    path = []
    step = goal
    while step is not None:
        path.append(step)
        step = parent[step]

    path.reverse()

    if path[0] == start:
        print(f"Shortest path from '{start}' to '{goal}': {path}")
    else:
        print(f"No path found from '{start}' to '{goal}'")

    return path if path[0] == start else None


if __name__ == '__main__':
    graph1 = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }

    print(bfs_shortest_path(graph1, 'A', 'F'))  # Ожидаемый результат: ['A', 'C', 'F']
    print(bfs_shortest_path(graph1, 'A', 'D'))  # Ожидаемый результат: ['A', 'B', 'D']
    print(bfs_shortest_path(graph1, 'A', 'A'))  # Ожидаемый результат: ['A']
    print(bfs_shortest_path(graph1, 'B', 'F'))  # Ожидаемый результат: ['B', 'E', 'F']
    print(bfs_shortest_path(graph1, 'C', 'D'))  # Ожидаемый результат: ['C', 'A', 'B', 'D']

    graph2 = {
        '1': ['2', '3'],
        '2': ['1', '4', '5'],
        '3': ['1', '6'],
        '4': ['2'],
        '5': ['2', '6'],
        '6': ['3', '5']
    }

    print(bfs_shortest_path(graph2, '1', '6'))  # Ожидаемый результат: ['1', '3', '6']
    print(bfs_shortest_path(graph2, '4', '6'))  # Ожидаемый результат: ['4', '2', '5', '6']
