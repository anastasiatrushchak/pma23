from node import CustomNode
from linked_list import CustomLinkedList

linkedlist = CustomLinkedList(CustomNode(10, None, None))
linkedlist.add_at_end(7)
linkedlist.add_at_begin(10)
linkedlist.add_at_end(5)
linkedlist.add_at_end(2)
linkedlist.add_at_begin(0)

print(linkedlist)
linkedlist.remove(5)
print(linkedlist)
linkedlist.remove(10)
print(linkedlist)
linkedlist.remove(0)
print(linkedlist)
linkedlist.add_by_index(1, 100)
print(linkedlist)
