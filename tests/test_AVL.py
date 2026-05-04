from src.trees.avl_tree import AVLTree

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