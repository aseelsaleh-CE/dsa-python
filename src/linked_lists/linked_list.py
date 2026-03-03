from typing import Optional, Any, Callable

class Node:
    """Represents a single node in the linked list."""
    def __init__(self, data: Any) -> None:
        self.data: Any = data
        self.next: Optional["Node"] = None


class LinkedList:
    """Singly Linked List implementation with utility methods."""

    def __init__(self) -> None:
        self.head: Optional[Node] = None
        self.length: int = 0
