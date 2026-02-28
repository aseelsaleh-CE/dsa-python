from typing import TypeVar, Generic
from linked_lists.doubly_linked_list import DoublyLinkedList
T = TypeVar('T')

class DLLQueue(Generic[T]):
    
    def __init__(self) -> None:
        self._list: DoublyLinkedList[T] = DoublyLinkedList()

    def enqueue(self, item: T) -> None:
        self._list.insert_at_tail(item)