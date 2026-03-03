class ListQueue:
    def __init__(self):
        # Initialize an empty list to store queue elements
        self.items = []
    
    def size(self):
        # Return the total number of items currently in the queue
        return len(self.items)