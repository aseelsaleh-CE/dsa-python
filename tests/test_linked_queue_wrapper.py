import pytest
from src.queues.linked_queue_wrapper import Queue

def test_enqueue_elements():
    q = Queue()
    q.enqueue("First")
    q.enqueue("Second")
    assert q.size() == 2
    assert q.is_empty() is False