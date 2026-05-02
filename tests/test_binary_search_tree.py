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