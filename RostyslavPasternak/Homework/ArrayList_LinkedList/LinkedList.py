def from_file(file_name: str, separator=" "):
    with open(file_name, 'r') as readFile:
        line = readFile.readline()

    array = line.split(separator)
    array = [float(i) for i in array if i.isdigit()]
    for i in range(0, 8):
        array.append(array[i] + array[i + 1])
        return array


class Node:
    def __init__(self, data_val=None):
        self.previous_val = None
        self.data_val = data_val
        self.next_val = None

    def __str__(self):
        return self.data_val.__str__()


class LinkedList:
    def __init__(self):
        self.size = 0

    def add(self, new_element):
        if isinstance(new_element, list):
            for element in new_element:
                self.add(element)
        else:
            if self.size == 0:
                self.first = Node(new_element)
                self.last = self.first
            else:
                new_node = Node(new_element)
                self.last.next_val = new_node
                new_node.previous_val = self.last
                self.last = new_node

            self.size += 1

    def remove_by_index(self, index: int):
        this_value = self.first
        element_index = 0
        while this_value:
            if element_index == index:
                previous_value = this_value.previous_val
                next_value = this_value.next_val

                previous_value.next_val = next_value
                next_value.previous_val = previous_value
                self.size -= 1
            this_value = this_value.next_val
            element_index += 1

    def add_by_index(self, index, new_element):
        this_value = self.first
        element = 0
        while this_value:
            if element == index:
                previous_value = this_value.previous_val
                new_node = Node(new_element)

                previous_value.next_val = new_node
                this_value.previous_val = new_node

                new_node.next_val = this_value
                new_node.previous_val = previous_value
                self.size += 1
            this_value = this_value.next_val
            element += 1

    def __str__(self):
        result = ""
        this_value = self.first
        while this_value:
            result += this_value.__str__() + " "
            this_value = this_value.next_val
        return "[ " + result + " ]"

    def delete(self):
        self.first = None
        self.last = None
        self.size = 0


linked_list = LinkedList()
linked_list.add(from_file("array.txt"))
linked_list.add([12, 32, 23, 4])
linked_list.add(12)
linked_list.remove_by_index(2)
linked_list.add_by_index(2, 11)
print(linked_list)
