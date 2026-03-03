from typing import List, Any, Optional

class ListStack:
    def __init__(self) -> None:
        # Initialize an empty list to store the stack elements
        self.items: List[Any] = []

    def size(self) -> int:
        # Return the total number of items currently in the stack
        return len(self.items)
    
    def is_empty(self) -> bool:
        # Check if the stack has no items; returns True if empty, False otherwise
        return len(self.items) == 0
    
    def push(self, item: Any) -> None:
        # Add a new item to the top of the stack
        self.items.append(item)

    def pop(self) -> Any:
        # Remove and return the top item from the stack
        # Raises an IndexError if the stack is empty
        if self.is_empty():
            raise IndexError("pop from Empty Stack")
        return self.items.pop()