from typing import Any
from src.linked_lists.linked_list import LinkedList 

class Queue:
    #Queue implementation using LinkedList (FIFO).

    def __init__(self) -> None:
        self.list = LinkedList()
        
    def enqueue(self, data: Any) -> None:
        #Adds an element to the rear of the queue.
        self.list.append(data)
