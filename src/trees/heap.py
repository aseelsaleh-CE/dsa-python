class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        
class MinHeap:
    def __init__(self):
            self.root = None
            self.size = 0
            
            
    def insert(self, value):
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
            self._heapify_up(new_node)
           
           
    def get_min(self):
            if self.root:
                return self.root.value 
            else:
                return None     
        
        
    def _heapify_up(self, node):
            while node.parent and node.value < node.parent.value:
                node.value,node.parent.value = node.parent.value,node.value
                node = node.parent
                 
        
    def _get_parent(self, index):
            path = bin(index)[3:]
            
            current = self.root
            
            for bit in path[:-1]:
                if bit == "0":
                    current = current.left
                else:
                    current = current.right
            
            return current    
        
       
         
        
       
                

        
        
        
        
            
                
            
        
   
   
            
        
            
                      