class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None
    def __str__(self):
        return self.dataval.__str__()
class LinkedList:
    def __init__(self):
        self.first = Node()
        self.last = Node()
    def add(self,new_element):
        if self.first.dataval == None:
            self.first.dataval = new_element
            self.last.dataval = new_element
            self.first.nextval = self.last
            return True
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
            this_value = this_value.nextval
        return "[ " + result +" ]"
linked_list = LinkedList()
linked_list.add(12)
linked_list.add(11)
linked_list.add(10)
linked_list.add(9)
linked_list.add(8)

print(linked_list)
