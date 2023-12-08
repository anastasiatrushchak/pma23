INDEX_ERROR = "Index error"

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append_to_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.previous = self.tail
            self.tail = new_node

    def append_to_begin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.head.previous = new_node
            new_node.next = self.head
            self.head = new_node

    def append_by_index(self, data, index = 0):
        try:
            if index == 0:
                self.append_to_begin(data)
            else:
                new_node = Node(data)
                current = self.head
                count = 0
                while current is not None and count < index - 1:
                    current = current.next
                    count += 1
                if current is None:
                    raise IndexError("Index out of bounds.")

                new_node.next = current.next
                new_node.previous = current
                if current.next is not None:
                    current.next.previous = new_node
                current.next = new_node
        except IndexError:
            print(INDEX_ERROR)



    def remove(self, data):
        current = self.head
        while current is not None:
            if current.data == data:
                if current.previous is not None:
                    current.previous.next = current.next
                else:
                    self.head = current.next

                if current.next is not None:
                    current.next.previous = current.previous
                else:
                    self.tail = current.previous

                return
            current = current.next

    def __str__(self):
        result = []
        current = self.head
        while current is not None:
            result.append(str(current.data))
            current = current.next
        return str(result)




list = LinkedList()
for i in range(10):
    list.append_to_end(1)
print("Append to the end", list)

list.append_to_begin("Zlatomyra")
print("Append to the begin", list)
list.remove(1)
print("Remove 5 ", list)
list.append_by_index(5, 6)
print(list)
