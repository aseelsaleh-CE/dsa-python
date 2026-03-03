import pytest
from src.stacks.linked_stack import LinkedStack 

def test_push():
    # Test adding an element to the stack
    stack = LinkedStack()
    stack.push(10)
    assert stack.count == 1

# def test_pop():
#     # Test removing the top element
#     stack = LinkedStack()
#     stack.push(10)
#     assert stack.pop() == 10

def test_is_empty():
    # Test checking if a new stack is empty
    stack = LinkedStack()
    assert stack.is_empty() is True
    stack.push(1)
    assert stack.is_empty() is False