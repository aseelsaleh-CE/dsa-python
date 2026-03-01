# test_linked_list.py
import pytest
from linked_lists.linked_list import LinkedList , Node
def test_linked_test_creation():
    node: Node = Node(10)

    assert node.data == 10
    assert node.next is None

    ll:LinkedList = LinkedList()
    assert ll.head is None
    assert ll.length == 0
