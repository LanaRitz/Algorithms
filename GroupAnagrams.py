################### O(n * (klogk))

def merge_sort(arr):   # O(klogk)  k - длина строки
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    sorted_arr = []

    while left and right:
        if left[0] < right[0]:
            sorted_arr.append(left.pop(0))
        else:
            sorted_arr.append(right.pop(0))

    sorted_arr.extend(left or right)

    return sorted_arr

def group_anagrams_merge(strs):
    anagrams = {}

    for s in strs: # O(n)  n - количество строк
        sorted_str = ''.join(merge_sort(list(s)))  # O(k)  k - длина строки

        if sorted_str not in anagrams:   # O(1)
            anagrams[sorted_str] = []

        anagrams[sorted_str].append(s)

    return list(anagrams.values())

def print_original_vector(vector):
    print("Original Vector:", vector)

def print_group_anagrams(grouped_anagrams):
    print("Grouped Vectors:", grouped_anagrams)

def test_cases():
    print("Typical Case\n")
    vector_1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print_original_vector(vector_1)
    grouped_1 = group_anagrams_merge(vector_1)
    print_group_anagrams(grouped_1)

    print("\nEmpty Input\n")
    vector_2 = []
    print_original_vector(vector_2)
    grouped_2 = group_anagrams_merge(vector_2)
    print_group_anagrams(grouped_2)

    print("\nSingle Word\n")
    vector_3 = ["hello"]
    print_original_vector(vector_3)
    grouped_3 = group_anagrams_merge(vector_3)
    print_group_anagrams(grouped_3)

    print("\nAll Words are Anagrams\n")
    vector_4 = ["abc", "bca", "cab", "bac"]
    print_original_vector(vector_4)
    grouped_4 = group_anagrams_merge(vector_4)
    print_group_anagrams(grouped_4)

    print("\nNo Anagrams\n")
    vector_5 = ["abc", "def", "ghi"]
    print_original_vector(vector_5)
    grouped_5 = group_anagrams_merge(vector_5)
    print_group_anagrams(grouped_5)

    print("\nWords of Different Lengths\n")
    vector_6 = ["abc", "de", "f", "cba", "ed"]
    print_original_vector(vector_6)
    grouped_6 = group_anagrams_merge(vector_6)
    print_group_anagrams(grouped_6)

    print("\nCase Sensitivity\n")
    vector_7 = ["b", "B", "bb", "aB", "Ab", "bB"]
    print_original_vector(vector_7)
    grouped_7 = group_anagrams_merge(vector_7)
    print_group_anagrams(grouped_7)

    print("\nSpecial Characters and Numbers\n")
    vector_8 = ["123", "321", "!@#", "#@!", "abc", "bca"]
    print_original_vector(vector_8)
    grouped_8 = group_anagrams_merge(vector_8)
    print_group_anagrams(grouped_8)

    print("\nDuplicates in the Input\n")
    vector_9 = ["eat", "tea", "eat", "ate"]
    print_original_vector(vector_9)
    grouped_9 = group_anagrams_merge(vector_9)
    print_group_anagrams(grouped_9)

    print("\nLong Words\n")
    vector_10 = ["character", "charter", "caterhr", "rachetr", "tracehr"]
    print_original_vector(vector_10)
    grouped_10 = group_anagrams_merge(vector_10)
    print_group_anagrams(grouped_10)

test_cases()


