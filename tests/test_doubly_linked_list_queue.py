import pytest
from queues.doubly_linked_list_queue import DLLQueue
def test_dequeue_basic():
    q = DLLQueue[str]()
    q.enqueue("A")
    q.enqueue("B")
    q.enqueue("C")
    
    assert q.dequeue() == "A"  
    assert q.dequeue() == "B"

def test_dequeue_empty_error():
    q = DLLQueue[int]()
    with pytest.raises(IndexError, match="Queue is empty"):
        q.dequeue()

def test_dequeue_to_empty():
    q = DLLQueue[int]()
    q.enqueue(100)
    
    assert q.dequeue() == 100
    assert q.is_empty() is True
    
    with pytest.raises(IndexError):
        q.dequeue()

def test_enqueue_dequeue_sequence():
    q = DLLQueue[int]()
    q.enqueue(1)
    q.dequeue()  
    q.enqueue(2)
    
    assert q.dequeue() == 2
    assert q.is_empty() is True
