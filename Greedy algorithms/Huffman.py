import heapq  # куча (приоритетная очередь)

# узел дерева 
class Node:
    def __init__(self, symbol, frequency):
        self.symbol = symbol
        self.frequency = frequency
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.frequency < other.frequency


def huffman_tree(frequencies):
    priority_queue = []
    for symbol, freq in frequencies.items():
        node = Node(symbol, freq)
        heapq.heappush(priority_queue, node)

    while len(priority_queue) > 1:
        t1 = heapq.heappop(priority_queue)
        t2 = heapq.heappop(priority_queue)

        merged = Node(None, t1.frequency + t2.frequency)
        merged.left = t1
        merged.right = t2

        heapq.heappush(priority_queue, merged)

    return heapq.heappop(priority_queue)


def huffman_codes(root, current_code="", codes=None):
    if codes is None:
        codes = {}

    if root.symbol is not None:
        codes[root.symbol] = current_code
        return codes

    if root.left:
        huffman_codes(root.left, current_code + "0", codes)
    if root.right:
        huffman_codes(root.right, current_code + "1", codes)

    return codes


def test_large_huffman_example():
    frequencies = {
        'a': 10, 'b': 15, 'c': 30, 'd': 45, 'e': 60, 'f': 5,
        'g': 25, 'h': 35, 'i': 20, 'j': 40, 'k': 50, 'l': 55,
        'm': 65, 'n': 70, 'o': 75, 'p': 80, 'q': 85, 'r': 90,
        's': 95, 't': 100, 'u': 105, 'v': 110, 'w': 115, 'x': 120,
        'y': 125, 'z': 130, '0': 10, '1': 20, '2': 30, '3': 40,
        '4': 50, '5': 60, '6': 70, '7': 80, '8': 90, '9': 100
    }

    root = huffman_tree(frequencies)
    codes = huffman_codes(root)

    print("Коды Хаффмана:")
    for symbol, code in sorted(codes.items()):
        print(f"{symbol}: {code}")

if __name__ == "__main__":
    test_large_huffman_example()

