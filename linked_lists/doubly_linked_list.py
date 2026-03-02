from typing import Optional, Any

    # Represents a node in a doubly linked list with pointers to next and previous nodes.
class DoublyNode:
    def __init__(self, data: Any):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
        # Initializes an empty doubly linked list.
        def __init__(self):
            self.head = None
            self.tail = None
            self.size = 0

        # Returns the number of elements in the list.
        def __len__(self) -> int:
            return self.size
        
        # Adds a new element at the beginning of the list.
        def insert_at_head(self, data) -> None:
            new_node = DoublyNode(data)
            if self.head is None: 
                self.head = new_node
                self.tail = new_node
    
            else:
                new_node.next = self.head
                self.head.prev = new_node 
                self.head = new_node
            self.size += 1

        # Inserts a new node with the given data at tail .
        def insert_at_tail(self,data) ->None:
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

        # Inserts a new node with the given data at the specified index in the list.
        def insert_at(self, data, pos: int) -> None:
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

            next_node = current.next

            new_node.prev = current
            new_node.next = next_node

            current.next = new_node
            next_node.prev = new_node

            self.size += 1

# Deletes the first node containing the given data from the list.
        def delete(self, data) -> bool:
            current = self.head
            while current:
                if current.data == data:

                    if current == self.head:
                        self.head = current.next
                        if self.head:
                            self.head.prev = None
                        else:
                            self.tail = None

                    elif current == self.tail:
                        self.tail = current.prev
                        if self.tail:
                            self.tail.next = None

                    else:
                        current.prev.next = current.next
                        current.next.prev = current.prev

                    self.size -= 1
                    return True

                current = current.next

            return False

            
           # Returns the data at the specified zero-based index.
        def get_at(self, index: int):
           
            if index < 0 or index >= self.size:
                return None

            current = self.head
            for _ in range(index):
                current = current.next

            return current.data
        
        #Returns True if the specified data exists in the list, False otherwise.
        def contains(self, data) -> bool:
            current = self.head
            while current:
                if current.data == data:
                    return True
                current = current.next
            return False
        

        # Prints the elements of the doubly linked list from head to tail
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
                    