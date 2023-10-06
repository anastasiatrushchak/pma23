class Node:
    def __init__(self, data=None):
        self.prev = None
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add(self, new_data):
        if isinstance(new_data, (list, set)):
            for data in new_data:
                self.add(data)
        else:
            if self.size == 0:
                self.head = Node(new_data)
                self.tail = self.head
            else:
                new_node = Node(new_data)
                self.tail.next = new_node
                new_node.prev = self.tail
                self.tail = new_node

            self.size += 1

    def remove_by_index(self, index):
        try:
            if index < 0 or index >= self.size:
                raise IndexError("Index out of range")

            current_node = self.head
            for i in range(index):
                current_node = current_node.next

            prev_node = current_node.prev
            next_node = current_node.next

            if prev_node:
                prev_node.next = next_node
            else:
                self.head = next_node

            if next_node:
                next_node.prev = prev_node
            else:
                self.tail = prev_node

            self.size -= 1
        except IndexError as e:
            print("Error:", str(e))

    def add_by_index(self, index, new_data):
        try:
            if index < 0 or index > self.size:
                raise IndexError("Index out of range")

            if index == self.size:
                self.add(new_data)
                return

            current_node = self.head
            for i in range(index):
                current_node = current_node.next

            new_node = Node(new_data)
            prev_node = current_node.prev

            if prev_node:
                prev_node.next = new_node
                new_node.prev = prev_node

            new_node.next = current_node
            current_node.prev = new_node

            self.size += 1

        except IndexError as e:
            print("Error:", str(e))

    def __str__(self):
        result = ""
        current_node = self.head
        while current_node:
            result += current_node.__str__() + " "
            current_node = current_node.next
        return "[ " + result + "]"


def read_array_from_file(file_name: str, separator=" "):
    try:
        with open(file_name, 'r') as readFile:
            line = readFile.readline()
    except FileNotFoundError:
        print("Файл не знайдено.")
        return []

    array = line.split(separator)
    array = [float(i) for i in array if i.isdigit()]

    return array


if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.add(read_array_from_file("array.txt"))
    linked_list.add(12)
    linked_list.remove_by_index(-19)
    linked_list.add_by_index(4,5)
    print(linked_list)
