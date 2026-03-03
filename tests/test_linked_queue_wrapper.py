import pytest
from src.queues.linked_queue_wrapper import Queue

def test_enqueue_elements():
    q = Queue()
    q.enqueue("First")
    q.enqueue("Second")
    assert q.size() == 2
    assert q.is_empty() is False

def test_dequeue_fifo_order():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    
    assert q.dequeue() == 1  
    assert q.size() == 2
    assert q.dequeue() == 2
    assert q.dequeue() == 3
    assert q.is_empty() is True

def test_peek_operation():
    q = Queue()
    q.enqueue("Apple")
    q.enqueue("Banana")
    
    assert q.peek() == "Apple"
    assert q.size() == 2  

def test_queue_clear():

    q = Queue()
    q.enqueue(100)
    q.enqueue(200)
    q.clear()
    
    assert q.size() == 0
    assert q.is_empty() is True

def test_str_representation():
    q = Queue()
    q.enqueue("A")
    q.enqueue("B")
    assert "A" in str(q)
    assert "B" in str(q)

def test_empty_queue_exceptions():
    q = Queue()
    
    with pytest.raises(IndexError, match="Dequeue from empty queue"):
        q.dequeue()
        
    with pytest.raises(IndexError, match="Peek from empty queue"):
        q.peek()
