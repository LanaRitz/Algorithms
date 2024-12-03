class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = TreeNode(value)
        if not self.root:
            self.root = new_node
        else:
            current = self.root
            while True:
                if value < current.value:
                    if not current.left:
                        current.left = new_node
                        break
                    current = current.left
                else:
                    if not current.right:
                        current.right = new_node
                        break
                    current = current.right

    def search(self, value):
        current = self.root
        while current:
            if value == current.value:
                return True
            elif value < current.value:
                current = current.left
            else:
                current = current.right
        return False

    def delete(self, value):
        if self.search(value):
            def _delete_node(node, value):
                if not node:
                    return None
                if value < node.value:
                    node.left = _delete_node(node.left, value)
                elif value > node.value:
                    node.right = _delete_node(node.right, value)
                else:
                    if not node.left and not node.right:
                        return None
                    elif not node.left:
                        return node.right
                    elif not node.right:
                        return node.left
                    else:
                        min_larger_node = self._find_min(node.right)
                        node.value = min_larger_node.value
                        node.right = _delete_node(node.right, min_larger_node.value)
                return node

            self.root = _delete_node(self.root, value)

    def _find_min(self, node):
        while node.left:
            node = node.left
        return node

    def _find_max(self, node):
        while node.right:
            node = node.right
        return node

    def in_order_traversal(self):
        result = []

        def _in_order(node):
            if node:
                _in_order(node.left)
                result.append(node.value)
                _in_order(node.right)

        _in_order(self.root)
        return result

    def pre_order_traversal(self):
        result = []

        def _pre_order(node):
            if node:
                result.append(node.value)
                _pre_order(node.left)
                _pre_order(node.right)

        _pre_order(self.root)
        return result

    def post_order_traversal(self):
        result = []

        def _post_order(node):
            if node:
                _post_order(node.left)
                _post_order(node.right)
                result.append(node.value)

        _post_order(self.root)
        return result

    def height(self):
        def _height(node):
            if not node:
                return 0
            return 1 + max(_height(node.left), _height(node.right))

        return _height(self.root)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def initialize_tree(values):
    tree = BinarySearchTree()
    for value in values:
        tree.insert(value)
    return tree
def print_test_header(test_name):
    print(f"=== Тестирование метода {test_name} ===")
def insert_and_print(tree, values):
    for value in values:
        print(f"\nВставка значения {value}:")
        tree.insert(value)
        print_tree(tree.root)
def print_tree(node, level=0, prefix="Root: "):
    if node:
        print(" " * (level * 4) + prefix + str(node.value))
        if node.left or node.right:
            print_tree(node.left, level + 1, "L--- ")
            print_tree(node.right, level + 1, "R--- ")

def test_insert():
    print_test_header("insert")

    test_values = [50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 45, 55, 65, 75, 85]
    print(f"Вставляем значения: {test_values}")

    tree = BinarySearchTree()
    insert_and_print(tree, test_values)

    print("\n=== Тестирование завершено ===")

def test_search():
    print_test_header("search")

    tree = BinarySearchTree()
    test_values = [50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 45, 55, 65, 75, 85]
    print(f"Вставляем значения: {test_values}")

    tree = BinarySearchTree()
    insert_and_print(tree, test_values)

    search_values = [25, 100, 40, 85, 15]

    results = []
    for value in search_values:
        result = tree.search(value)
        results.append((value, result))

    print("\nРезультаты поиска:")
    for value, result in results:
        if result:
            print(f"Значение {value} найдено в дереве.")
        else:
            print(f"Значение {value} не найдено в дереве.")

    print("\n=== Тестирование завершено ===")

def test_delete():
    print_test_header("delete")

    test_values = [50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 45, 55, 65, 75, 85]
    print(f"Вставляем значения: {test_values}")

    tree = BinarySearchTree()
    insert_and_print(tree, test_values)

    print("\nДерево после вставки:")
    print_tree(tree.root)

    delete_values = [20, 70, 40, 10, 100]
    print(f"\nМассив значений для удаления: {delete_values}")

    for value in delete_values:
        print(f"\nУдаляем значение: {value}")
        tree.delete(value)
        print_tree(tree.root)

    print("\n=== Тестирование завершено ===")

def test_find_min():
    print_test_header("find_min")

    test_values = [10, 5, 3, 1, 15, 12, 20]
    print(f"Вставляем значения: {test_values}")

    tree = BinarySearchTree()
    insert_and_print(tree, test_values)

    min_node = tree._find_min(tree.root)
    print(f"Minimum node value: {min_node.value}")

    print("\n=== Тестирование завершено ===")

def test_find_max():
    print_test_header("find_max")

    test_values = [10, 5, 3, 1, 100, 12, 20]
    print(f"Вставляем значения: {test_values}")

    tree = BinarySearchTree()
    insert_and_print(tree, test_values)

    max_node = tree._find_max(tree.root)
    print(f"Maximum node value: {max_node.value}")

    print("\n=== Тестирование завершено ===")

def test_in_order_traversal():
    print_test_header("in_order_traversal")

    test_values = [50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 45, 55, 65, 75, 85]
    print(f"Вставляем значения: {test_values}")

    tree = BinarySearchTree()
    insert_and_print(tree, test_values)

    print("\nРезультат обхода в симметричном порядке:")
    in_order_result = tree.in_order_traversal()
    print(in_order_result)

    print(f"Ожидаемый результат:\n {sorted(test_values)}")

    print("\n=== Тестирование завершено ===")

def test_pre_order_traversal():
    print_test_header("pre_order_traversal")

    test_values = [50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 45, 55, 65, 75, 85]
    print(f"Вставляем значения в дерево: {test_values}")

    tree = BinarySearchTree()
    insert_and_print(tree, test_values)

    print("\nРезультат обхода в предварительном порядке:")
    pre_order_result = tree.pre_order_traversal()
    print(pre_order_result)

    print(f"\nОжидаемый результат: "
          f"\n[50, 30, 20, 10, 25, 40, 35, 45, 70, 60, 55, 65, 80, 75, 85]")

    print("\n=== Тестирование завершено ===")

def test_post_order_traversal():
    print_test_header("post_order_traversal")

    test_values = [50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 45, 55, 65, 75, 85]
    print(f"Вставляем значения в дерево: {test_values}")

    tree = BinarySearchTree()
    insert_and_print(tree, test_values)

    print("\nРезультат обхода в постпорядке:")
    post_order_result = tree.post_order_traversal()
    print(post_order_result)

    print(f"\nОжидаемый результат: \n"
          f"[10, 25, 20, 35, 45, 40, 30, 55, 65, 60, 75, 85, 80, 70, 50]")

    print("\n=== Тестирование завершено ===")

def test_height():
    print_test_header("height")

    test_values = [50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 45, 55, 65, 75, 85]
    print(f"Вставляем значения в дерево: {test_values}")

    tree = BinarySearchTree()
    insert_and_print(tree, test_values)

    tree_height = tree.height()
    print(f"\nВысота дерева: {tree_height}")

    print(f"\nОжидаемая высота: 4")

    print("\n=== Тестирование завершено ===")



# Запуск тестовых функций----------------------------------------------------------------------------------------------------------------------------------------------
#test_height()
#test_post_order_traversal()
#test_pre_order_traversal()
#test_in_order_traversal()
#test_find_max()
#test_find_min()
#test_delete()
#test_search()
test_insert()
