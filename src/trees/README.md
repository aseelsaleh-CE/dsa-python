# Binary Min Heap

## Overview
This project implements a *Binary Min Heap* from scratch using Python without relying on built-in list methods or external libraries.

A Min Heap is a complete binary tree where the value of each parent node is less than or equal to its children. The root node always contains the minimum value.

## Features
The heap implementation supports:

- Insert a new element
- Delete an element
- Update an existing value
- Search for a value
- Heap property maintenance (heapify)

## Project Structure

txt
trees/
│── heap.py

## Heap Operations

### Insert
Adds a new value to the heap while maintaining the Min Heap property.

*Time Complexity:* O(log n)

### Delete
Removes an element from the heap and reorganizes the structure.

*Time Complexity:* O(log n)

### Update
Updates a node value and restores heap ordering if needed.

*Time Complexity:* O(log n)

### Search
Searches for a specific value inside the heap.

*Time Complexity:* O(n)

## Heap Property
For every node:

txt
Parent <= Left Child
Parent <= Right Child

Example:

txt
        2
      /   \
     5     8
    / \
   10  15

The smallest value is always at the root.

## Testing
You can test heap operations using pytest.

Example:

pytest

## Implementation Notes
- Implemented manually from scratch
- No built-in heap libraries used
- Designed for educational and data structure learning purposes
