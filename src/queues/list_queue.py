class ListQueue:
    def __init__(self):
        # Initialize an empty list to store queue elements
        self.items = []
    
    def size(self):
        # Return the total number of items currently in the queue
        return len(self.items)
    
    def is_empty(self):
        # Check if the queue has no elements; returns True if empty, False otherwise
        return len(self.items) == 0
    
    def enqueue(self, item):
        # Add a new element to the back (end) of the queue
        self.items.append(item)