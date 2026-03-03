import pytest
from src.linked_lists.circular_linked_list import CircularLinkedList

def test_new_list_is_empty():
    cll = CircularLinkedList()
    assert cll.is_empty() is True
    assert cll.head is None
    assert cll.tail is None
    assert cll.size == 0

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


