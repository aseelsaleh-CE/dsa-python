import pytest
from queues.list_queue import ListQueue  

@pytest.fixture
def l_queue():
      return ListQueue()

def test_enqueue_list(l_queue):
    l_queue.enqueue("First")
    l_queue.enqueue("Second")

def test_dequeue_list(l_queue):
    l_queue.enqueue(1)
    l_queue.enqueue(2)
    val = l_queue.dequeue()
    assert val == 1
    assert l_queue.size == 1
    assert l_queue.items == [2]