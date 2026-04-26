from typing import Any, Optional


class Node:
    def __init__(self, data: Any) -> None:
        self.data = data
        self.next: Optional["Node"] = None


class CircularLinkedList:
    def __init__(self) -> None:
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None
        self.size = 0

    # -------------------------
    # Basic Helpers
    # -------------------------

    # Check if the list is empty
    def is_empty(self) -> bool:
        return self.head is None

    # Return the number of nodes in the list
    def length(self) -> int:
        return self.size

    # -------------------------
    # Insertion
    # -------------------------

    # Insert a new node at the end of the list
    def insert(self, data: Any) -> None:
        new_node = Node(data)

        if self.is_empty():
            self.head = self.tail = new_node
            new_node.next = self.head
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = self.head

        self.size += 1

    # -------------------------
    # Search Operations
    # -------------------------

    # Check if a value exists in the list
    def contains(self, value: Any) -> bool:
        if not self.head:
            return False

        current = self.head

        for _ in range(self.size):
            if current.data == value:
                return True
            current = current.next

        return False

    # Get element at a specific index
    def getAt(self, index: int) -> Any:
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")

        current = self.head

        for _ in range(index):
            current = current.next

        return current.data

    # -------------------------
    # Deletion
    # -------------------------

    # Delete first occurrence of a value
    def delete(self, value: Any) -> bool:
        if not self.head:
            return False

        prev = self.tail
        current = self.head

        for _ in range(self.size):
            if current.data == value:

                # Only one node case
                if self.size == 1:
                    self.head = self.tail = None
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

    # -------------------------
    # Display
    # -------------------------

    # Print the circular linked list safely
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

    # -------------------------
    # Advanced Operations
    # -------------------------

    # Rotate the circular linked list by k positions
    def rotate(self, k: int):
        if not self.head or k == 0:
            return

        # Calculate list length
        length = 1
        current = self.head

        while current.next != self.head:
            current = current.next
            length += 1

        # Normalize k
        k = k % length
        if k == 0:
            return

        # Move to new tail position
        current = self.head

        for _ in range(k - 1):
            current = current.next

        new_head = current.next
        new_tail = current

        # Re-link circular structure
        new_tail.next = new_head
        self.head = new_head

    # Flatten nested circular linked lists
    def flatten(self):
        if not self.head:
            return

        current = self.head

        while True:

            if isinstance(current.data, CircularLinkedList):
                sublist = current.data

                # Find sublist head and tail
                sub_head = sublist.head
                sub_tail = sublist.head

                while sub_tail.next != sublist.head:
                    sub_tail = sub_tail.next

                # Break circular structure
                sub_tail.next = None

                next_node = current.next

                # Replace current node data with sublist head data
                current.data = sub_head.data

                # Insert sublist nodes into main list
                temp = sub_head.next
                prev = current

                while temp:
                    new_node = Node(temp.data)
                    prev.next = new_node
                    prev = new_node
                    temp = temp.next

                # Connect back to main list
                prev.next = next_node

            current = current.next

            if current == self.head:
                break

    # Detect if list is circular using Floyd's Cycle Detection
    def is_circular(self) -> bool:
        if not self.head:
            return False

        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False

    # Create a deep copy of the circular linked list
    def copy_circular(self):
        if not self.head:
            return None

        new_list = CircularLinkedList()
        current = self.head

        while True:
            new_list.insert(current.data)
            current = current.next

            if current == self.head:
                break

        return new_list