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

def test_insert_at_tail():
    dll = DoublyLinkedList()
    
    dll.insert_at_tail(10)
    dll.insert_at_tail(20)
    dll.insert_at_tail(30)
    
    assert len(dll) == 3
    assert dll.tail.data == 30
    assert dll.tail.prev.data == 20
    assert dll.head.data == 10
    assert dll.head.next.data == 20
