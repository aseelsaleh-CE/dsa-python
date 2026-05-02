from src.trees.BST import BinarySearchTree


def test_insert_root():
    bst = BinarySearchTree()
    bst.insert(10)

    assert bst.root is not None
    assert bst.root.value == 10


def test_insert_multiple():
    bst = BinarySearchTree()
    values = [10, 5, 15, 2, 7]

    for v in values:
        bst.insert(v)

    assert bst.root.value == 10
    assert bst.root.left.value == 5
    assert bst.root.right.value == 15
    assert bst.root.left.left.value == 2
    assert bst.root.left.right.value == 7

def test_remove_leaf_node():
    bst = BinarySearchTree()
    values = [10, 5, 15, 2, 7]

    for v in values:
        bst.insert(v)

    bst.remove(2)

    assert bst.root.left.left is None

def test_remove_one_child():
    bst = BinarySearchTree()
    values = [10, 5, 15, 2]

    for v in values:
        bst.insert(v)

    bst.remove(5)

    assert bst.root.left.value == 2
    
       
def test_remove_two_children():
    bst = BinarySearchTree()
    values = [10, 5, 15, 2, 7, 12, 20]

    for v in values:
        bst.insert(v)

    bst.remove(5)

    assert bst.root.left.value == 7
    assert bst.root.left.left.value == 2
    assert bst.root.left.right is None

def test_remove_root():
    bst = BinarySearchTree()
    values = [10, 5, 15]

    for v in values:
        bst.insert(v)

    bst.remove(10)

    assert bst.root.value != 10

def test_search_non_existing_value():
    bst = BinarySearchTree()
    values = [10, 5, 15]

    for v in values:
        bst.insert(v)

    assert bst.search(100) is False
    assert bst.search(0) is False

def test_search_empty_tree():
    bst = BinarySearchTree()

    assert bst.search(10) is False

def test_search_after_multiple_inserts():
    bst = BinarySearchTree()
    values = [50, 30, 70, 20, 40, 60, 80]

    for v in values:
        bst.insert(v)

    assert bst.search(20) is True
    assert bst.search(80) is True
    assert bst.search(100) is False

def test_map_bst():
    bst = BinarySearchTree()
    for v in [10, 5, 15]:
        bst.insert(v)

    new_tree = bst.map(lambda x: x * 2)

    assert new_tree.root.value == 20
    assert new_tree.root.left.value == 10
    assert new_tree.root.right.value == 30


def create_bst():
    tree = BinarySearchTree()
    values = [10, 5, 15, 3, 7]
    for v in values:
        tree.insert(v)
    return tree


def test_fold_sum():
    bst = create_bst()
    result = bst.fold(lambda acc, x: acc + x, 0)
    assert result == 40


def test_fold_max():
    bst = create_bst()
    result = bst.fold(lambda acc, x: max(acc, x), float("-inf"))
    assert result == 15


def test_fold_count_nodes():
    bst = create_bst()
    result = bst.fold(lambda acc, x: acc + 1, 0)
    assert result == 5


def test_fold_empty_tree():
    tree = BinarySearchTree()
    result = tree.fold(lambda acc, x: acc + x, 0)
    assert result == 0