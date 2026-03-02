import pytest
from linked_lists.doubly_linked_list import DoublyLinkedList


def test_insert_at_head():
    dll = DoublyLinkedList()

    # Insert first element
    dll.insert_at_head("B")
    assert dll.head.data == "B"
    assert dll.tail.data == "B"

    # Insert second element at head
    dll.insert_at_head("A")
    assert dll.head.data == "A"
    assert dll.head.next.data == "B"
    assert dll.tail.data == "B"
    assert dll.tail.prev.data == "A"
    assert len(dll) == 2