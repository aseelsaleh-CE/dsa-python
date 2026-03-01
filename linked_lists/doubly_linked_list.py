from typing import TypeVar, Generic
T = TypeVar('T')
class DoublyNode (Generic[T]):
    def __init__(self, data :T) :
        self.data  = data
        self.next : DoublyNode[T] = None
        self.prev : DoublyNode[T] = None


class DoublyLinkedList (Generic[T]):
    def __init__(self):
        self.head : DoublyNode[T] = None
        self.tail : DoublyNode[T] = None
        self.size :int = 0

    def __len__(self) -> int:
        return self.size
    
    
    def insert_at_head(self,data:T) ->None:
        new_node = DoublyNode(data)
        new_node.data = data
        if self.size == 0:
            self.head=self.tail = new_node
            new_node.next=new_node.prev=None
        else:
            new_node.next = self.head
            new_node.prev = None
            self.head.prev = new_node
            self.head= new_node
        self.size +=1

    def insert_at_tail(self,data:T) ->None:
            new_node = DoublyNode(data)
            new_node.data = data
            if self.size == 0:
                self.head=self.tail = new_node
                new_node.next=new_node.prev=None
            else:
                new_node.next = None
                new_node.prev = self.tail
                self.tail.next = new_node
                self.tail= new_node
            self.size +=1

    def insert_at(self, data: T, pos: int) -> None:
        if pos < 0 or pos > self.size:
            raise IndexError("Out of Range!")
        
        if pos == 0:
            self.insert_at_head(data)
            return 
        
        if pos == self.size:
            self.insert_at_tail(data)
            return

        new_node = DoublyNode(data)
        current = self.head
        
        for _ in range(pos - 1):
            current = current.next
        
        new_node.next = current.next
        new_node.prev = current
        
        if current.next:
            current.next.prev = new_node
        
        current.next = new_node
        
        self.size += 1

    def delete(self, data: T) -> bool:
        current = self.head
        while current:
            if current.data == data:
                if current == self.head:
                    self.head = current.next
                    if self.head: 
                        self.head.prev = None
                    else: self.tail = None
                elif current == self.tail:
                    self.tail = current.prev
                    self.tail.next = None
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                
                self.size -= 1
                return True
            current = current.next
        return False    

    def remove_at_tail(self) -> T:
        if self.size == 0:
            raise IndexError("List is empty")
    
        data = self.tail.data
    
        if self.size == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        
        self.size -= 1
        return data
     
    def get_at(self, index: int) -> Generic[T]:
        if index < 0 or index >= self.size:
            return None 
            
        current = self.head
        
        for _ in range(index):
                current = current.next
        
        return current.data 
    
    def contains(self, data: T) -> bool:
            current = self.head
            
            while current:
                if current.data == data:
                    return True  
                current = current.next 
                
            return False  

    def print_forward(self) -> None:
            if self.head is None:
                print("Empty List")
                return
                
            current = self.head
            elements = []
            
            while current:
                elements.append(str(current.data))
                current = current.next
                
            print(" <-> ".join(elements))

    def print_backward(self) -> None:
        if self.tail is None:
            print("Empty List")
            return
            
        current = self.tail
        elements = []
        
        while current:
            elements.append(str(current.data))
            current = current.prev  
            
        print(" <-> ".join(elements))