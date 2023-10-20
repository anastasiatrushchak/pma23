from array_list import ArrayList
from linked_list import LinkedList

# Приклад використання ArrayList
array_list = ArrayList()

for i in range(15):
    if i % 2 == 0:
        array_list.append(i)

array_list.insert(4, 20)
print("ArrayList:", array_list)
array_list.remove(5)
array_list.remove(13)
print("ArrayList:", array_list)

array_list.insert(3, 99)
print("ArrayList:", array_list)
array_list.clear()
print("ArrayList:", array_list)

# Приклад використання LinkedList
linked_list = LinkedList()

for i in range(15):
    if i % 2 != 0:
        linked_list.append(i)

print("LinkedList:", linked_list)
linked_list.remove(3)
linked_list.remove(11)
print("LinkedList:", linked_list)

linked_list.insert(2, 88)
print("LinkedList:", linked_list)
linked_list.clear()
print("LinkedList:", linked_list)
