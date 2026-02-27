import pytest
from queues.list_queue import ListQueue  

@pytest.fixture
def l_queue():
      return ListQueue()

def test_enqueue_list(l_queue):
    l_queue.enqueue("First")
    l_queue.enqueue("Second")
