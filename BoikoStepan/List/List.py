class Linked_List:
    def __init__(self, node=None):
        self.head = node
        self.tail = self.head

    def __len__(self):
        length = 0
        current = self.head.next_item
        while current:
            length += 1
            current = current.next_item
        return length

    def __str__(self):
        result = 'Linked list: '
        current = self.head.next_item
        while current:
            result += str(current) + ", "
            current = current.next_item
        if len(self) != 0:
            result = result[:-2]
        else:
            result = 'Empty Linked list'
        return result

    def __getitem__(self, index):
        if index < 0 or index >= len(self):
            raise IndexError("Index out of range")
        current = self.head.next_item
        for i in range(index):
            current = current.next_item
        return current


    def delete(self, index):
        try:
            if index < 0 or index >= len(self):
                raise IndexError("Index out of range")
            current = self.head
            for _ in range(index):
                current = current.next_item
            current.next_item = current.next_item.next_item
        except IndexError:
            print("Index out of range. Cannot delete element.")


    def add(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
        else:
            self.tail.next_item = node
        self.tail = node



    def insert(self, index, value):
        try:
            if index < 0 or index > len(self):
                raise IndexError("Wrong insert index!")
            current = self.head
            for _ in range(index):
                current = current.next_item
            node = Node(value)
            node.next_item = current.next_item
            current.next_item = node
        except IndexError:
            print("Wrong insert index!")



    def clear(self):
        self.head.next_item = None
        self.tail = self.head


class Node:
    def __init__(self, value):
        self.this_item = value
        self.next_item = None
        self.previous_item = None

    def previous(self):
        return self.previous_item

    def next(self):
        return self.next_item

    def __str__(self):
        return str(self.this_item)


my_list = Linked_List()
my_list.add(17)
my_list.add(39)
my_list.add(198)
my_list.add(103)
my_list.add(14)
my_list.add(10)
my_list.add(666)


print(my_list)
my_list.delete(1)

print(my_list)
my_list.insert(2, 4)
print(my_list)

