class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1


def kruskal_union_find(V, edges):
    T = []  # остов
    uf = UnionFind(V)

    edges.sort(key=lambda x: x[2])

    for u, v, weight in edges:
        if uf.find(u) != uf.find(v):
            T.append((u, v, weight))
            uf.union(u, v)

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
mst = kruskal_union_find(V, edges)
end_time = time.time()

print("Ребра минимального остовного дерева:", mst)
print("Количество ребер минимального остовного дерева:", len(mst))
print("Время выполнения:", end_time - start_time, "секунд")
