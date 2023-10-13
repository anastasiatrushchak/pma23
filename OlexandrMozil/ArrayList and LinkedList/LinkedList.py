def set_nodes(linked_list):
    last = len(linked_list) - 1
    i = 0
    for j in linked_list:
        if i == 0:
            j.previous_item = None
            if len(linked_list) > 1:
                j.next_item = linked_list[i + 1]
                i += 1
                continue
            else:
                j.next_item = None
                i += 1
                continue
        elif i == last:
            j.next_item = None
            j.previous_item = linked_list[i - 1]
            continue
        else:
            j.next_item = linked_list[i + 1]
            j.previous_item = linked_list[i - 1]
            i += 1
            continue


class LinkedList:
    def __init__(self):
        self.__list = []

    def __len__(self):
        return len(self.__list)

    def __str__(self):
        output = 'Linked list: '
        for i in self.__list:
            output += str(i) + ", "
        if len(self) != 0:
            output = output[:-2]
        else:
            output = 'Empty Linked list'
        return output

    def __getitem__(self, index):
        return self.__list[index]

    def remove(self, index):
        del self.__list[index]
        set_nodes(self.__list)

    def append(self, value):
        temp = Node(value)
        self.__list.append(temp)
        set_nodes(self.__list)

    def insert(self, index, value):
        try:
            if index < 0 or index > len(self):
                raise IndexError
            else:
                temp = Node(value)
                self.__list.insert(index, temp)
        except IndexError:
            print("Wrong insert index!")
        set_nodes(self.__list)

    def clear(self, index):
        self[index].this_item = None
        set_nodes(self.__list)

    def clear_list(self):
        self.__list = []


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


# some_list = [1, 2, 3, 4]
a = LinkedList()
a.append(13)
a.append(23)
a.append(33)
a.append(43)
a.append(53)
a.append(55)
a.append(63)
a.append(73)
print(a)
a.insert(-2, 14)
a.clear(5)
print(a)
a.clear_list()
print(a)
