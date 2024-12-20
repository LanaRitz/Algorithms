class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)


if __name__ == "__main__":
    uf = UnionFind(1000)

    uf.union(1, 2)
    uf.union(2, 3)
    uf.union(4, 5)

    print(uf.connected(1, 3))  # True, так как 1 и 3 в одном множестве
    print(uf.connected(1, 4))  # False, так как 1 и 4 в разных множествах

    uf.union(3, 4)
    print(uf.connected(1, 5))  # True, после объединения 3 и 4
