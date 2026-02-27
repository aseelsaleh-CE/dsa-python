from typing import List, TypeVar, Generic

T = TypeVar('T')

class ListQueue(Generic[T]):
    def __init__(self) -> None:
        self._items: List[T] = []
    def enqueue(self, item: T) -> None:
        self._items.append(item)