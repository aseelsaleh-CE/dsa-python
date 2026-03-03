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