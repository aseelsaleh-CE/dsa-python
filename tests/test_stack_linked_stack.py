import pytest
from src.stacks.linked_stack import LinkedStack 

def test_push():
    # Test adding an element to the stack
    stack = LinkedStack()
    stack.push(10)
    assert stack.count == 1

def test_is_empty():
    # Test checking if a new stack is empty
    stack = LinkedStack()
    assert stack.is_empty() is True
    stack.push(1)
    assert stack.is_empty() is False

def test_stack_size():
    # Test stack size tracking through multiple operations
    stack = LinkedStack()
    assert stack.size() == 0
    stack.push(10)
    stack.push(20)
    assert stack.size() == 2
    stack.pop()
    assert stack.size() == 1
    stack.pop()
    assert stack.size() == 0

def test_pop():
    # Test removing the top element
    stack = LinkedStack()
    stack.push(10)
    assert stack.pop() == 10
    assert stack.is_empty() is True

def test_peek():
    # Test viewing the top element without removing it
    stack = LinkedStack()
    stack.push(50)
    assert stack.peek() == 50
    assert stack.size() == 1

def test_stack_clear():

    stack = LinkedStack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    assert stack.size() == 3
    
    stack.clear()
    
    assert stack.size() == 0
    assert stack.is_empty() is True
    assert stack.top is None
    assert stack.peek() is None