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

    def __len__(self) -> int:
        # Returns the number of elements in the list
        return self.size

    def insert_at_head(self, data: Any) -> None:
        # Insert a new element at the beginning
        new_node = DoublyNode(data)
        if self.size == 0:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1
