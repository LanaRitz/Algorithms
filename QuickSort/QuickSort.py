import random
import time

def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]

    return quicksort(left) + [pivot] + quicksort(right)


def generate_test_data(size):
    return [random.randint(-10 ** 6, 10 ** 6) for _ in range(size)]


def run_tests():
    size = 10 ** 6
    data = generate_test_data(size)

    data_temp = data.copy()

    start = time.time()
    sorted_arr_quick = quicksort(data)
    end = time.time()
    print(f"Custom quicksort time: {end - start:.4f} seconds")

    start = time.time()
    sorted_arr_builtin = sorted(data_temp)
    end = time.time()
    print(f"Built-in sorted() time: {end - start:.4f} seconds")

    assert sorted_arr_quick == sorted_arr_builtin, "Test failed: The results do not match!"
    print("Test passed: Both sorting methods give the same result.")


run_tests()


# The built-in sorted() function in Python is implemented in C using the Timsort algorithm,
# which combines the advantages of Merge Sort and Insertion Sort.