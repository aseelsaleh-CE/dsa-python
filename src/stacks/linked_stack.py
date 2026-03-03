from typing import TypeVar, Generic, List
T = TypeVar('T')
class Node(Generic[T]):
    def __init__(self, data:T):
        self.data = data
        self.next = None

class LinkedStack (Generic[T]):
    def __init__(self) -> None:
        self.top = None
        self.count : int = 0

    def push(self, data: T) -> None:
            new_node = Node(data)
            new_node.next = self.top
            self.top = new_node
            self.count += 1

    def pop(self) -> TypeVar[T]:
        if self.count == 0:
            return None
        data = self.top.data 
        self.top = self.top.next 
        self.count -= 1
        return data
    def peek(self) -> TypeVar[T]:
        if self.count > 0 :     
            return self.top.data
        else :
            return None
        
    def is_empty(self) -> bool:
        return self.count == 0
    
    def size(self) -> int:
        return self.count 
    
    def clear(self):
        self.top = None
        self.count = 0
