from typing import Any, Optional

class Node:
    def __init__(self, data: Any):
        # Store data of any type and a reference to the next node
        self.data: Any = data 
        self.next: Optional['Node'] = None 

class LinkedQueue:
    def __init__(self) -> None:
        # Initialize an empty linked queue with head, tail, and count
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None
        self.size: int = 0