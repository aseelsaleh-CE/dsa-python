from src.trees.avl_tree import AVLTree, Node

def test_avl_insert_balanced():
    avl = AVLTree()
    for v in [10, 20, 30]:  # RR case
        avl.insert(v)

    assert avl.root.value == 20
    assert avl.root.left.value == 10
    assert avl.root.right.value == 30

def test_remove_leaf():
    avl = AVLTree()
    for v in [10, 5, 15]:
        avl.insert(v)

    avl.remove(5)

    assert avl.search(5) is False

def test_remove_one_child():
    avl = AVLTree()
    for v in [10, 5, 2]:
        avl.insert(v)

    avl.remove(5)

    assert avl.search(5) is False

def test_remove_two_children():
    avl = AVLTree()
    for v in [20, 10, 30, 25, 40]:
        avl.insert(v)

    avl.remove(30)

    assert avl.search(30) is False

def test_remove_root():
    avl = AVLTree()
    for v in [10, 5, 15]:
        avl.insert(v)

    avl.remove(10)

    assert avl.search(10) is False

def test_remove_not_found():
    avl = AVLTree()
    for v in [10, 5, 15]:
        avl.insert(v)

    avl.remove(999)  # should not crash


def test_search_found():
    avl = AVLTree()
    values = [10, 5, 15, 2, 7]

    for v in values:
        avl.insert(v)

    assert avl.search(10) is True
    assert avl.search(5) is True
    assert avl.search(7) is True


def test_search_not_found():
    avl = AVLTree()
    values = [10, 5, 15]

    for v in values:
        avl.insert(v)

    assert avl.search(100) is False
    assert avl.search(-1) is False


def test_search_empty_tree():
    avl = AVLTree()
    assert avl.search(10) is False

def multiply_by_two(x: int) -> int:
    return x * 2


def add_one(x: int) -> int:
    return x + 1

def test_map_values():
    avl = AVLTree()

    for v in [10, 5, 15]:
        avl.insert(v)

    new_avl = avl.map(add_one)


def multiply(a: int, b: int) -> int:
    return a * b


def max_func(a: int, b: int) -> int:
    return max(a, b)

def test_fold_max():
    avl = AVLTree()

    for v in [10, 50, 20]:
        avl.insert(v)

    result = avl.fold(max_func, float("-inf"))

    assert result == 50

def test_fold_max():
    avl = AVLTree()

    for v in [10, 50, 20]:
        avl.insert(v)

    result = avl.fold(max_func, float("-inf"))

    assert result == 50

def is_greater_than_7(x: int) -> bool:
    return x > 7


def is_even(x: int) -> bool:
    return x % 2 == 0


def is_less_than_10(x: int) -> bool:
    return x < 10

def test_filter_greater_than_7():
    avl = AVLTree()

    for v in [10, 5, 15, 2, 7]:
        avl.insert(v)

    result = avl.filter(is_greater_than_7)

    assert sorted(result) == [10, 15]

def test_filter_even():
    avl = AVLTree()

    for v in [10, 5, 15, 2, 7, 8]:
        avl.insert(v)

    result = avl.filter(is_even)

    assert sorted(result) == [2, 8, 10]

def test_filter_less_than_10():
    avl = AVLTree()

    for v in [10, 5, 15, 2, 7]:
        avl.insert(v)

    result = avl.filter(is_less_than_10)

    assert sorted(result) == [2, 5, 7]    

def test_filter_empty_tree():
    avl = AVLTree()

    result = avl.filter(is_even)

    assert result == []

def test_inorder_sorted():
    avl = AVLTree()

    values = [10, 5, 15, 2, 7]

    for v in values:
        avl.insert(v)

    result = avl.in_order()

    assert result == [2, 5, 7, 10, 15]

def test_postorder_simple():
    avl = AVLTree()

    for v in [10, 5, 15]:
        avl.insert(v)

    result = avl.post_order()

    assert result == [5, 15, 10]

def test_preorder_simple():
    avl = AVLTree()

    for v in [10, 5, 15]:
        avl.insert(v)

    result = avl.pre_order()

    assert result == [10, 5, 15]

def test_is_balanced():
    tree = AVLTree()

    tree.root = Node(10)
    tree.root.left = Node(5)
    tree.root.right = Node(15)

    assert tree.is_balanced(tree.root) == True


def test_is_not_balanced():
    tree = AVLTree()

    tree.root = Node(10)
    tree.root.left = Node(5)
    tree.root.left.left = Node(2)

    assert tree.is_balanced(tree.root) == False