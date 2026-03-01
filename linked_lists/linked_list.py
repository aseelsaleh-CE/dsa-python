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

    def remove_at(self, index: int) -> Any:
        if index < 0 or index >= self.length:
            raise IndexError("Index out of range")

        if self.head is None:
            raise IndexError("List is empty")

        if index == 0:
            removed_data = self.head.data
            self.head = self.head.next
            self.length -= 1
            return removed_data

        current = self.head

        for _ in range(index - 1):
            if current.next is None:
                raise IndexError("Index out of range")
            current = current.next

        node_to_remove = current.next
        if node_to_remove is None:
            raise IndexError("Index out of range")

        current.next = node_to_remove.next
        self.length -= 1
        return node_to_remove.data
    
    def clear(self) -> None:
        self.head = None
        self.length = 0

    def contains(self, value: Any) -> bool:
        current = self.head
        while current is not None:
            if current.data == value:
                return True
            current = current.next
        return False
    
    def index_of(self, value: Any) -> int:
        current = self.head
        index = 0
        while current is not None:
            if current.data == value:
                return index
            current = current.next
            index += 1
        return -1
    
    def for_each(self, action:Any) -> None:
        current = self.head
        while current is not None:
            action(current.data)
            current = current.next

    def map(self, transform: Any) -> LinkedList:
        new_list = LinkedList()
        current = self.head
        while current is not None:
            new_list.append(transform(current.data))
            current = current.next
        return new_list
    
    def where(self, test:Any) -> LinkedList:
        new_list = LinkedList()
        current = self.head
        while current is not None:
            if test(current.data):
                new_list.append(current.data)
            current = current.next
        return new_list
    
    def __str__(self) -> str:
        if self.head is None:
            return "Empty List"

        nodes: list[str] = []
        current = self.head

        while current is not None:
            nodes.append(str(current.data))
            current = current.next

        return " -> ".join(nodes) + " -> None"