import pytest
from src.stacks.linked_stack import LinkedStack 

def test_push():
    # Test adding an element to the stack
    stack = LinkedStack()
    stack.push(10)
    assert stack.count == 1
