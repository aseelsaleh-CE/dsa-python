import pytest
from src.linked_lists.circular_linked_list import CircularLinkedList


def test_insert_and_cycle():
    cll = CircularLinkedList()
    cll.append(1)
    cll.append(2)
    assert cll.head.next.next == cll.head