from typing import Optional, Any

class DoublyNode:
    # Represents a node in a doubly linked list with pointers to next and previous nodes.
    def __init__(self, data: Any):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    
        def __init__(self):
            # Initializes an empty doubly linked list.
            self.head = None
            self.tail = None
            self.size = 0

        def __len__(self) -> int:
        # Returns the number of elements in the list.
            return self.size
        
        def insert_at_head(self, data) -> None:
        # Adds a new element at the beginning of the list.
            new_node = DoublyNode(data)
            if self.head is None: 
                self.head = new_node
                self.tail = new_node
    
            else:
                new_node.next = self.head
                self.head.prev = new_node 
                self.head = new_node
            self.size += 1