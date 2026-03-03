import pytest
from src.stacks.list_stack import ListStack 
def test_push():
    s = ListStack()
    s.push(1)
    assert s.size() == 1