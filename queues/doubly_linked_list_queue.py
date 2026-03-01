from typing import TypeVar, Generic
from linked_lists.doubly_linked_list import DoublyLinkedList
T = TypeVar('T')

class DLLQueue(Generic[T]):

    def __init__(self) -> None:
        self.list: DoublyLinkedList[T] = DoublyLinkedList()

    def is_empty(self) -> bool:
        return self.list.size == 0

    def enqueue(self, item: T) -> None:
        self.list.insert_at_tail(item)

    def dequeue(self) -> T:
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.list.remove_at_head() 
    

    def front(self) -> T:
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.list.head.data 
