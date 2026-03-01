from typing import Optional, Any, Callable

class Node:
    # Represents a single node in the linked list.
    def __init__(self, data: Any) -> None:
        self.data: Any = data
        self.next: Optional["Node"] = None

class LinkedList:
    
    def __init__(self) -> None:
        # Initializes an empty LinkedList.
        self.head: Optional[Node] = None
        self.length: int = 0

    def get_length(self) -> int:
        # Returns the total number of elements in the list.
        return self.length
    
    def add(self, data: Any) -> None:
        # Inserts a new element at the beginning of the list (Prepend).
        node = Node(data)
        node.next = self.head
        self.head = node
        self.length += 1

    def append(self, data: Any) -> None:
        # Adds a new element to the end of the list.
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.length += 1

    def insert(self, index: int, data: Any) -> None:
        # Inserts an element at a specific index.
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

    def remove_at(self, index: int) -> Any:
        # Removes and returns the element at the specified index.
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
    
    def clear(self) -> None:
        # Removes all elements from the list.
        self.head = None
        self.length = 0

    def contains(self, value: Any) -> bool:
        # Checks if a specific value exists within the list.
        current = self.head
        while current:
            if current.data == value:
                return True
            current = current.next
        return False
    
    def index_of(self, value: Any) -> int:
        # Returns the index of the first occurrence of the value, or -1 if not found.
        current = self.head
        index = 0
        while current:
            if current.data == value:
                return index
            current = current.next
            index += 1
        return -1
    
    def for_each(self, action: Any) -> None:
        # Applies a given function to each element in the list.
        current = self.head
        while current:
            action(current.data)
            current = current.next

    def map(self, transform: Any) -> LinkedList:
        # Creates a new list by transforming each element with the provided function.
        new_list = LinkedList()
        current = self.head
        while current:
            new_list.append(transform(current.data))
            current = current.next
        return new_list
    
    def where(self, test: Any) -> LinkedList:
        # Filters the list and returns a new list containing elements that match the condition.
        new_list = LinkedList()
        current = self.head
        while current:
            if test(current.data):
                new_list.append(current.data)
            current = current.next
        return new_list
    
    def __str__(self) -> str:
        # Returns a string representation of the list for easy debugging.
        if not self.head:
            return "Empty List"
        
        nodes = []
        current = self.head
        while current:
            nodes.append(str(current.data))
            current = current.next
        return " -> ".join(nodes) + " -> None"
