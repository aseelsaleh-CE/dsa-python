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
    
    def pop(self) -> Any:
        #Removes and returns the top element
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self.list.remove_at(0)
    
    def peek(self) -> Any:
        #Returns the top element without removing it.
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self.list.head.data

    def clear(self) -> None:
    #Removes all elements.
        self.list.clear()

    def __str__(self) -> str:
        return str(self.list)