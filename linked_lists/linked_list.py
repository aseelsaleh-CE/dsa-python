from typing import Optional, Callable, Any

class Node:
    def __init__(self, data: Any) -> None:
        self.data: Any = data
        self.next: Optional["Node"] = None

class LinkedList:
    def __init__(self) -> None:
        self.head: Optional[Node] = None
        self.length: int = 0

    def get_length(self) -> int:
        return self.length
