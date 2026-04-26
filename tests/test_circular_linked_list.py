import pytest
from src.linked_lists.circular_linked_list import CircularLinkedList


# -------------------------
# Basic state tests
# -------------------------

def test_new_list_is_empty():
    cll = CircularLinkedList()
    assert cll.is_empty() is True
    assert cll.head is None
    assert cll.tail is None
    assert cll.size == 0


# -------------------------
# Insert tests
# -------------------------

def test_insert_single_element():
    cll = CircularLinkedList()
    cll.insert(10)

    assert cll.length() == 1
    assert cll.head == cll.tail
    assert cll.head.data == 10
    assert cll.head.next == cll.head  # circular


def test_insert_multiple_elements():
    cll = CircularLinkedList()
    values = [1, 2, 3]

    for v in values:
        cll.insert(v)

    assert cll.length() == 3
    assert cll.tail.next == cll.head

    current = cll.head
    result = []

    for _ in range(cll.length()):
        result.append(current.data)
        current = current.next

    assert result == values


# -------------------------
# Contains tests
# -------------------------

def test_contains_existing_value():
    cll = CircularLinkedList()
    cll.insert(5)
    cll.insert(10)

    assert cll.contains(5) is True
    assert cll.contains(10) is True


def test_contains_non_existing_value():
    cll = CircularLinkedList()
    cll.insert(5)

    assert cll.contains(100) is False


# -------------------------
# getAt tests
# -------------------------

def test_getAt_valid_index():
    cll = CircularLinkedList()
    cll.insert("A")
    cll.insert("B")
    cll.insert("C")

    assert cll.getAt(0) == "A"
    assert cll.getAt(1) == "B"
    assert cll.getAt(2) == "C"


def test_getAt_invalid_index():
    cll = CircularLinkedList()
    cll.insert(1)

    with pytest.raises(IndexError):
        cll.getAt(5)


# -------------------------
# Delete tests
# -------------------------

def test_delete_only_element():
    cll = CircularLinkedList()
    cll.insert(10)

    assert cll.delete(10) is True
    assert cll.length() == 0
    assert cll.head is None
    assert cll.tail is None


def test_delete_head():
    cll = CircularLinkedList()
    cll.insert(1)
    cll.insert(2)
    cll.insert(3)

    assert cll.delete(1) is True
    assert cll.length() == 2
    assert cll.head.data == 2
    assert cll.tail.next == cll.head


def test_delete_tail():
    cll = CircularLinkedList()
    cll.insert(1)
    cll.insert(2)
    cll.insert(3)

    assert cll.delete(3) is True
    assert cll.length() == 2
    assert cll.tail.data == 2
    assert cll.tail.next == cll.head


def test_delete_middle():
    cll = CircularLinkedList()
    cll.insert(1)
    cll.insert(2)
    cll.insert(3)

    assert cll.delete(2) is True
    assert cll.length() == 2
    assert cll.contains(2) is False


def test_delete_non_existing_value():
    cll = CircularLinkedList()
    cll.insert(1)
    cll.insert(2)

    assert cll.delete(100) is False
    assert cll.length() == 2


# -------------------------
# Print list tests
# -------------------------

def test_print_list_empty(capsys):
    cll = CircularLinkedList()
    cll.print_list()

    captured = capsys.readouterr()
    assert "List is empty" in captured.out


def test_print_list_non_empty(capsys):
    cll = CircularLinkedList()
    cll.insert(1)
    cll.insert(2)

    cll.print_list()
    captured = capsys.readouterr()

    assert "1 -> 2 -> (Back to Head)" in captured.out


def test_rotate_zero():
    cll = CircularLinkedList()
    cll.insert(1)
    cll.insert(2)
    cll.insert(3)

    cll.rotate(0)

    values = []
    current = cll.head
    start = cll.head

    while True:
        values.append(current.data)
        current = current.next
        if current == start:
            break

    assert values == [1, 2, 3]


def test_flatten_multiple():
    sub1 = CircularLinkedList()
    sub1.insert(2)
    sub1.insert(3)

    sub2 = CircularLinkedList()
    sub2.insert(6)

    cll = CircularLinkedList()
    cll.insert(1)
    cll.insert(sub1)
    cll.insert(4)
    cll.insert(sub2)
    cll.insert(5)

    cll.flatten()

    values = []
    current = cll.head
    start = cll.head

    while True:
        values.append(current.data)
        current = current.next
        if current == start:
            break

    assert values == [1, 2, 3, 4, 6, 5]


def test_is_circular_true():
    cll = CircularLinkedList()
    cll.insert(1)
    cll.insert(2)
    cll.insert(3)

    assert cll.is_circular() is True


def test_is_circular_empty():
    cll = CircularLinkedList()
    assert cll.is_circular() is False