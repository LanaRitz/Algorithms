def is_cyclic(V, T):
    visited = [False] * V # Изначально ничего не посетили

    def dfs(v, parent):
        visited[v] = True
        for u, _ in adj[v]:
            if not visited[u]:
                if dfs(u, v):
                    return True
            elif u != parent:
                return True
        return False

    adj = [[] for _ in range(V)]
    for u, v, weight in T:
        adj[u].append((v, weight))
        adj[v].append((u, weight))

    for i in range(V):
        if not visited[i]:
            if dfs(i, -1):
                return True
    return False


def kruskal_no_union_find(V, edges):
    T = []  # остов

    edges.sort(key=lambda x: x[2])

    for u, v, weight in edges:
        T.append((u, v, weight))
        if is_cyclic(V, T):
            T.remove((u, v, weight))

    return T

import random
import time

V = 1000  # Количество вершин
E = 5000  # Количество ребер

edges = []
for _ in range(E):
    u = random.randint(0, V-1)
    v = random.randint(0, V-1)
    while u == v:
        v = random.randint(0, V-1)
    weight = random.randint(1, 1000)
    edges.append((u, v, weight))

start_time = time.time()
mst = kruskal_no_union_find(V, edges)
end_time = time.time()

print("Ребра минимального остовного дерева:", mst)
print("Количество ребер минимального остовного дерева:", len(mst))
print("Время выполнения:", end_time - start_time, "секунд")