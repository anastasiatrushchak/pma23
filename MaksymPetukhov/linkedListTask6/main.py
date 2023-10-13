import constants


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

    def __init__(self, arr=None):
        self.size = 0
        self.head = None
        self.end = None

        if arr is not None:
            for i in range(len(arr)):
                self.push(arr[i])

    def push(self, new_data):
        self.size += 1
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            self.end = new_node
            return

        new_node.next = None
        new_node.prev = self.end
        self.end.next = new_node
        self.end = new_node

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


values = [13, 21, 18, 29, 31, 78]
values = [1, 2, 3, 4, 5]
# llist = LinkedList('Hello', 1, 4 ,6)
llist = LinkedList(values)
# llist = LinkedList()
#
# llist.push(13)
# llist.push(21)
# llist.push(18)
# llist.push(29)
# llist.push(31)
# llist.push(78)

# with open(constants.INPUT_FILE, 'r') as file:
#     lines = file.readlines()
#     for line in lines:
#         llist.push(int(line))

# values = []
# with open(constants.INPUT_FILE, 'r') as file:
#     lines = file.readlines()
#     for line in lines:
#         values.append(int(line))
#
# llist = LinkedList(values)

llist.print()
print("\nDelete element:")
llist.delete(3)
llist.print()
print("\nInsert value:")
llist.insert(3, 6)
llist.print()
print("\nInsert none:")
llist.insert(0, None)
llist.print()
print("\nErase value:")
llist.erase(2)
llist.print()
print("\nClear list:")
llist.clear()
llist.print()
