class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value 
        self.next = None

class HashTable:
    def __init__(self, capacity=8):
        self.capacity = capacity  # index = hash(key) & (capacity - 1)
        self.size = 0
        self.buckets = [None] * self.capacity # [None, None, None, None, None, None, None, None]
        self.load_factory_threshod = 0.75  # load factor = size / capacity
    
   
    # Converts key into a valid index within the hash table range
    def _hash(self,key):
        return hash(key) % self.capacity
       
    def _resize(self):
        # Save the old buckets before resizing
        old_bukets = self.buckets   
        # Double the capacity to reduce collisions
        self.capacity *=2
        self.buckets = [None] * self.capacity
         # Reset size because elements will be reinserted
        self.size = 0 
        
        # Reinsert all elements into the new buckets (rehashing)
        for bucket in old_bukets:
            current = bucket
          # Traverse linked list in each bucket (handling collisions)
            while current:
                self.insert(current.key,current.value)
                current = current.next
    
    def insert(self, key, value):
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
        
        if self.size / self.capacity > self.load_factory_threshod:
            self._resize()
    
    def delete(self, key):
        index = self._hash(key)
        curruent = self.buckets[index]
        previous = None
        
        while curruent:
            if curruent.key == key:
                # If node is first node in bucket
                if previous is None:
                    self.buckets[index] = curruent.next
                # If node is in middle/end
                else:
                     previous.next = curruent.next
                     
                self.size -=1
                
                return True
            previous = curruent
            curruent = curruent.next
            
        return False
    
    def update(self, key, new_value):
        
        index = self._hash(key)
        
        current = self.buckets[index]
        
        while current:
            
            if current.key == key:
                current.value = new_value
                return True
            
            current = current.next
        
        return False

    
    
    
      
                    
            
            
    