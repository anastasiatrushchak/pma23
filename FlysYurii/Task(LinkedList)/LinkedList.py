
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node.next.prev = node
                node = node.next

    def append(self, data):
        if not self.head:
            self.head = Node(data=data)
        else:
            node = self.head
            while node.next:
                node = node.next
            new_node = Node(data=data)
            node.next = new_node
            new_node.prev = node

    def remove(self, data):
        node = self.head
        while node:
            if node.data == data:
                if node.prev:
                    node.prev.next = node.next
                else:
                    self.head = node.next
                if node.next:
                    node.next.prev = node.prev
                return True
            node = node.next
        raise ValueError("Елемент не знайдено в списку")

    def insert(self, index, data):
        try:
            if index == 0:
                new_node = Node(data)
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node
            else:
                node = self.head
                for _ in range(index - 1):
                    if not node:
                        raise IndexError("Невірний індекс")

                    node = node.next
                if not node:
                    raise IndexError("Невірний індекс")
                new_node = Node(data)
                new_node.next = node.next
                new_node.prev = node
                if node.next:
                    node.next.prev = new_node
                node.next = new_node
        except IndexError as e:
            print(e)

    def clear(self):
        self.head = None

    def display(self):
        elements = []
        node = self.head
        while node:
            elements.append(node.data)
            node = node.next
        return elements

llist = LinkedList(["A", "B", "C", "D", 1])
l = LinkedList([1, 2, 3, 4, 5])
str(l)
l.insert(3,6)
print(l.display())
