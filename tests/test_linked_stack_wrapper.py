import pytest
from src.stacks.linked_stack_wrapper import Stack

def test_push_operation():
    # Test if elements are added to the stack correctly
    stack = Stack()
    stack.push(10)
    stack.push(20)
   