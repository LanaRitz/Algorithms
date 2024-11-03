from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for word in strs:
            sorted_word = tuple(sorted(word))
            if sorted_word in anagrams:
                anagrams[sorted_word].append(word)
            else:
                anagrams[sorted_word] = [word]

        return list(anagrams.values())


def test_group_anagrams():
    solution = Solution()

    input_data = ["eat", "tea", "tan", "ate", "nat", "bat"]
    expected_output = [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

    output = solution.groupAnagrams(input_data)
    assert all(sorted(group) in map(sorted, expected_output) for group in output), f"Error in case 1: {output}"
    print("Result case 1:", output)

    input_data = []
    expected_output = []

    output = solution.groupAnagrams(input_data)
    assert output == expected_output, f"Error in case 2: {output}"
    print("Result case 2:", output)

    input_data = ["hello"]
    expected_output = [["hello"]]
    output = solution.groupAnagrams(input_data)
    assert output == expected_output, f"Error in case 3: {output}"
    print("Result case 3:", output)

test_group_anagrams()
