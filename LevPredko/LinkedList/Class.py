class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class LinkedList:
    def __init__(self):
        self.size = 0
        self.head = None
        self.end = None

    def load_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                data = [int(item) for item in file.read().split()]
                for item in data:
                    self.push(item)
        except Exception as e:
            print(f"Error reading from file: {e}")

    def push(self, new_data):
        self.size += 1
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            self.end = new_node
        else:
            new_node.prev = self.end
            self.end.next = new_node
            self.end = new_node

    def delete(self, index):
        if index < 0 or index >= self.size:
            print("Index out of list bounds")
            return

        current = self.head
        for _ in range(index):#Перевірка, чи існує попередній вузол перед поточним вузлом
            current = current.next

        self.size -= 1
        if current.prev:#Якщо поточний вузол не є головним вузлом, то встановлюється зв'язок між попереднім вузлом і наступним вузлом
            current.prev.next = current.next
        else:
            self.head = current.next
        if current.next:
            current.next.prev = current.prev

    def insert(self, index, new_value):
        if index < 0 or index > self.size:
            print("Index out of list bounds")
            return

        insert_new_value = Node(new_value)
        current = self.head

        for _ in range(index):
            current = current.next

        if current.prev:
            current.prev.next = insert_new_value
        else:
            self.head = insert_new_value
        insert_new_value.prev = current.prev
        insert_new_value.next = current
        current.prev = insert_new_value

        self.size += 1

    def clear(self):
        self.head = None
        self.size = 0

    def print(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

