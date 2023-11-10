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

            

    def add_at_index(self, index, data):
        new_node = Node(data)
        if index == 0:
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            self.head = new_node
            self.size += 1
            return

        current_node = self.head
        for i in range(index - 1):
            try:
                if current_node is None:
                    raise IndexError
            except IndexError:
                print("Index out of range")
                exit(-1)
            current_node = current_node.next

        new_node.next = current_node.next
        new_node.prev = current_node
        if current_node.next:
            current_node.next.prev = new_node
        current_node.next = new_node
        self.size += 1

    def remove_at_index(self, index):
        if index < 0 or index >= self.size:
            print("Index out of range")
            return

        current_node = self.head
        for i in range(index):
            current_node = current_node.next

        if current_node.prev:
            current_node.prev.next = current_node.next
        else:
            self.head = current_node.next

        if current_node.next:
            current_node.next.prev = current_node.prev

        self.size -= 1

    def remove_all_data(self, data):
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
            current_node = current_node.next

    def clear(self):
        self.head = None
        self.size = 0


initial_elements = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
linkedList = LinkedList(initial_elements)
linkedList.print()
linkedList.remove_at_index(9)
linkedList.add_element(3)
linkedList.print()
linkedList.remove_all_data(3)
linkedList.print()
