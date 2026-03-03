from typing import Any
from src.linked_lists.linked_list import LinkedList

class Stack:
    # Stack implementation using LinkedList (LIFO).

    def __init__(self) -> None:
        self.list = LinkedList()
    
    def push(self, data: Any) -> None:
        #Adds an element to the top of the stack.
        self.list.add(data)
