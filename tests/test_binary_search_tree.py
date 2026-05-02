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

def double(x):
    return x * 2

def test_map_bst():
    bst = BinarySearchTree()
    for v in [10, 5, 15]:
        bst.insert(v)

    new_tree = bst.map(double)

    assert new_tree.root.value == 20
    assert new_tree.root.left.value == 10
    assert new_tree.root.right.value == 30


def create_bst():
    tree = BinarySearchTree()
    values = [10, 5, 15, 3, 7]
    for v in values:
        tree.insert(v)
    return tree

def add(acc, x):
    return acc + x

def test_fold_sum():
    bst = create_bst()
    result = bst.fold(add, 0)
    assert result == 40


def max_func(acc, x):
    return max(acc, x)

def test_fold_max():
    bst = create_bst()
    result = bst.fold(max_func, float("-inf"))
    assert result == 15

def count(acc, x):
    return acc + 1

def test_fold_count_nodes():
    bst = create_bst()
    result = bst.fold(count, 0)
    assert result == 5

def greater_than_10(x):
    return x > 10

def test_fold_empty_tree():
    tree = BinarySearchTree()
    result = tree.fold(add, 0)
    assert result == 0

def create_binary_search_tree():
    tree = BinarySearchTree()
    values = [10, 5, 15, 3, 7, 12, 18]
    for v in values:
        tree.insert(v)
    return tree

def test_filter_greater_than_10():
    bst = create_binary_search_tree()
    result = bst.filter(greater_than_10)
    assert sorted(result) == [12, 15, 18]


def less_than_5(x):
    return x < 5

def test_filter_less_than_5():
    bst = create_binary_search_tree()
    result = bst.filter(less_than_5)
    assert result == [3]

def greater_than_100(x):
    return x > 100

def test_filter_no_match():
    bst = create_binary_search_tree()
    result = bst.filter(greater_than_100)
    assert result == []

def greater_than_0(x):
    return x > 0

def test_filter_empty_tree():
    bst = BinarySearchTree()
    result = bst.filter(greater_than_0)
    assert result == []

def test_inorder():
    bst = BinarySearchTree()
    for v in [10, 5, 15, 3, 7]:
        bst.insert(v)

    assert bst.inorder() == [3, 5, 7, 10, 15]

def test_inorder_sorted():
    bst = BinarySearchTree()
    values = [10, 5, 15, 3, 7]
    for v in values:
        bst.insert(v)

    result = bst.inorder()

    assert result == [3, 5, 7, 10, 15]

def test_inorder_single_node():
    bst = BinarySearchTree()
    bst.insert(10)

    assert bst.inorder() == [10]

def test_inorder_empty_tree():
    bst = BinarySearchTree()

    assert bst.inorder() == []

def test_preorder():
    bst = BinarySearchTree()
    for v in [10, 5, 15, 3, 7]:
        bst.insert(v)

    assert bst.preorder() == [10, 5, 3, 7, 15]

def test_postorder():
    bst = BinarySearchTree()
    for v in [10, 5, 15, 3, 7]:
        bst.insert(v)

    assert bst.postorder() == [3, 7, 5, 15, 10]

def test_postorder_single():
    bst = BinarySearchTree()
    bst.insert(10)

    assert bst.postorder() == [10]

def test_postorder_empty():
    bst = BinarySearchTree()

    assert bst.postorder() == []

def test_height():
    bst = BinarySearchTree()
    for v in [10, 5, 15, 3]:
        bst.insert(v)

    assert bst.get_height(bst.root) == 2

def test_is_balanced_true():
    bst = BinarySearchTree()
    for v in [10, 5, 15]:
        bst.insert(v)

    assert bst.is_balanced(bst.root) is True

def test_is_unbalanced():
    bst = BinarySearchTree()
    for v in [10, 5, 3, 1]:
        bst.insert(v)

    assert bst.is_balanced(bst.root) is False