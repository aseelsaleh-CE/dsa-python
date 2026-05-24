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
            
            # if heap is empty
            if self.root is None:
                self.root = new_node
                return
            
            # find parent
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
                node.value, node.parent.value = (node.parent.value,node.value)
                node = node.parent
                 
    # This function finds the parent node using the index path   
    def _get_parent(self, index) -> Node:
        
            path = bin(index)[3:]
            
            current = self.root
            
            for bit in path[:-1]:
                if bit == "0":
                    current = current.left
                else:
                    current = current.right
            
            return current    
    

    def bubble_down(self, node: Node) ->None:
        
        while node :
           
            smallest = node 
            
            if node.left and node.left.value < smallest.value:
                smallest = node.left
            
            if node.right and node.right.value < smallest.value:
                smallest = node.right
            
            if smallest == node:
                break 
            
            node.value, smallest.value = (smallest.value,node.value)
           
            node = smallest
        
    #this function removes the minumime value from heap
    def delete_min(self) -> int | None:
        
        if self.root is None:
            return None
        
        min_value = self.root.value
        
        #only one node in heap
        if self.size == 1:
            self.root = None
            self.size = 0
            return min_value
        
        # find last node
        path = bin(self.size)[3:]
        current = self.root
        
        for bit in path:
            if bit == "0":
                current = current.left
            else:
                current = current.right
            
        last_node = current
            
        #move last node value to root 
        self.root.value = last_node.value
        
        #remove last node
        if last_node.parent.left == last_node:
            last_node.parent.left = None
        else:
            last_node.parent.right = None
        
        self.size -= 1
        
        #bubble down 
        self.bubble_down(self.root)

        return min_value    
    
    def search(self, node, value:int) -> bool:
        
        if node is None:
            return False
        
        if node.value == value:
            return True
        
        return self.search(node.left, value) or self.search(node.right, value)  
    
    #this function 
    def find_node(self, node: Node | None, value: int) -> Node | None:
       
        if node is None:
            return None
        
        if node.value == value:
            return node
         
        return (self.find_node(node.left,value) 
                or self.find_node(node.right,value) )
    
    def delete_value(self, value: int) -> bool:
       
        if self.root is None:
            return False 
        # find target node
        target = self.find_node(self.root, value)
        
        if target is None:
            return False
        
        #find last node  
        path = bin(self.size)[3:]
        current = self.root
        
        for bit in path:
            if bit =="0":
                current = current.left
            else:
                current =current.right
        
        last_node = current
        
        #replace values
        target.value = last_node.value
        
        if last_node.parent.left == last_node:
            last_node.parent.left = None
        else:
            last_node.parent.right = None
        
        self.size -=1
        
        self.bubble_down(target)
        
        if target.parent and target.value < target.parent.value:
            self.bubble_up(target)
        
        return True    
       
        
        
        
  

    
   
         
        
       
                

        
        
        
        
            
                
            
        
   
   
            
        
            
                      