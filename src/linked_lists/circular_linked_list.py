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
    
    def getAt(self, index: int) -> Any:
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        
        current = self.head
        for _ in range(index):
            current = current.next
        return current.data
    
    def delete(self, value: Any) -> bool:
        if not self.head:
            return False

        prev = self.tail
        current = self.head

        for _ in range(self.size):
            if current.data == value:
                if self.size == 1:
                    self.head = None
                    self.tail = None
                else:
                    prev.next = current.next
                    if current == self.head:
                        self.head = current.next
                    if current == self.tail:
                        self.tail = prev
                
                self.size -= 1
                return True
            
            prev = current
            current = current.next
            
        return False
    
    def print_list(self) -> None:
        if not self.head:
            print("List is empty")
            return

        current = self.head
        elements = []
        for _ in range(self.size):
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements) + " -> (Back to Head)")