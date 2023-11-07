class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def delete(self, data):
        current = self.head
        while current:
            if current.data == data:
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                if current == self.head:
                    self.head = current.next
                return
            current = current.next

    def insert_at_index(self, data, index):
        if index < 0:
            return
        new_node = Node(data)
        if index == 0:
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            self.head = new_node
            return

        current = self.head
        for i in range(index - 1):
            if current is None:
                return
            current = current.next

        new_node.next = current.next
        if current.next:
            current.next.prev = new_node
        current.next = new_node
        new_node.prev = current

    def clear(self):
        self.head = None


    def display(self):
        current = self.head
        while current:
            print(current.data, end=", ")
            current = current.next
        print("\n")


linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.display()
linked_list.delete(2)
linked_list.clear()
linked_list.append(4)
linked_list.append(7)
linked_list.append(5)
linked_list.append(6)
linked_list.insert_at_index(0,3)
linked_list.display()
