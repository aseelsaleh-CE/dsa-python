Available Types (Implementations)
1. Singly Linked List
Each node contains data and a pointer to the next node only.

Advantages: Low memory consumption.
Disadvantages: No backward navigation.


2. Doubly Linked List
Each node contains data, a pointer to the next node, and a pointer to the previous node.

Advantages: High flexibility; allows deletion and addition at both ends with a speed of 0(1).
Disadvantages: Higher memory consumption (additional pointer).

        	Singly Linked	Doubly Linked
Insert at Head      	O(1)	O(1)
Insert at Tail      	O(1)	O(1)
Remove at Head	        O(1)	O(1)
Remove at Tail      	O(n)	O(1) 


## 🚀 How to Run

```bash
python sample_linked_list.py