import pytest
from src.queues.list_queue import ListQueue  

def test_queue_operation():
    l_queue = ListQueue()

    assert l_queue.size() == 0
    
def test_enqueue_and_size():
    queue = ListQueue()
    queue.enqueue("A")
    queue.enqueue("B")
    assert queue.size() == 2
    assert queue.is_empty() is False

def test_dequeue_order():
    queue = ListQueue()
    queue.enqueue(1)
    queue.enqueue(2)
    assert queue.dequeue() == 1
    assert queue.dequeue() == 2
    assert queue.is_empty() is True

def test_clear_queue():
    queue = ListQueue()
    queue.enqueue(100)
    queue.clear()
    assert queue.size() == 0
    assert queue.is_empty() is True

def test_front_element():
    queue = ListQueue()
    queue.enqueue("First")
    queue.enqueue("Second")
    assert queue.front() == "First"
    assert queue.size() == 2 
