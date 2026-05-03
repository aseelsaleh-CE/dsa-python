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
        