from typing import Any, Optional

class Node:
    def __init__(self, data: Any) -> None:
        self.data = data
        self.next: Optional['Node'] = None

class CircularLinkedList:
    def __init__(self) -> None:
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None
        self.size = 0

    def is_empty(self) -> bool:
        return self.head is None
    
    def length(self) -> int:
        return self.size
    
    def insert(self, data: Any) -> None:
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = self.head
        self.size += 1

    def contains(self, value: Any) -> bool:
        if not self.head:
            return False
        
        current = self.head
        for _ in range(self.size):
            if current.data == value:
                return True
            current = current.next
        return False