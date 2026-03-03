from typing import Any
from src.linked_lists.linked_list import LinkedList 

class Queue:
    #Queue implementation using LinkedList (FIFO).

    def __init__(self) -> None:
        self.list = LinkedList()
