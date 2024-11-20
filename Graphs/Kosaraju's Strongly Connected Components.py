from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def _dfs(self, v, visited, stack=None):
        visited[v] = True
        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                self._dfs(neighbor, visited, stack)
        if stack is not None:
            stack.append(v)

    def _transpose(self):
        transposed_graph = Graph(self.V)
        for u in self.graph:
            for v in self.graph[u]:
                transposed_graph.add_edge(v, u)
        return transposed_graph

    def kosaraju_scc(self):
        # 1. Построить G_rev (транспонированный граф)
        transposed_graph = self._transpose()

        # 2. Отметить все вершины как неразведанные (visited = False)
        visited = [False] * self.V
        stack = []

        # 3. Выполнить TopoSort (DFS на G_rev) для определения f(v)
        for i in range(self.V):
            if not visited[i]:
                transposed_graph._dfs(i, visited, stack)

        # 4. Отметить все вершины как неразведанные (visited = False)
        visited = [False] * self.V
        scc_list = []

        # 5. Выполнить второй обход в исходном порядке f(v)
        while stack:
            v = stack.pop()
            if not visited[v]:
                component = []
                self._dfs(v, visited, component)  # DFS на исходном графе
                scc_list.append(component)

        return scc_list


if __name__ == "__main__":
    g = Graph(5)
    g.add_edge(1, 0)
    g.add_edge(0, 1)
    g.add_edge(2, 3)
    g.add_edge(0, 3)
    g.add_edge(3, 4)
    g.add_edge(4, 2)

    sccs = g.kosaraju_scc()
    print("Strongly Connected Components:", sccs)
