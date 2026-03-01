import pytest
from queues.doubly_linked_list_queue import DLLQueue
def test_dll_queue_front():
    q = DLLQueue[int]()
    q.enqueue(5)
    q.enqueue(10)
   
