class Node:
    def __init__(self, value:int) -> None:
        self.value = value
        self.left = None
        self.right = None 
        self.hight: int = 1
class AVLTree:
    def __init__(self) ->None:
        self.root = None
    
    def _height(self, node) -> int:
        if node is None:
            return 0
        else:
            return node.height
        
    def _update_height(self, node) ->None:
        node.height = 1 + max(self._height(node.left), self._height(node.right))

    def _balance_factor(self, node:Node) -> int:
        return self._height(node.left) - self._height(node.right)