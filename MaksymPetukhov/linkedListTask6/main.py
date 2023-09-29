class OutOfListBound(Exception):
    def __init__(self):
        self.message = "Index is out of list size!"
        super().__init__(self.message)


class Node:

    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class LinkedList:

    def __init__(self):
        self.size = 0
        self.head = None

    def push(self, new_data):
        self.size += 1
        new_node = Node(new_data)
        new_node.next = self.head
        new_node.prev = None

        if self.head is not None:
            self.head.prev = new_node

        self.head = new_node

    def delete(self, index):
        try:
            if index < 0 or index > self.size:
                raise OutOfListBound
        except OutOfListBound as e:
            print(e)
            return

        current = self.head
        temp = 0

        while current is not None:
            if temp is index:
                self.size -= 1
                if current.prev is not None:
                    current.prev.next = current.next
                else:
                    self.head = current.next

                if current.next is not None:
                    current.next.prev = current.prev

                return
            current = current.next
            temp += 1

    def insert(self, index, new_data):
        try:
            if index < 0 or index > self.size:
                raise OutOfListBound
        except OutOfListBound as e:
            print(e)
            return

        new_node = Node(new_data)

        if index == 0:
            new_node.next = self.head
            new_node.prev = None

            if self.head:
                self.head.prev = new_node
            self.head = new_node
        elif index == self.size:
            current = self.head

            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current
        else:
            current = self.head
            temp = 0

            while temp < index:
                current = current.next
                temp += 1

            new_node.prev = current.prev
            new_node.next = current
            current.prev.next = new_node
            current.prev = new_node

        self.size += 1

    def print(self):
        current = self.head

        while current is not None:
            print(current.data)
            current = current.next

    def erase(self, index):
        try:
            if index < 0 or index > self.size:
                raise OutOfListBound
        except OutOfListBound as e:
            print(e)
            return

        current = self.head
        temp = 0

        while current is not None:
            if temp is index:
                current.data = None
                return

            current = current.next
            temp += 1

    def clear(self):
        self.head = None
        self.size = 0


llist = LinkedList()
llist.push(13)
llist.push(21)
llist.push(18)
llist.push(29)
llist.push(31)
llist.push(78)

llist.print()
print("\nDelete element:")
llist.delete(0)
llist.print()
print("\nInsert value:")
llist.insert(100, 100)
llist.print()
print("\nErase value:")
llist.erase(2)
llist.print()
print("\nClear list:")
llist.clear()
llist.print()