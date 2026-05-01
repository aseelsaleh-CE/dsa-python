class Node:
    def __init__(self,value):
        self.value = value 
        self.left = None
        self.rigth = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, current, value):
        if value < current.value:
            if current.left is None:
                current.left = Node(value)
            else:
                self._insert_recursive(current.left, value)
        
        elif value > current.vlaue:
            if current.right is None:
                current.right = Node(value)
            else :
                self._insert_recursive(current.right, value)





    