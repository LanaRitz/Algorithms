import random

def prim_algorithm(graph):
    start_vertex = random.choice(list(graph.keys()))
    X = set([start_vertex])           # Множество X содержит вершины MST
    T = []                            # Рёбра минимального остовного дерева
    total_cost = 0
    while len(X) < len(graph):
        min_edge = None
        min_weight = float('inf')

        for v in X:
            for neighbor, weight in graph[v]:
                if neighbor not in X and weight < min_weight:
                    min_edge = (v, neighbor)
                    min_weight = weight

        if min_edge:
            v, w = min_edge
            X.add(w)
            T.append((v, w, min_weight))
            total_cost += min_weight

    return T, total_cost


import time

graph = {
    'A': [('B', 4), ('C', 3), ('D', 2)],
    'B': [('A', 4), ('C', 5), ('E', 10)],
    'C': [('A', 3), ('B', 5), ('D', 7), ('F', 6)],
    'D': [('A', 2), ('C', 7), ('G', 1)],
    'E': [('B', 10), ('F', 4), ('H', 8)],
    'F': [('C', 6), ('E', 4), ('G', 2)],
    'G': [('D', 1), ('F', 2), ('I', 3)],
    'H': [('E', 8), ('I', 4)],
    'I': [('G', 3), ('H', 4), ('J', 5)],
    'J': [('I', 5), ('K', 6), ('L', 9)],
    'K': [('J', 6), ('L', 9), ('M', 8)],
    'L': [('J', 9), ('K', 9), ('N', 4)],
    'M': [('K', 8), ('O', 3)],
    'N': [('L', 4), ('O', 2)],
    'O': [('M', 3), ('N', 2), ('P', 5)],
    'P': [('O', 5), ('Q', 7)],
    'Q': [('P', 7), ('R', 6)],
    'R': [('Q', 6), ('S', 4)],
    'S': [('R', 4)]
}

start_time = time.time()
mst_edges, mst_cost = prim_algorithm(graph)
end_time = time.time()

print("Ребра MST:", mst_edges)
print("Суммарная стоимость MST:", mst_cost)

print(f"Время выполнения алгоритма: {end_time - start_time} секунд")