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
        self.count: int = 0

    def is_empty(self) -> bool:
        # Return True if the queue has no nodes
        return self.head is None

    def size(self) -> int:
        # Return the current number of elements in the queue
        return self.count
    
    def enqueue(self, item: Any) -> None:
        # Add a new node with data to the end of the queue
        new_node = Node(item)
        if self.tail:
            self.tail.next = new_node
        self.tail = new_node
        if self.head is None:
            self.head = self.tail
        self.count += 1

    def dequeue(self) -> Any:
        # Remove and return the data from the front node
        if self.is_empty():
            raise IndexError("Queue is empty")
        
        # We know head is not None because of is_empty check
        data: Any = self.head.data 
        self.head = self.head.next
        
        if self.head is None:
            self.tail = None
            
        self.count -= 1
        return data
    
    def clear(self) -> None:
        # Reset the queue to an empty state
        self.head = None
        self.tail = None
        self.count = 0
    
    def front(self) -> Any:
        # Return the data of the first node without removing it
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.head.data
    

