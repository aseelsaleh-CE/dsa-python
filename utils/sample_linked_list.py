from linked_lists.linked_list import LinkedList
from linked_lists.doubly_linked_list import DoublyLinkedList




print("Testing Single Linked List")
sll = LinkedList()

sll.append(10)
sll.append(20)
sll.append(30)

print("List after insertion:")
sll.display()




print("\nTesting Doubly Linked List")
dll = DoublyLinkedList()

dll.insert_at_tail(100)
dll.insert_at_tail(200)
dll.insert_at_tail(300)

print("List after insertion:")
dll.display()

    