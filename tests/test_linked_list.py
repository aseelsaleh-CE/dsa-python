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

def test_append_and_length():
    ll = LinkedList()
    ll.append(10)
    ll.append(20)
    ll.append(30)
    assert ll.length == 3

def test_insert_at_beginning():
    ll = LinkedList()
    ll.insert(0, 10)

def test_insert_invalid_index():
    ll = LinkedList()
    with pytest.raises(IndexError):
        ll.insert(5, 100)

def test_remove_at():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    removed = ll.remove_at(1)
    assert removed == 2
    assert ll.length == 2
    
def test_clear():
    ll =LinkedList()
    ll.append(1)
    ll.append(2)
    ll.clear()