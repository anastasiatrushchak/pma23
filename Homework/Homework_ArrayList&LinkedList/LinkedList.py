class Node:
    def __init__(self, data_val=None):
        self.previous_val = None
        self.data_val = data_val
        self.next_val = None
    def __str__(self):
        return self.data_val.__str__()
class LinkedList:
    def __init__(self):
        self.first = Node()
        self.last = Node()
        self.size = 0
    def add(self,new_element):
        if self.size == 0:
            self.first.data_val = new_element
        elif self.size == 1:
            self.last.data_val = new_element
            self.last.previous_val = self.first
            self.first.next_val = self.last
        else:
            new_node = Node(new_element)
            self.last.next_val = new_node
            temp = self.last
            self.last = new_node
            self.last.previous_val = temp
        self.size += 1

    def remove_by_index(self, index):
        this_value = self.first
        element = 0
        while this_value:
            if element == index:
                previous_value = this_value.previous_val
                next_value = this_value.next_val

                previous_value.next_val = next_value
                next_value.previous_val = previous_value
                self.size -= 1
            this_value = this_value.next_val
            element += 1
    def __str__(self):
        result = ""
        this_value = self.first
        while this_value:
            result += this_value.__str__() + " "
            this_value = this_value.next_val
        return "[ " + result +" ]"

linked_list = LinkedList()
linked_list.add(12)
linked_list.add(11)
linked_list.add(10)
linked_list.add(9)
linked_list.add(8)

print(linked_list)
linked_list.remove_by_index(2)
print(linked_list)
