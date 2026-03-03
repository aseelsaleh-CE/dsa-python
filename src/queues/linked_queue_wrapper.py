from typing import Any
from src.linked_lists.linked_list import LinkedList 

class Queue:
    #Queue implementation using LinkedList (FIFO).

    def __init__(self) -> None:
        self.list = LinkedList()
   
    def size(self) -> int:
        #Returns number of elements.
        return self.list.get_length()

    def is_empty(self) -> bool:
        #Checks if the queue is empty
        return self.list.get_length() == 0
         
    def enqueue(self, data: Any) -> None:
        #Adds an element to the rear of the queue.
        self.list.append(data)

    def dequeue(self) -> Any:
        #Removes and returns the front element.
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        return self.list.remove_at(0)
    
    def peek(self) -> Any:
        #Returns the front element without removing it.
        if self.is_empty():
            raise IndexError("Peek from empty queue")
        return self.list.head.data
    
    def clear(self) -> None:
        #Removes all elements.
        self.list.clear()


