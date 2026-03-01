from queues.list_queue import ListQueue
from queues.linked_queue import LinkedQueue
from queues.doubly_linked_list_queue import DLLQueue

print("Testing Queue using List:")
q1 = ListQueue()
q1.enqueue(1)
q1.enqueue(2)
q1.enqueue(3)
print("Front:", q1.front())
print("Removed:", q1.dequeue())
print("Front after dequeue:", q1.front())

print("\nTesting Queue using Linked List:")
q2 = LinkedQueue()
q2.enqueue(10)
q2.enqueue(20)
print("Front:", q2.front())
print("Removed:", q2.dequeue())

print("\nTesting Queue using Deque:")
q3 = DLLQueue()
q3.enqueue(100)
q3.enqueue(200)
print("Front:", q3.front())
print("Removed:", q3.dequeue())