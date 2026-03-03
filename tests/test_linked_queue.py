from src.queues.linked_queue import LinkedQueue 

def test_initial_state():
    queue = LinkedQueue()
    assert queue.size == 0
    assert queue.head is None
    assert queue.tail is None
    print("test_initial_state passed!")
