from typing import Optional, Callable, Any

class Node:
    def __init__(self, data: Any) -> None:
        self.data: Any = data
        self.next: Optional["Node"] = None

class LinkedList:
    def __init__(self) -> None:
        self.head: Optional[Node] = None
        self.length: int = 0

    def get_length(self) -> int:
        return self.length
    
    def add(self, data: Any) -> None:
        node = Node(data)
        node.next = self.head
        self.head = node
        self.length += 1

    def append(self, data: Any) -> None:
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

        self.length += 1

    def insert(self, index: int, data: Any) -> None:
        if index < 0 or index > self.length:
            raise IndexError("Index out of range")

        if index == 0:
            self.add(data)
            return

        new_node = Node(data)
        current = self.head

        if current is None:
            raise IndexError("Index out of range")

        for _ in range(index - 1):
            if current.next is None:
                raise IndexError("Index out of range")
            current = current.next

        new_node.next = current.next
        current.next = new_node
        self.length += 1
