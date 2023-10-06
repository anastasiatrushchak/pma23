class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, initial_elements=None):
        self.head = None
        self.size = 0
        if initial_elements:
            for element in initial_elements:
                self.add_element(element)

    def insert(self, new_node):
        if self.head:
            last_node = self.head
            while last_node.next is not None:
                last_node = last_node.next
            new_node.prev = last_node
            last_node.next = new_node
        else:
            self.head = new_node
        self.size += 1

    def print(self):
        print("Normal Order:", end=" ")
        temp_node = self.head
        while temp_node is not None:
            print(temp_node.data, end=" ")
            temp_node = temp_node.next
        print(" ")

        print("Reverse Order:", end=" ")
        last_node = self.head
        while last_node is not None and last_node.next is not None:
            last_node = last_node.next

        temp_node = last_node
        while temp_node is not None:
            print(temp_node.data, end=" ")
            temp_node = temp_node.prev
        print(" ")

    def add_element(self, data):
        new_node = Node(data)
        self.insert(new_node)

    def remove_element(self, data):
        current_node = self.head
        while current_node is not None:
            if current_node.data == data:
                if current_node.prev:
                    current_node.prev.next = current_node.next
                else:
                    self.head = current_node.next

                if current_node.next:
                    current_node.next.prev = current_node.prev

                self.size -= 1
                return

            current_node = current_node.next

    def insert_at_index(self, index, data):
        new_node = Node(data)
        if index == 0:
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            self.head = new_node
            self.size += 1
            return

        current_node = self.head
        for _ in range(index - 1):
            if current_node is None:
                raise IndexError("Index out of range")
            current_node = current_node.next

        new_node.next = current_node.next
        new_node.prev = current_node
        if current_node.next:
            current_node.next.prev = new_node
        current_node.next = new_node
        self.size += 1

    def clear(self):
        self.head = None
        self.size = 0



initial_elements = [1, 2, 3, 4, 5]
linkedList = LinkedList(initial_elements)
linkedList.print()

linkedList.remove_element(3)
linkedList.print()

linkedList.insert_at_index(3, 6)
linkedList.print()
linkedList.insert_at_index(0, None)
linkedList.print()
linkedList.clear()
linkedList.print()
