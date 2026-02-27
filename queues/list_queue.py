from typing import List, TypeVar, Generic

T = TypeVar('T')

class ListQueue(Generic[T]):
    def __init__(self) -> None:
        self.items: List[T] = []
    
    
    @property
    def size(self) -> int:
        return len(self.items)
    
    def is_empty(self) -> bool:
        return len(self.items) == 0
    
    def enqueue(self, item: T) -> None:
        self.items.append(item)

    def dequeue(self) -> T:
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.items.pop(0)
    
    def clear(self):
        self.items = []