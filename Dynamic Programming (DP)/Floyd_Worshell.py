import math

def floyd_warshall(graph, n):
    A = [[[math.inf] * n for _ in range(n)] for _ in range(n + 1)]

    #Получаем S между всеми вершинами v-w
    for v in range(n): # от вершины v
        for w in range(n):  # до вершины w
            if v == w:
                A[0][v][w] = 0
            elif graph[v][w] != math.inf:
                A[0][v][w] = graph[v][w]
            else:
                A[0][v][w] = math.inf

    for k in range(1, n + 1):  # количество вершин
        for v in range(n):
            for w in range(n):
                A[k][v][w] = min(A[k - 1][v][w], A[k - 1][v][k - 1] + A[k - 1][k - 1][w])

    for v in range(n):
        if A[n][v][v] < 0:
            return "Есть отрицательный цикл"

    return A[n]

#__________________________________________________________________________________________________________________________________________________________________________________
graph1 = [
    #s   u        v     w       x
    [0, 1, math.inf, math.inf, math.inf],
    [math.inf, 0, -2, math.inf, 4],
    [math.inf, math.inf, 0, -3, math.inf],
    [math.inf, -1, math.inf, 0, math.inf],
    [math.inf, math.inf, math.inf, math.inf, 0]
]

n1 = 5

graph2 = [
    # 1       2      3    4
    [0, 2, 5, math.inf],
    [math.inf, 0, 1, math.inf],
    [math.inf, math.inf, 0, -3],
    [-4, math.inf, math.inf, 0]
]

n2 = 4

graph3 = [
    # A       B      C     D
    [0, 3, 8, math.inf],
    [math.inf, 0, math.inf, 2],
    [math.inf, math.inf, 0, 1],
    [math.inf, math.inf, math.inf, 0]
]

n3 = 4

def show_result(result, n):
    if isinstance(result, str):
        print(result)
    else:
        for v in range(n):
            for w in range(n):
                print(f"dist({v + 1}, {w + 1}) = {result[v][w]}")



# Запуск алгоритма
result1 = floyd_warshall(graph1, n1)
result2  = floyd_warshall(graph2, n2)
result3 = floyd_warshall(graph3, n3)

show_result(result1, n1)
show_result(result2, n2)
show_result(result3, n3)