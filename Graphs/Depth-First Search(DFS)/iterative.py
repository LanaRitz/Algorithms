def depth_first_print(graph, source):
    stack = [source]
    result = []

    while stack:
        current = stack.pop()
        result.append(current)

        for neighbor in graph[current]:
            stack.append(neighbor)

    return result