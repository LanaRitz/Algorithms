def mwis(path_graph, weights):
    n = len(path_graph)

    # Basic cases
    if n == 0:
        return set()  # An empty set
    if n == 1:
        return {path_graph[0]}  # The only vertex

    # Recursive calls
    S_1 = mwis(path_graph[:-1], weights)  # MWIS for a graph without the last vertex
    S_2 = mwis(path_graph[:-2], weights)  # MWIS for a graph without the last two vertices

    # Calculate the total weights for S_1 and S_2 with the addition of v_n
    weight_S_1 = sum(weights[v] for v in S_1)
    weight_S_2 = sum(weights[v] for v in S_2) + weights[path_graph[-1]]

    # Returning the optimal set
    if weight_S_1 > weight_S_2:
        return S_1
    else:
        return S_2 | {path_graph[-1]}


path_graph = ['v1', 'v2', 'v3', 'v4', 'v5']

weights = {
    'v1': 4,
    'v2': 2,
    'v3': 3,
    'v4': 5,
    'v5': 6
}

result = mwis(path_graph, weights)
print("The maximum weighted independent set:", result)

max_weight = sum(weights[v] for v in result)
print("Maximum weight:", max_weight)
