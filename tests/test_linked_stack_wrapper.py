import pytest
from src.stacks.linked_stack_wrapper import Stack

def test_push_operation():
    # Test if elements are added to the stack correctly
    stack = Stack()
    stack.push(10)
    stack.push(20)

def test_is_empty_and_size():
    # Test the empty state and size tracking
    stack = Stack()
    assert stack.is_empty() is True
    stack.push(5)
    assert stack.is_empty() is False
    assert stack.size() == 1
   