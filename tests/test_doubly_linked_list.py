import pytest
from linked_lists.doubly_linked_list import DoublyLinkedList


def test_insert_at_head():
    dll = DoublyLinkedList()

    dll.insert_at_head("B")
    assert dll.head.data == "B"
    assert dll.tail.data == "B"

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


def test_insert_at_middle():
    dll = DoublyLinkedList()
    dll.insert_at_tail("A")
    dll.insert_at_tail("C")
    dll.insert_at("B", 1)

    assert dll.head.data == "A"
    assert dll.head.next.data == "B"
    assert dll.tail.data == "C"
    assert dll.head.next.next == dll.tail
    assert dll.tail.prev.data == "B"
    assert dll.tail.prev.prev == dll.head
    assert dll.head.prev is None
    assert dll.tail.next is None
    assert len(dll) == 3


def test_delete_by_value():
    dll = DoublyLinkedList()
    dll.insert_at_tail("A")
    dll.insert_at_tail("B")
    dll.insert_at_tail("C")
    
    assert dll.delete("B") is True
    assert len(dll) == 2
    assert dll.head.next.data == "C"
    assert dll.tail.prev.data == "A"
    
    assert dll.delete("A") is True
    assert dll.head.data == "C"
    assert dll.head.prev is None
    assert len(dll) == 1
    
    assert dll.delete("C") is True
    assert dll.head is None
    assert dll.tail is None
    assert len(dll) == 0
    
    assert dll.delete("Z") is False
    assert len(dll) == 0


def test_delete_from_empty_list():
    dll = DoublyLinkedList()
    assert dll.delete(10) is False


def test_get_at_functionality():
    dll = DoublyLinkedList()
    
    assert dll.get_at(0) is None
    
    dll.insert_at_tail("Python")
    dll.insert_at_tail("Java")
    dll.insert_at_tail("C++")
    
    assert dll.get_at(0) == "Python"
    assert dll.get_at(1) == "Java"
    assert dll.get_at(2) == "C++"
    
    assert dll.get_at(3) is None
    assert dll.get_at(-1) is None


def test_contains_logic():
    dll = DoublyLinkedList()
    
    assert dll.contains("Python") is False
    
    dll.insert_at_tail("Data")
    dll.insert_at_tail("Structures")
    dll.insert_at_tail("Lab")
    
    assert dll.contains("Data") is True        
    assert dll.contains("Structures") is True  
    assert dll.contains("Lab") is True         
    assert dll.contains("Java") is False
    assert dll.contains("data") is False  


def test_print_forward(capsys):
    dll = DoublyLinkedList()
    dll.insert_at_tail(10)
    dll.insert_at_tail(20)
    dll.insert_at_tail(30)
    
    dll.print_forward()
    
    captured = capsys.readouterr()
    assert captured.out.strip() == "10 <-> 20 <-> 30"


def test_print_empty(capsys):
    dll = DoublyLinkedList()
    dll.print_forward()
    
    captured = capsys.readouterr()
    assert captured.out.strip() == "Empty List"


def test_print_backward(capsys):
    dll = DoublyLinkedList()
    dll.insert_at_tail(10)
    dll.insert_at_tail(20)
    dll.insert_at_tail(30)
    
    dll.print_backward()
    
    captured = capsys.readouterr()
    assert captured.out.strip() == "30 <-> 20 <-> 10"


def test_print_backward_empty(capsys):
    dll = DoublyLinkedList()
    dll.print_backward()
    
    captured = capsys.readouterr()
    assert captured.out.strip() == "Empty List"