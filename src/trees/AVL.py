class Node:
    def __init__(self, value:int) -> None:
        self.value = value
        self.left = None
        self.right = None 
        self.hight: int = 1
class AVLTree:
    def __init__(self) ->None:
        self.root = None
        