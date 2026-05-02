class Node:
    def __init__(self,value: int) -> None:
        self.value = value 
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value: int) ->None:
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, current: Node, value: int) ->None:
        if value < current.value:
            if current.left is None:
                current.left = Node(value)
            else:
                self._insert_recursive(current.left, value)
        
        else:  # value >= current.value (duplicates go right)
            if current.right is None:
                current.right = Node(value)
            else :
                self._insert_recursive(current.right, value)

    def remove(self, value: int) ->None:
        self.root = self._remove_recursive(self.root, value)
    
    def _remove_recursive(self, current: Node |None, value: int) ->Node | None:
        if current is None:
            return None 
        
        if value < current.value:
            current.left = self._remove_recursive(current.left ,value)

        elif value > current.value:
            current.right = self._remove_recursive(current.right, value)
        
        else:
             # case 1: no children
            if current.left is None and current.right is None:
                return None
            # case 2: one child
            if current.left is None:
                return current.right
            
            if current.right is None:
                return current.left 
            
             # case 3: two children
            successor = self._find_min(current.right)
            current.value = successor.value
            current.right = self._remove_recursive(current.right, successor.value)

        return current
    
    def _find_min(self, node:Node) ->Node:
        current = node 
        while current.left:
            current = current.left
        return current
    
    def search(self, data) -> bool:
        current = self.root

        while current:
            if data == current.data:
                return True
            elif data < current.data:
                current = current.left
            else:
                current = current.right

        return False

                    
                    

                
                    
                






    