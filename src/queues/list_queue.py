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

    def dequeue(self):
        # Remove and return the first element (front) of the queue (FIFO)
        # Raises an exception if the queue is empty
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.items.pop(0)
    
    def clear(self):
        # Remove all elements from the queue to make it empty
        self.items = []
    
    def front(self):
        # Return the value of the first element without removing it
        # Raises an exception if the queue is empty
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.items[0]