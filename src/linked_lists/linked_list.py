from typing import Optional, Any, Callable


class Node:
    # Represents a single node in the linked list
    def __init__(self, data: Any) -> None:
        self.data: Any = data
        self.next: Optional["Node"] = None


class LinkedList:
    # Singly Linked List implementation with utility methods

    def __init__(self) -> None:
        self.head: Optional[Node] = None
        self.length: int = 0

    # =========================
    # Basic info
    # =========================

    # Returns the number of elements in the list
    def get_length(self) -> int:
        return self.length

    # =========================
    # Insertion
    # =========================

    # Insert at the beginning (prepend)
    def add(self, data: Any) -> None:
        node = Node(data)
        node.next = self.head
        self.head = node
        self.length += 1

    # Insert at the end
    def append(self, data: Any) -> None:
        new_node = Node(data)

        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

        self.length += 1

    # Insert at a specific index
    def insert(self, index: int, data: Any) -> None:
        if not (0 <= index <= self.length):
            raise IndexError("Index out of range")

        if index == 0:
            self.add(data)
            return

        new_node = Node(data)
        current = self.head

        for _ in range(index - 1):
            current = current.next

        new_node.next = current.next
        current.next = new_node
        self.length += 1

    # Insert sorted (ascending order)
    def insert_sorted(self, data):
        new_node = Node(data)

        if not self.head or data < self.head.data:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head

        while current.next and current.next.data < data:
            current = current.next

        new_node.next = current.next
        current.next = new_node

    # =========================
    # Deletion
    # =========================

    # Remove element at index
    def remove_at(self, index: int) -> Any:
        if not (0 <= index < self.length):
            raise IndexError("Index out of range")

        if index == 0:
            removed_data = self.head.data
            self.head = self.head.next
        else:
            current = self.head

            for _ in range(index - 1):
                current = current.next

            node_to_remove = current.next
            removed_data = node_to_remove.data
            current.next = node_to_remove.next

        self.length -= 1
        return removed_data

    # Clear the entire list
    def clear(self) -> None:
        self.head = None
        self.length = 0

    # =========================
    # Search
    # =========================

    # Check if value exists
    def contains(self, value: Any) -> bool:
        current = self.head

        while current:
            if current.data == value:
                return True
            current = current.next

        return False

    # Return index of value or -1
    def index_of(self, value: Any) -> int:
        current = self.head
        index = 0

        while current:
            if current.data == value:
                return index

            current = current.next
            index += 1

        return -1

    # Get node at index (returns Node)
    def where_at(self, index: int):
        current = self.head
        current_index = 0

        while current:
            if current_index == index:
                return current

            current = current.next
            current_index += 1

        return None

    # =========================
    # Traversal / Functional
    # =========================

    # Apply function to each element
    def for_each(self, action: Callable[[Any], None]) -> None:
        current = self.head

        while current:
            action(current.data)
            current = current.next

    # Map to new list
    def map(self, transform: Callable[[Any], Any]) -> "LinkedList":
        new_list = LinkedList()
        current = self.head

        while current:
            new_list.append(transform(current.data))
            current = current.next

        return new_list

    # Filter list based on condition
    def where(self, predicate_func) -> "LinkedList":
        new_list = LinkedList()
        current = self.head

        while current:
            if predicate_func(current.data):
                new_list.append(current.data)
            current = current.next

        return new_list

    # Find middle element using slow/fast pointers
    def find_middle(self):
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    # =========================
    # Display
    # =========================

    # String representation
    def __str__(self) -> str:
        if not self.head:
            return "Empty List"

        nodes = []
        current = self.head

        while current:
            nodes.append(str(current.data))
            current = current.next

        return " -> ".join(nodes)