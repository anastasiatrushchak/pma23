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


class LinkedList:
    def __init__(self, arr=[]):
        self.__list = [Node(i) for i in arr]

        self._set_nodes()

    def __len__(self):
        return len(self.__list)

    def __str__(self):
        if not self.__list:
            return 'Empty Linked list'
        return 'Linked list: ' + ', '.join(str(node) for node in self.__list)

    def __getitem__(self, index):
        return self.__list[index]

    def _set_nodes(self):
        last = len(self.__list) - 1
        for i, node in enumerate(self.__list):
            if i == 0:
                node.previous_item = None
            else:
                node.previous_item = self.__list[i - 1]

            if i == last:
                node.next_item = None
            else:
                node.next_item = self.__list[i + 1]

    def remove(self, index):
        try:
            del self.__list[index]
            self._set_nodes()
        except IndexError:
            print("Error: Index out of bounds for removal.")

    def append(self, value):
        temp = Node(value)
        self.__list.append(temp)
        self._set_nodes()

    def insert(self, index, value):
        try:
            if index < 0 or index > len(self):
                raise IndexError("Wrong insert index!")
            else:
                temp = Node(value)
                self.__list.insert(index, temp)
                self._set_nodes()
        except IndexError as e:
            print(e)

    def clear(self, index):
        try:
            self[index].this_item = None
            self._set_nodes()
        except IndexError:
            print("Error: Index out of bounds for clearing.")

    def clear_list(self):
        self.__list = []



a = LinkedList([1,2,3])

a.append(1)
a.append(5)
a.append(2)
a.append(1)
a.append(9)
a.append(55)
a.append(6)
a.append(73)
print(a)

a.insert(-5, 24)
a.remove(19)
a.clear(5)
print(a)

a.clear_list()
print(a)