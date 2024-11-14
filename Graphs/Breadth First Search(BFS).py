def breadth_first_print(graph, source):
    queue = [source]
    result = []
    while queue:
        current = queue.pop(0)
        result.append(current)
        for neighbor in graph[current]:
            queue.append(neighbor)
    return result


def run_tests():
    # Пример 1:
    graph1 = {
        'a': ['b', 'c'],
        'b': ['d', 'e'],
        'c': [],
        'd': [],
        'e': []
    }
    expected1 = ['a', 'b', 'c', 'd', 'e']
    result1 = breadth_first_print(graph1, 'a')
    print("Test 1 - Expected:", expected1)
    print("Test 1 - Result:", result1)
    assert result1 == expected1, "Test 1 Failed!"
    print("Test 1 Passed!\n")

    # Пример
    graph2 = {
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
    expected2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm']
    result2 = breadth_first_print(graph2, 'a')
    print("Test 2 - Expected:", expected2)
    print("Test 2 - Result:", result2)
    assert result2 == expected2, "Test 2 Failed!"
    print("Test 2 Passed!\n")



if __name__ == '__main__':
    run_tests()