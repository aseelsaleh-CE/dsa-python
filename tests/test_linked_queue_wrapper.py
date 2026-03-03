import pytest
from src.queues.linked_queue_wrapper import Queue

def test_queue_operations():
    q = Queue()
    q.enqueue("A")
    q.enqueue("B")

    