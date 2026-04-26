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

    # Check if list is empty
    def is_empty(self) -> bool:
        return self.head is None
    # Return list length
    def length(self) -> int:
        return self.size
    
    # Insert at end
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

    # Check if value exists
    def contains(self, value: Any) -> bool:
        if not self.head:
            return False

        current = self.head
        for _ in range(self.size):
            if current.data == value:
                return True
            current = current.next
        return False

    # Get element at index
    def getAt(self, index: int) -> Any:
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")

        current = self.head
        for _ in range(index):
            current = current.next
        return current.data

    # Delete element by value
    def delete(self, value: Any) -> bool:
        if not self.head:
            return False

        prev = self.tail
        current = self.head

        for _ in range(self.size):
            if current.data == value:
                # only one node
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

    # Print list safely
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



    def rotate(self, k: int):
        if not self.head or k == 0:
            return

        # Step 1: Calculate the length of the circular linked list
        length = 1
        current = self.head

        while current.next != self.head:
            current = current.next
            length += 1

        # Step 2: Reduce k to avoid unnecessary full rotations
        k = k % length
        if k == 0:
            return

        # Step 3: Move to the node just before the new head
        current = self.head
        for _ in range(k - 1):
            current = current.next

        # Step 4: Define new head and new tail
        new_head = current.next
        new_tail = current

        # Step 5: Maintain circular structure
        new_tail.next = new_head

        # Step 6: Update head pointer
        self.head = new_head