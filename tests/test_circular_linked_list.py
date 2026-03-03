import pytest
from src.linked_lists.circular_linked_list import CircularLinkedList

def test_new_list_is_empty():
    cll = CircularLinkedList()
    assert cll.is_empty() is True
    assert cll.head is None
    assert cll.tail is None
    assert cll.size == 0


def test_append_first_node():
    cll = CircularLinkedList()
    cll.append(10)

    assert cll.is_empty() is False
    assert cll.head is not None
    assert cll.tail is not None
    assert cll.head == cll.tail
    assert cll.head.data == 10
    assert cll.head.next == cll.head  # circular reference
    assert cll.size == 1


def test_append_second_node():
    cll = CircularLinkedList()
    cll.append(10)
    cll.append(20)

    assert cll.head.data == 10
    assert cll.tail.data == 20
    assert cll.tail.next == cll.head
    assert cll.head.next == cll.tail
    assert cll.size == 2


def test_append_multiple_nodes_and_circularity():
    cll = CircularLinkedList()
    values = [1, 2, 3, 4]

    for v in values:
        cll.append(v)

    assert cll.size == 4
    assert cll.tail.next == cll.head

    # traverse once and collect values
    current = cll.head
    result = []

    for _ in range(cll.size):
        result.append(current.data)
        current = current.next

    assert result == values
    assert current == cll.head  # confirms circular loop


def test_is_empty_after_appends():
    cll = CircularLinkedList()
    cll.append("A")
    cll.append("B")

    assert cll.is_empty() is False
