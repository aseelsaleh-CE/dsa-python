from typing import Any, Optional


class Node:
    def __init__(self, data: Any):
        # Initialize a node with data and a reference to the next node
        self.data: Any = data
        self.next: Optional[Node] = None


class LinkedStack:
    def __init__(self) -> None:
        # Initialize an empty linked stack
        self.top: Optional[Node] = None
        self.count: int = 0
    
    def is_empty(self) -> bool:
        # Check if the stack contains no nodes
        return self.count == 0


    def push(self, data: Any) -> None:
        # Create a new node and place it at the top of the stack
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self.count += 1

    # def pop(self) -> Optional[Any]:
    #     # Remove and return the data from the top node
    #     # Returns None if the stack is empty
    #     if self.is_empty():
    #         return None
    #     data = self.top.data
    #     self.top = self.top.next
    #     self.count -= 1
    #     return data