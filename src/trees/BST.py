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
    
    def search(self, data:int) -> bool:
        current = self.root

        while current:
            if data == current.value:
                return True
            elif data < current.value:
                current = current.left
            else:
                current = current.right

        return False
    
    def map(self, transform_func) ->BinarySearchTree:
        new_tree = BinarySearchTree()
        new_tree.root = self._map_recursive(self.root, transform_func)
        return new_tree
    

    def _map_recursive(self, node:Node, transform_func):
        if node is None:
            return None
        
        new_node = Node(transform_func(node.value))

        new_node.left = self._map_recursive(node.left, transform_func)
        new_node.right = self._map_recursive(node.right, transform_func)

        return new_node

    def fold(self, combine_func, initial):
        def traverse(node, acc):
            if node is None:
                return acc  
            
            acc = combine_func(acc, node.value)
            acc = traverse(node.left, acc)
            acc = traverse(node.right, acc)
            return acc
        
        return traverse(self.root,initial)
    
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

    #In-order Traversal (Left → Root → Right)
    def inorder(self) -> list[int]:  
        traversal =[]
        self._inorder(self.root, traversal)
        return traversal
    def _inorder(self, node, traversal):
        if node is not None:
            self._inorder(node.left,traversal)
            traversal.append(node.value)
            self._inorder(node.right,traversal)
    

                        
                        

                    
                        
                    






        