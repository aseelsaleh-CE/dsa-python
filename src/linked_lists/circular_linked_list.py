from typing import Any, Optional

class Node:
    def __init__(self, data: Any) -> None:
        self.data = data
        self.next: Optional['Node'] = None
        
class CircularLinkedList:
    def __init__(self) -> None:
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None
        self.size = 0

    def is_empty(self) -> bool:
        return self.head is None