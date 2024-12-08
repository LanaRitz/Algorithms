def merge_sort(jobs):
    if len(jobs) <= 1:
        return jobs

    mid = len(jobs) // 2
    left = merge_sort(jobs[:mid])
    right = merge_sort(jobs[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    while left and right:
        key_left = (left[0][0] - left[0][1], left[0][0])
        key_right = (right[0][0] - right[0][1], right[0][0])

        if key_left > key_right:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    result.extend(left if left else right)
    return result

def greedy_diff(jobs): #Список задач, где каждая задача представлена как (вес, длина).
    print("\n--- Шаг 1: Сортировка задач ---")
    sorted_jobs = merge_sort(jobs)
    print(f"Отсортированные задач: {sorted_jobs}")

    weighted_completion_time = 0
    current_time = 0

    for weight, length in sorted_jobs:
        current_time += length
        weighted_completion_time += weight * current_time

    return weighted_completion_time


import random

def test_greedy_diff():
    num_jobs = 1000
    max_weight = 100
    max_length = 50
    jobs = [(random.randint(1, max_weight), random.randint(1, max_length)) for _ in range(num_jobs)]

    print("=== Тестирование функции greedy_diff ===")
    print(f"Количество задач: {num_jobs}")
    print(f"Данные: {jobs}")

    weighted_completion_time = greedy_diff(jobs)
    print("\n--- Шаг 2: Вычисление итогового времени ---")
    print(f"Взвешенное завершенное время: {weighted_completion_time}")


test_greedy_diff()
