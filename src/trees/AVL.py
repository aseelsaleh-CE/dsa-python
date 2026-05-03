class Node:
    def __init__(self, value:int) -> None:
        self.value = value
        self.left = None
        self.right = None 
        self.height: int = 1
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
    
    def _rebalance(self, node:Node) -> Node:
        balance = self._balance_factor(node)

        # LL
        if balance > 1 and self._balance_factor(node.left) >= 0:
            return self._rotate_right(node)
        # LR
        if balance > 1 and self._balance_factor(node.left) < 0:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)
        #RR
        if balance < -1 and self._balance_factor(node.right) <= 0:
            return self._rotate_left(node)
        # RL
        if balance < -1 and self._balance_factor(node.right) > 0:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)
        
        return node
    
    def _rotate_left(self,z: Node) ->Node:
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2
        self._update_height(z)
        self._update_height(y)
        
        return y
    
    def insert(self, value):
        self.root = self._insert(self.root, value)

    def _insert(self, node, value):
            if node is None:
                return Node(value)
            
            if value < node.value:
                node.left = self._insert(node.left, value)
            else:
                node.right = self._insert(node.right, value)
            
            self._update_height(node)
            return self._rebalance(node)   
        

        
    