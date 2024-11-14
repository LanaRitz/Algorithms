def depth_first_print(graph, source, result=None):
    if result is None:
        result = []

    result.append(source)

    for neighbor in graph[source]:
        depth_first_print(graph, neighbor, result)

    return result