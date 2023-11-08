class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        try:
            new_node = Node(data)
            if not self.head:
                self.head = new_node
                self.tail = new_node
            else:
                self.tail.next = new_node
                new_node.prev = self.tail
                self.tail = new_node
        except Exception as e:
            print(f"Error while appending: {e}")

    def insert(self, index, data):
        try:
            new_node = Node(data)
            if index == 0:
                new_node.next = self.head
                if self.head:
                    self.head.prev = new_node
                self.head = new_node
                if not self.tail:
                    self.tail = new_node
            else:
                current = self.head
                for _ in range(index - 1):
                    if current is None:
                        raise IndexError("Index out of range")
                    current = current.next
                new_node.next = current.next
                if new_node.next:
                    new_node.next.prev = new_node
                new_node.prev = current
                current.next = new_node
                if new_node.next is None:
                    self.tail = new_node
        except IndexError as ie:
            print(ie)
        except Exception as e:
            print(f"Error while inserting: {e}")

    def delete(self, data):
        try:
            current = self.head
            while current:
                if current.data == data:
                    if current.prev:
                        current.prev.next = current.next
                    else:
                        self.head = current.next
                    if current.next:
                        current.next.prev = current.prev
                    else:
                        self.tail = current.prev
                    return
                current = current.next
            raise ValueError("Data not found in list")
        except ValueError as ve:
            print(ve)
        except Exception as e:
            print(f"Error while deleting: {e}")

    def clear(self):
        try:
            self.head = None
            self.tail = None
        except Exception as e:
            print(f"Error while clearing: {e}")

    def __str__(self):
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        return ' <-> '.join(elements)

ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
print(ll) 
ll.insert(1, 15)
print(ll) 
ll.delete(20)
print(ll) 
ll.delete(50) 
ll.clear()
print(ll) 
