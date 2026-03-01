# test_linked_list.py

import pytest
from linked_lists.linked_list import LinkedList, Node


def test_node_and_linked_list_creation():
    node = Node(10)

    assert node.data == 10
    assert node.next is None

    ll = LinkedList()

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

    assert ll.length == 1
    assert ll.head.data == 10


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
    assert ll.head.next.data == 3


def test_clear():
    ll = LinkedList()

    ll.append(1)
    ll.append(2)

    ll.clear()

    assert ll.head is None
    assert ll.length == 0


def test_contains():
    ll = LinkedList()

    ll.append("a")
    ll.append("b")

    assert ll.contains("a") is True
    assert ll.contains("z") is False


def test_index_of():
    ll = LinkedList()

    ll.append(5)
    ll.append(10)

    assert ll.index_of(10) == 1
    assert ll.index_of(5) == 0
    assert ll.index_of(999) == -1


def test_for_each_multiplication():
    ll = LinkedList()

    ll.append(10)
    ll.append(20)

    doubled = []
    ll.for_each(lambda x: doubled.append(x * 2))

    assert doubled == [20, 40]


def test_map():
    ll = LinkedList()

    ll.append(1)
    ll.append(2)
    ll.append(3)

    new_list = ll.map(lambda x: x * 2)

    current = new_list.head

    assert current.data == 2
    current = current.next
    assert current.data == 4
    current = current.next
    assert current.data == 6


def test_where():
    ll = LinkedList()

    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)

    evens = ll.where(lambda x: x % 2 == 0)

    assert evens.length == 2

    current = evens.head
    assert current.data == 2

    current = current.next
    assert current.data == 4


def test_str_representation():
    ll = LinkedList()

    ll.append(1)
    ll.append(2)

    assert str(ll) == "1 -> 2 -> None"