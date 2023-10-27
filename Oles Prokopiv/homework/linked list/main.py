class Node:
    def __init__(self, value):
        self.this_item = value
        self.next_item = None
        self.previous_item = None

class Linked_List:
    def __init__(self):
        self.__list = []

    def __len__(self):
        return len(self.__list)

    def __str__(self):
        if not self.__list:
            return 'Empty Linked list'
        result = ': '
        for node in self.__list:
            result += str(node.this_item) + ", "
        return result[:-2]

    def delete(self, index):
        try:
            if index < 0:
                index = len(self) + index
            if 0 <= index < len(self):
                del self.__list[index]
                self.set_nodes()
            else:
                print("Index out of range. Cannot delete element.")
        except IndexError:
            print("Index out of range. Cannot delete element.")

    def add(self, value):
        node = Node(value)
        self.__list.append(node)
        self.set_nodes()

    def insert(self, index, value):
        try:
            if index < 0 or index > len(self):
                raise IndexError
            node = Node(value)
            self.__list.insert(index, node)
            self.set_nodes()
        except IndexError:
            print("Wrong insert index!")

    def clear_element(self, index):
        try:
            if index < 0:
                index = len(self) + index
            if 0 <= index < len(self):
                self.__list[index].this_item = None
                self.set_nodes()
            else:
                print("Index out of range. Cannot clear element.")
        except IndexError:
            print("Index out of range. Cannot clear element.")

    def clear(self):
        self.__list = []

    def set_nodes(self):
        length = len(self)
        for i in range(length):
            self.__list[i].previous_item = self.__list[i - 1] if i > 0 else None
            self.__list[i].next_item = self.__list[i + 1] if i < length - 1 else None

my_list = Linked_List()
my_list.add(42)
my_list.add(88)
my_list.add(123)
my_list.add(555)
my_list.add(77)
my_list.add(99)
my_list.add(789)
print("Linked List", my_list)
my_list.clear_element(-103)
print("Після очищення 3-го елементу", my_list)
my_list.delete(2)
print("Після видалення 1-го елементу", my_list)
my_list.insert(5, 1001)
print("Після вставлення елемента 1001 в індексі 5", my_list)

