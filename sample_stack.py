from stacks.list_stack import ListStack
from stacks.linked_stack import LinkedStack

print("Testing Stack using List")
s1 = ListStack()

s1.push(10)
s1.push(20)
s1.push(30)

print("Top element:", s1.peek())
print("Popped:", s1.pop())
print("Top after pop:", s1.peek())
print("Is empty?", s1.is_empty())

print("\nTesting Stack using Linked List")
s2 = LinkedStack()

s2.push(100)
s2.push(200)
s2.push(300)

print("Top element:", s2.peek())
print("Popped:", s2.pop())
print("Top after pop:", s2.peek())
print("Is empty?", s2.is_empty())