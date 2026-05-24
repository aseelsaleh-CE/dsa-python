import pytest
from src.trees.heap import MinHeap

def test_insert_single():
    heap = MinHeap()
    heap.insert(10)
    assert heap.get_min() == 10

def test_multiple_inserts():
    heap = MinHeap()
    values = [10, 5, 8, 2, 7]
    for v in values:
        heap.insert(v)
    assert heap.get_min() == 2
    
    