def knapsack(values, sizes, capacity):
    n = len(values)
    A = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for c in range(capacity + 1):
            if sizes[i - 1] <= c:
                A[i][c] = max(A[i - 1][c], A[i - 1][c - sizes[i - 1]] + values[i - 1])
            else:
                A[i][c] = A[i - 1][c]

    return A[n][capacity], A


def reconstruct_solution(A, values, sizes, capacity):
    n = len(values)
    S = [] # предметы, которые выбрали
    c = capacity

    for i in range(n, 0, -1):
        if sizes[i - 1] <= c and A[i][c] == A[i - 1][c - sizes[i - 1]] + values[i - 1]:
            S.append(i - 1)
            c -= sizes[i - 1]

    return S


import random

n = 10
values = [random.randint(50, 200) for _ in range(n)]
sizes = [random.randint(10, 50) for _ in range(n)]
capacity = 100

max_value, A = knapsack(values, sizes, capacity)
selected_items = reconstruct_solution(A, values, sizes, capacity)
selected_values = [values[i] for i in selected_items]

print(f"Максимальная стоимость: {max_value}")
print(f"Выбранные предметы (индексы): {selected_items}")
print(f"Стоимость выбранных предметов: {selected_values}")
