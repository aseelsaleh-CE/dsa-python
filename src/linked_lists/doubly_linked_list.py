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
    
    def insert_at_tail(self, data: Any) -> None:
        # Insert a new element at the end
        new_node = DoublyNode(data)
        if self.size == 0:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1
    
    def insert_at(self, data: Any, pos: int) -> None:
        # Insert element at a specific position
        if pos < 0 or pos > self.size:
            raise IndexError("Out of Range!")
        if pos == 0:
            self.insert_at_head(data)
            return
        if pos == self.size:
            self.insert_at_tail(data)
            return
        new_node = DoublyNode(data)
        current = self.head
        for _ in range(pos - 1):
            current = current.next
        new_node.next = current.next
        new_node.prev = current
        if current.next:
            current.next.prev = new_node
        current.next = new_node
        self.size += 1
    
    def delete(self, data: Any) -> bool:
        # Delete the first occurrence of a value
        current = self.head
        while current:
            if current.data == data:
                if current == self.head:
                    self.head = current.next
                    if self.head:
                        self.head.prev = None
                    else:
                        self.tail = None
                elif current == self.tail:
                    self.tail = current.prev
                    self.tail.next = None  
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                self.size -= 1
                return True
            current = current.next
        return False
    
    def get_at(self, index: int) -> Any:
        # Get element at a specific index
        if index < 0 or index >= self.size:
            return None
        current = self.head
        for _ in range(index):
            current = current.next  
        return current.data  


     

