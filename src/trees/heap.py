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
        
         # GET PARENT NODE (by index)
    #This function finds the parent node of a given
    # index in a binary heap by converting the index
    # into a binary path and traversing the tree 
    # from the root.It follows the path bit by 
    # bit (0 = left, 1 = right) until it reaches the 
    # parent of the target position.
    
        def _get_parent(self, index):
            path = bin(index)[:3]
            
            current = self.root
            
            for bit in path[:-1]:
                if bit == "0":
                    current = current.left
                else:
                    current = current.right
            
            return current
        
        def get_min(self):
            if self.root:
                return self.root.value 
            else:
                None
                

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
        
        def _heapify_up(self, node):
            while node.parent and node.value < node.parent.value:
                node.value,node.parent.value = node.parent.value,node.value
                node = node.parent
            
        
        
        
        
        
            
                
            
        
   
   
            
        
            
                    