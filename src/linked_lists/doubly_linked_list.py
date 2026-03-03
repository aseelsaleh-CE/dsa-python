from typing import Optional, Any

class DoublyNode:
    # Represents a node in a doubly linked list
    def __init__(self, data: Any):
        self.data: Any = data
        self.next: Optional["DoublyNode"] = None
        self.prev: Optional["DoublyNode"] = None


class DoublyLinkedList:
    # Doubly linked list implementation
    def __init__(self):
        self.head: Optional[DoublyNode] = None
        self.tail: Optional[DoublyNode] = None
        self.size: int = 0