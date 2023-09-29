def set_nodes(linked_list):
    length = len(linked_list)
    i = 0

    for node in linked_list:
        node.previous_item = linked_list[i - 1] if i > 0 else None
        node.next_item = linked_list[i + 1] if i < length - 1 else None
        i += 1

class Linked_List:
    def __init__(self):
        self.__list = []

    def __len__(self):
        return len(self.__list)

    def __str__(self):
        result = 'Linked list: '
        for i in self.__list:
            result += str(i) + ", "
        if len(self) != 0:
            result = result[:-2]
        else:
            result = 'Empty Linked list'
        return result

    def __getitem__(self, index):
        return self.__list[index]

    def delete(self, index):
        del self.__list[index]
        set_nodes(self.__list)

    def add(self, value):
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

    def clear_element(self, index):
        self[index].this_item = None
        set_nodes(self.__list)

    def clear(self):
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
my_list.insert(5, 2007)
print(my_list)

