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

    # -------------------------
    # Utility
    # -------------------------

    # Return number of elements in the list
    def __len__(self) -> int:
        return self.size

    # -------------------------
    # Insertion
    # -------------------------

    # Insert at the beginning
    def insert_at_head(self, data: Any) -> None:
        new_node = DoublyNode(data)

        if self.size == 0:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        self.size += 1

    # Insert at the end
    def insert_at_tail(self, data: Any) -> None:
        new_node = DoublyNode(data)

        if self.size == 0:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

        self.size += 1

    # Insert at a specific position
    def insert_at(self, data: Any, pos: int) -> None:
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

    # -------------------------
    # Deletion
    # -------------------------

    # Delete first occurrence of a value
    def delete(self, data: Any) -> bool:
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

    # Remove node at a specific index
    def remove_at(self, index: int):
        if not self.head:
            return

        if index == 0:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            self.size -= 1
            return

        current = self.head
        i = 0

        while current and i < index:
            current = current.next
            i += 1

        if not current:
            return

        if current.prev:
            current.prev.next = current.next

        if current.next:
            current.next.prev = current.prev

        self.size -= 1

    # -------------------------
    # Search
    # -------------------------

    # Get element at index
    def get_at(self, index: int) -> Any:
        if index < 0 or index >= self.size:
            return None

        current = self.head

        for _ in range(index):
            current = current.next

        return current.data

    # Check if value exists
    def contains(self, data: Any) -> bool:
        current = self.head

        while current:
            if current.data == data:
                return True
            current = current.next

        return False

    # -------------------------
    # Display
    # -------------------------

    # Print list from head to tail
    def print_forward(self) -> None:
        if not self.head:
            print("Empty List")
            return

        current = self.head
        elements = []

        while current:
            elements.append(str(current.data))
            current = current.next

        print(" <-> ".join(elements))

    # Print list from tail to head
    def print_backward(self) -> None:
        if not self.tail:
            print("Empty List")
            return

        current = self.tail
        elements = []

        while current:
            elements.append(str(current.data))
            current = current.prev

        print(" <-> ".join(elements))

    # -------------------------
    # Functional operations
    # -------------------------

    # Apply function to each element and return new list
    def map(self, transform_func):
        new_list = DoublyLinkedList()
        current = self.head

        while current:
            new_list.insert_at_tail(transform_func(current.data))
            current = current.next

        return new_list

    # Reduce list into a single value
    def fold(self, combine_func, initial):
        result = initial
        current = self.head

        while current:
            result = combine_func(result, current.data)
            current = current.next

        return result

    # Split list into two lists at index
    def split_at(self, index):
        first = DoublyLinkedList()
        second = DoublyLinkedList()

        current = self.head
        i = 0

        while current and i < index:
            first.insert_at_tail(current.data)
            current = current.next
            i += 1

        while current:
            second.insert_at_tail(current.data)
            current = current.next

        return first, second