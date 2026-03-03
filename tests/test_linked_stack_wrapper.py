import pytest
from src.stacks.linked_stack_wrapper import Stack

def test_push_operation():
    # Test if elements are added to the stack correctly
    stack = Stack()
    stack.push(10)
    stack.push(20)
    assert stack.size() == 2

def test_is_empty_and_size():
    # Test the empty state and size tracking
    stack = Stack()
    assert stack.is_empty() is True
    stack.push(5)
    assert stack.is_empty() is False
    assert stack.size() == 1

def test_pop_operation():
    # Test if the last added element is the first one to be removed (LIFO)
    stack = Stack()
    stack.push("A")
    stack.push("B")
    assert stack.pop() == "B"
    assert stack.pop() == "A"
    assert stack.is_empty() is True

def test_peek_operation():
    # Test viewing the top element without removing it
    stack = Stack()
    stack.push(100)
    stack.push(200)
    assert stack.peek() == 200
    assert stack.size() == 2  
   