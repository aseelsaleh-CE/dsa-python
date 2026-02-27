import pytest
from stacks.linked_stack import LinkedStack 
@pytest.fixture
def stack():
    return LinkedStack()

def test_push(stack):
    stack.push(10)
    assert stack.count == 1

def test_pop(stack):
    stack.push(10)
    assert stack.pop() == 10

def test_peek(stack):
    stack.push(50)
    assert stack.peek() == 50

def test_is_empty(stack):
    assert stack.is_empty() is True

def test_stack_size(stack):
    assert stack.size() == 0
    
    stack.push(10)
    stack.push(20)
    assert stack.size() == 2
    
    stack.pop()
    assert stack.size() == 1
    
    stack.pop()
    assert stack.size() == 0


    
def test_stack_clear(stack):
    stack.push(10)
    stack.push(20)
    stack.push(30)
    assert stack.size() == 3
    
    stack.clear()
    
    assert stack.size() == 0
    assert stack.is_empty() is True
    assert stack.top is None
    assert stack.peek() is None
