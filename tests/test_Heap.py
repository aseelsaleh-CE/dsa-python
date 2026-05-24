import pytest
from src.trees.heap import MinHeap

def test_insert_single():
    heap = MinHeap()
    heap.insert(10)
    assert heap.get_min() == 10
    
    