from typing import TypeVar, Generic
T = TypeVar('T')
class Node(Generic[T]):
    def __init__(self,data : T):
        self.data = data 
        self.next :Node = None 

class LinkedQueue (Generic[T]):
    def __init__(self):
        self.head :Node = None
        self.tail:Node = None
        self.size :int = 0

    def is_empty(self) -> bool:
        return self.head is None

    def size(self) -> int:
        return self.size

    def enqueue(self, item: T) -> None:
        new_node = Node(item)
        if self.tail:
            self.tail.next = new_node
        self.tail = new_node
        if self.head is None:
            self.head = self.tail
        self.size += 1

    
    def dequeue(self) -> T:
        if self.is_empty():
            raise IndexError("Queue is empty")
        data: T = self.head.data 
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        self.size -= 1
        return data
    
    def clear(self):
        self.head = None
        self.tail = None
        self.size = 0
