import pytest
from src.linked_lists.circular_linked_list import CircularLinkedList

def test_new_list_is_empty():
    cll = CircularLinkedList()
    assert cll.is_empty() is True
    assert cll.head is None
    assert cll.tail is None
    assert cll.size == 0