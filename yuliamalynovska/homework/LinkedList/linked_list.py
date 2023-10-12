from node import Node


class LinkedList:
    def __init__(self, first):
        self.first = first

    def add_at_end(self, value):
        current = self.first
        while current.has_next():
            current = current.next_node
        current.next_node = Node(value, current, None)

    def add_at_begin(self, value):
        new_node = Node(value, None, self.first)
        self.first.prev_node = new_node
        self.first = new_node

    def add_by_index(self, index, value):
        i = 0
        current = self.first
        while current.has_next() and i < index:
            i += 1
            current = current.next_node
        if i == index:
            new_node = Node(value, current.prev_node, current)
            current.prev_node.next_node = new_node
            current.prev_node = new_node

    def remove(self, value):
        current = self.first
        while current.has_next():
            if current.value == value:
                break
            current = current.next_node
        if current.value == value:
            if current.prev_node is None:
                self.first = current.next_node
                current.next_node.prev_node = None
                return
            else:
                current.prev_node.next_node = current.next_node
            if current.next_node is None:
                current.prev_node.next_node = None
            else:
                current.next_node.prev_node = current.prev_node

    def __str__(self):
        current = self.first
        out = str(current.value) + " "
        while current.has_next():
            current = current.next_node
            out += str(current.value) + " "
        return out
