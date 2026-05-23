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
            
            for bit in bin[:-1]:
                if bit == "0":
                    current = current.left
                else:
                    current = current.right
            
            return current
            
   
   
            
        
            
                    