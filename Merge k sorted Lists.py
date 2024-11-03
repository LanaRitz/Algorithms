#O(Nlogk)

import random
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        result = []
        current = self

        while current:
            result.append(current.val)
            current = current.next

        return " -> ".join(map(str, result))


class Solution:
    def merge_k_lists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        print("Starting list:")
        for i, list in enumerate(lists):
            if list:
                print(f"list {i + 1}: {list}")
            else:
                print(f"List {i + 1}: null")

        if not lists or len(lists) == 0:
            return None

        while len(lists) > 1:
            temp = []

            for i in range(0, len(lists), 2):
                list1 = lists[i]
                list2 = lists[i + 1] if i + 1 < len(lists) else None
                temp.append(self.merge_lists(list1, list2))
            lists = temp

        print("\nSorted combined list:")
        print(lists[0])
        return lists[0]

    def merge_lists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        node = ListNode()
        ans = node

        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next

        if list1:
            node.next = list1
        else:
            node.next = list2

        return ans.next


def generate_list(length: int, start: int, end: int) -> Optional[ListNode]:
    if length <= 0:
        return None

    values = sorted(random.randint(start, end) for _ in range(length))
    head = ListNode(values[0])
    current = head

    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next

    return head


def generate_list_from_lists(num_lists: int, list_length: int, start: int, end: int) -> List[Optional[ListNode]]:
    return [generate_list(list_length, start, end) for _ in range(num_lists)]


if __name__ == '__main__':
    solution = Solution()

    num_lists = 10
    list_length = 100
    start = 0
    end = 1000

    lists = generate_list_from_lists(num_lists, list_length, start, end)

    solution.merge_k_lists(lists)
