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
    
    # Rotations
    def _rotate_left(self,z: Node) ->Node:
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        self._update_height(z)
        self._update_height(y)
        
        return y
    
    def _rotate_right(self, z: Node) -> Node:
        y = z.left
        T3 = y.right 

        y.right = z
        z.left = T3

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
        elif value > node.value:
            node.right = self._insert(node.right, value)
        else:   
            return node #ignore duplicates 
         
        self._update_height(node)
        return self._rebalance(node)   
    
      #successor helper min value 
    def _get_min(self,node: Node) -> Node:
        while node.left:
            node = node.left
        return node

        
    def remove(self, value: int) ->None:
        self.root = self._remove(self.root ,value)

    def _remove(self, node, value: int) ->Node:
        if node is None:
            return None
        
        if value < node.value:
            node.left = self._remove(node.left ,value)
        elif value > node.value:
            node.right = self._remove(node.right, value)
        else:
             # found node
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            
             # two children → successor
            successor = self._get_min (node.right)
            node.value = successor.value
            node.right = self._remove(node.right, successor.value)

        self._update_height(node)
        self._rebalance(node)

    # def search (self, value: int) ->bool:
    #     return self._search(self.root, value)
    
    # def _search(self, node, value:int) ->bool:
    #     if node is None:
    #         return False
        
    #     if value == node.value:
    #         return True
    #     elif value < node.value:
    #         return self._search(node.left, value)
    #     else:
    #         return self._search(node.right, value)

    def search(self, value: int) ->bool:
        current = self.root 

        while current is not None:
            if value == current.value:
                return True
            elif value < current.value:
                current = current.left
            else:
                current = current.right

        return False
    
    def map (self, transfom_func):
        new_tree = AVLTree()
        self._map_insert(self.root, new_tree, transfom_func)
        return new_tree
    
    def _map_insert(self, node, new_tree, transform_func):
        if node is None:
            return 
        
        new_value = transform_func(node.value)

        new_tree.insert(new_value)

        self._map_insert(node.left, new_tree, transform_func)
        self._map_insert(node.right, new_tree, transform_func)
    

    def fold (self, combine_func, initial):
        return self._fold(self.root, combine_func, initial)
    
    def _fold(self, node, combine_func, acc):
        if node is None:
            return acc
        
        acc = combine_func(acc, node.value)
        acc = self._fold(node.left, combine_func, acc)
        acc = self._fold(node.right, combine_func, acc)

        return acc
    
    def filter(self, predicate_func) -> list:
        result = []
        self._filter_recursive(self.root, predicate_func, result)
        return result
    
    def _filter_recursive(self, node, predicate_func, result):
        if node is None:
            return
        if predicate_func(node.value):
            result.append(node.value)  

        self._filter_recursive(node.left, predicate_func, result)
        self._filter_recursive(node.right, predicate_func, result)   

    def in_order(self):
        result = []
        self._inorder(self.root, result)
        return result
    
    def _inorder(self, node, result):
        if node is None:
            return
        
        self._inorder(node.left, result)
        result.append(node.value)
        self._inorder(node.right, result)
    
    

    



        


    



        
 





    
