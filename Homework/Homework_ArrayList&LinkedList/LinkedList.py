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
            temp = Node(new_element)
            self.last.nextval = temp
            self.last = temp
            return True

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
