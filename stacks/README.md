Data structure applications: The Stack
1. The Stack - LIFO Principle

List Stack: Based on a Python array (append and pop).
Linked Stack: Based on a linked list (Singly Linked List).

List Stack (Most Common):
Python is very clever with lists; append and pop() operations from the end are very fast (O(1)).
Why use it?
 Because it's ready-made, fast, and consumes minimal memory.


 Singly Linked Stack:
Additions and deletions are always done from the head.'

Double Linked Stack:
Is it necessary? Technically not for a regular stack, since we only need one side.
Why use it? Only if you're building a more complex data structure (like Undo/Redo) that needs to move in both directions.