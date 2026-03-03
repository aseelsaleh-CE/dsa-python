from typing import Any
from src.linked_lists.linked_list import LinkedList

class Stack:
    # Stack implementation using LinkedList (LIFO).

    def __init__(self) -> None:
        self.list = LinkedList()
    
    def size(self) -> int:
        return self.list.get_length()
    
    def is_empty(self) -> bool:
        return self.list.get_length() == 0
    
    def push(self, data: Any) -> None:
        #Adds an element to the top of the stack.
        self.list.add(data)
