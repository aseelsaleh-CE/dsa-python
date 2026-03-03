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
    
    def get_length(self) -> int:
        """Returns the total number of elements in the list."""
        return self.length
    
    def add(self, data: Any) -> None:
        """Inserts a new element at the beginning of the list (Prepend)."""
        node = Node(data)
        node.next = self.head
        self.head = node
        self.length += 1

    def append(self, data: Any) -> None:
        """Adds a new element to the end of the list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.length += 1
