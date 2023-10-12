class Node:
    def __init__(self, value, prev_node, next_node):
        self.value = value
        self.prev_node = prev_node
        self.next_node = next_node

    def has_next(self):
        return self.next_node is not None

