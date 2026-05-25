from typing import Optional, Any
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value 
        self.next = None

class HashTable:
    def __init__(self, capacity: int =8 ) ->None:
        self.capacity: int = capacity  # index = hash(key) & (capacity - 1)
        self.size:int  = 0
        self.buckets = [None] * self.capacity # [None, None, None, None, None, None, None, None]
        self.load_factory_threshold:float = 0.75  # load factor = size / capacity
    
   
    # Converts key into a valid index within the hash table range
    def _hash(self,key ) ->int:
        return hash(key) % self.capacity
    
    def __len__(self) -> int:
        return self.size
        
       
    def _resize(self) ->None:
        # Save the old buckets before resizing
        old_buckets = self.buckets   
        # Double the capacity to reduce collisions
        self.capacity *=2
        self.buckets = [None] * self.capacity
         # Reset size because elements will be reinserted
        self.size = 0 
        
        # Reinsert all elements into the new buckets (rehashing)
        for bucket in old_buckets:
            current = bucket
          # Traverse linked list in each bucket (handling collisions)
            while current:
                self.insert(current.key,current.value)
                current = current.next
    
    def insert(self, key, value) -> None:
        # Get bucket index using hash function
        index = self._hash(key)
        # Start from first node in the bucket
        current = self.buckets[index]
        # Check if key already exists
        while current:
            # If key found, update its value
            if current.key == key:
                current.value = value
                return
            # Move to next node in linked list
            current = current.next
        #create a new node
        new_node = Node(key, value)
        #insert new node at the begining 
        new_node.next = self.buckets[index]
        #update bucket head to new node
        self.buckets[index] = new_node
        #increase number of stored elements
        self.size += 1
        
        if self.size / self.capacity > self.load_factory_threshold:
            self._resize()
    
    def delete(self, key) -> bool:
        index = self._hash(key)
        current = self.buckets[index]
        previous = None
        
        while current:
            if current.key == key:
                # If node is first node in bucket
                if previous is None:
                    self.buckets[index] = current.next
                # If node is in middle/end
                else:
                     previous.next = current.next
                     
                self.size -=1
                
                return True
            previous = current
            current = current.next
            
        return False
    
    def update(self, key, new_value) -> bool:
        
        index = self._hash(key)
        
        current = self.buckets[index]
        
        while current:
            
            if current.key == key:
                current.value = new_value
                return True
            
            current = current.next
        
        return False
    
    def search(self, key) -> Optional[Any]:
        
        index = self._hash(key)
        current = self.buckets[index]
        
        while current:
            
            if current.key == key:
                return current.value
            
            current = current.next 
            
        return None
    
    def __repr__(self) -> str:
        
        result = ""

        for index, bucket in enumerate(self.buckets):

            result += f"Bucket {index}: "

            current = bucket

            while current:
                result += f"({current.key}: {current.value}) -> "
                current = current.next

            result += "None\n"

        return result
            
        

    
    
    
      
                    
            
            
    