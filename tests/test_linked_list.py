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

def test_add_and_length():
    ll = LinkedList()
    ll.add(10)
    ll.add(20)
    ll.add(30)

    assert ll.length == 3