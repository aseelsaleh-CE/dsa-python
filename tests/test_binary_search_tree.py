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