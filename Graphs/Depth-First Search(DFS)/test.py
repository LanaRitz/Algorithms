import timeit
from iterative import depth_first_print as iterative_dfs
from recursive import depth_first_print as recursive_dfs

def run_tests():
    graph = {
        'a': ['b', 'c', 'd'],
        'b': ['e', 'f'],
        'c': ['g'],
        'd': ['h', 'i'],
        'e': [],
        'f': ['j', 'k'],
        'g': ['l'],
        'h': [],
        'i': ['m'],
        'j': [],
        'k': [],
        'l': [],
        'm': []
    }

    expected_iterative = ['a', 'd', 'i', 'm', 'h', 'c', 'g', 'l', 'b', 'f', 'k', 'j', 'e']
    expected_recursive = ['a', 'b', 'e', 'f', 'j', 'k', 'c', 'g', 'l', 'd', 'h', 'i', 'm']

    result_iterative = iterative_dfs(graph, 'a')
    if result_iterative == expected_iterative:
        print("Iterative DFS test passed!")
    else:
        print("Iterative DFS test failed.")
        print("Expected:", expected_iterative)
        print("Got:", result_iterative)

    result_recursive = recursive_dfs(graph, 'a')
    if result_recursive == expected_recursive:
        print("Recursive DFS test passed!")
    else:
        print("Recursive DFS test failed.")
        print("Expected:", expected_recursive)
        print("Got:", result_recursive)

    iterative_time = timeit.timeit(lambda: iterative_dfs(graph, 'a'), number=1000)
    recursive_time = timeit.timeit(lambda: recursive_dfs(graph, 'a'), number=1000)

    print(f"\nPerformance Comparison (1000 runs):")
    print(f"Iterative DFS time: {iterative_time:.6f} seconds")
    print(f"Recursive DFS time: {recursive_time:.6f} seconds")

    if iterative_time < recursive_time:
        print("\nIterative DFS is faster.")
    else:
        print("\nRecursive DFS is faster.")

if __name__ == '__main__':
    run_tests()
