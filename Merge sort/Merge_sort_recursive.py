def copy_to_temp_arrays(arr, left, mid, right):
    size_l = mid - left + 1
    size_r = right - mid

    L = arr[left:left + size_l]
    R = arr[mid + 1:mid + 1 + size_r]

    return L, R


def merge_temp_arrays(arr, L, R, left):
    i, j, k = 0, 0, left
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    return i, j, k

def copy_remaining_elements(arr, L, R, i, j, k):
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1
    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1


def merge(arr, left, mid, right):
    L, R = copy_to_temp_arrays(arr, left, mid, right)

    i, j, k = merge_temp_arrays(arr, L, R, left)

    copy_remaining_elements(arr, L, R, i, j, k)


def merge_sort(arr, left, right):
    if left < right:
        mid = (left + (right - 1)) // 2

        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)
        merge(arr, left, mid, right)

    return arr



import random
import time

def get_test_lists(max_size, max_value):
    test_values = []
    for size in range(2, max_size, 1):
        test_values.append([random.randint(0, max_value) for _ in range(size)])
    return test_values

def execute_merge_sort(test_lists):
    sorted_results = []

    start = time.process_time()
    for lst in test_lists:
        lst_copy = lst[:]
        merge_sort(lst_copy, 0, len(lst_copy) - 1)
        sorted_results.append(lst_copy)
    end = time.process_time()

    print('The running time of the merge sort algorithm: ', (end - start))
    return sorted_results

def check_correctness_merge_sort(test_lists, sorted_results):
    true_results = [sorted(lst) for lst in test_lists]

    is_correct = true_results == sorted_results
    print('Correct algorithm: ', is_correct)

    return is_correct

def print_merge_sort_results(test_lists, elem, sorted_results):
    print(f'Test element: {elem}')
    print('Original list:', test_lists[elem])
    print('Sorted list using sorted():', sorted(test_lists[elem]))
    print('Sorted list using merge sort:', sorted_results[elem])

def test_case():
    test_values = get_test_lists(100, 1000)  # Настройка размера списка и максимального значения

    sorted_results = execute_merge_sort(test_values)

    if check_correctness_merge_sort(test_values, sorted_results):
        test_elem = len(test_values) - 1
        print_merge_sort_results(test_values, test_elem, sorted_results)

test_case()
