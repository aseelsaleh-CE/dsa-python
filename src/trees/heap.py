class Node:
    def __init__(self,value: int):
        self.value: int = value
        self.left = None
        self.right = None
        self.parent = None
        
class MinHeap:
    def __init__(self):
            self.root = None
            self.size = 0
            
    # This function inserts a new value into the heap        
    def insert(self, value: int) -> None:
            new_node = Node(value)
            self.size +=1
            
            if self.root is None:
                self.root = new_node
                return
            
            parent = self._get_parent(self.size)
            
            if parent.left is None:
                parent.left = new_node
            else:
                parent.right = new_node
            
            new_node.parent = parent
            self.bubble_up(new_node)
           
    # This function returns the minimum value in the heap       
    def get_min(self)-> int | None:
            if self.root:
                return self.root.value 
            else:
                return None     
        
    # This function compares the node with its parent and moves it up if needed
    def bubble_up(self, node) -> None:
            while node.parent and node.value < node.parent.value:
                node.value = node.parent.value
                node.parent.value = node.value
                node = node.parent
                 
    # This function finds the parent node using the index path   
    def _get_parent(self, index)->Node:
            path = bin(index)[3:]
            
            current = self.root
            
            for bit in path[:-1]:
                if bit == "0":
                    current = current.left
                else:
                    current = current.right
            
            return current    
        
       
         
        
       
                

        
        
        
        
            
                
            
        
   
   
            
        
            
                      