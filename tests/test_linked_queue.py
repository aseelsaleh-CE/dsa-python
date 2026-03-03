from src.queues.linked_queue import LinkedQueue 

def test_initial_state():
    queue = LinkedQueue()
    assert queue.size() == 0
    assert queue.head is None
    assert queue.tail is None
    print("test_initial_state passed!")

def test_enqueue():
    queue = LinkedQueue()
    queue.enqueue(10)
    assert queue.size() == 1
    assert queue.is_empty() is False
    assert queue.head.data == 10
    assert queue.tail.data == 10

    queue.enqueue(20)
    assert queue.size() == 2
    assert queue.head.data == 10
    assert queue.tail.data == 20
    print("test_enqueue passed!")

def test_dequeue():
    queue = LinkedQueue()
    queue.enqueue("A")
    queue.enqueue("B")
    
    val = queue.dequeue()
    assert val == "A"
    assert queue.size() == 1
    assert queue.head.data == "B"
    
    val = queue.dequeue()
    assert val == "B"
    assert queue.is_empty() is True
    print("test_dequeue passed!")

def test_clear_method():
    queue = LinkedQueue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    assert queue.size() == 3
    
    queue.clear()
    
    assert queue.size() == 0
    assert queue.head is None
    assert queue.tail is None
    assert queue.is_empty() is True
    print("test_clear_method passed!")