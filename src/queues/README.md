Queue data structure applications in Python
##This project contains various applications of the Queue data structure using three different methods.

A queue  : is a linear data structure that follows the "first in, first out" principle. The first element added is the first element removed.

Basic Operations :

enqueue: Add an item to the back
dequeue: Remove an item from the front 
front: Peek at the first item 
size: Get the number of item

 Implementations Included :

Python List Queue: Simple but slow for large data (O(n) dequeue).
Singly Linked List Queue: Efficient O(1) operations with less memory.
Doubly Linked List Queue: Most flexible with O(1) operations (Our main wrapper).


Complexity :
      	List 	Singly Linked	Doubly Linked
Enqueue	O(1)	      O(1)	            O(1)
Dequeue	O(n)	      O(1)	            O(1)
Space	O(n)	      O(n)	            O(n)


How to Run :
= Requirements

1-python
2-pytest

= Run Tests
python -m pytest

## 🚀 How to Run

```bash
python sample_queue.py