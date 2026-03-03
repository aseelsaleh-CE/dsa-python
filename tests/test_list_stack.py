import pytest
from src.stacks.list_stack import ListStack


def test_push():
    s = ListStack()
    s.push(1)
    assert s.size() == 1


def test_pop_single_element():
    s = ListStack()
    s.push('A')
    popped_value = s.pop()
    assert popped_value == 'A'
    assert s.is_empty() is True


def test_peek_functionality():
    s = ListStack()
    s.push('Python')
    assert s.peek() == 'Python'
    assert s.size() == 1


def test_clear_stack():
    s = ListStack()
    s.push(10)
    s.push(20)
    s.push(30)
    assert s.size() == 3
    
    s.clear()
    
    assert s.size() == 0
    assert s.is_empty() is True
    assert s.peek() is None
