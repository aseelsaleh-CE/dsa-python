from typing import Optional, Any

class DoublyNode:
    # Represents a node in a doubly linked list with pointers to next and previous nodes.
    def __init__(self, data: Any):
        self.data = data
        self.next: Optional[DoublyNode] = None
        self.prev: Optional[DoublyNode] = None

    class DoublyLinkedList:
    
        def __init__(self):
            # Initializes an empty doubly linked list.
            self.head: Optional[DoublyNode] = None
            self.tail: Optional[DoublyNode] = None
            self.size: int = 0
        def __len__(self) -> int:
        # Returns the number of elements in the list.
            return self.size