from typing import Any, Optional

# Represents a node in a doubly linked list with pointers to next and previous nodes.
class DoublyNode:
    def __init__(self, data: Any):
        self.data = data
        self.next: Optional['DoublyNode'] = None
        self.prev: Optional['DoublyNode'] = None


class DoublyLinkedList:
    # Initializes an empty doubly linked list.
    def __init__(self):
        self.head: Optional[DoublyNode] = None
        self.tail: Optional[DoublyNode] = None
        self.size: int = 0

    # Returns the number of elements in the list.
    def __len__(self) -> int:
        return self.size

    # Adds a new element at the beginning of the list.
    def insert_at_head(self, data: Any) -> None:
        """
        Inserts a new node with the given data at the head of the list.
        """
        new_node = DoublyNode(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1

    # Inserts a new node with the given data at the tail.
    def insert_at_tail(self, data: Any) -> None:
        """
        Inserts a new node with the given data at the end of the list.
        """
        new_node = DoublyNode(data)
        if self.size == 0:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    # Inserts a new node with the given data at the specified index.
    def insert_at(self, data: Any, pos: int) -> None:
        """
        Inserts a new node with the given data at the specified zero-based index.
        Raises IndexError if index is out of range.
        """
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

        next_node = current.next
        new_node.prev = current
        new_node.next = next_node
        current.next = new_node
        next_node.prev = new_node

        self.size += 1

    # Deletes the first node containing the given data.
    def delete(self, data: Any) -> bool:
        """
        Deletes the first node containing the specified data.
        Returns True if deletion was successful, False otherwise.
        """
        current = self.head
        while current:
            if current.data == data:
                # Deleting head
                if current == self.head:
                    self.head = current.next
                    if self.head:
                        self.head.prev = None
                    else:
                        self.tail = None
                # Deleting tail
                elif current == self.tail:
                    self.tail = current.prev
                    if self.tail:
                        self.tail.next = None
                # Deleting middle node
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev

                self.size -= 1
                return True
            current = current.next
        return False

    # Returns the data at the specified zero-based index.
    def get_at(self, index: int) -> Optional[Any]:
        """
        Returns the data at the specified index, or None if index is out of range.
        """
        if index < 0 or index >= self.size:
            return None

        current = self.head
        for _ in range(index):
            current = current.next
        return current.data

    # Checks whether the list contains the specified data.
    def contains(self, data: Any) -> bool:
        """
        Returns True if the list contains the given data, False otherwise.
        """
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    # Prints the elements of the list from head to tail.
    def print_forward(self) -> None:
        """
        Prints the elements of the list from head to tail in '<->' format.
        """
        if self.head is None:
            print("Empty List")
            return

        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next

        print(" <-> ".join(elements))

    # Prints the elements of the list from tail to head.
    def print_backward(self) -> None:
        """
        Prints the elements of the list from tail to head in '<->' format.
        """
        if self.tail is None:
            print("Empty List")
            return

        current = self.tail
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.prev

        print(" <-> ".join(elements))