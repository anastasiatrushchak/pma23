from problem_1 import Node


class LinkedListNode(Node):

    def __init__(self, data):
        Node.__init__(self, data)
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, data):
        new_node = LinkedListNode(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:

            self.tail.next = new_node
            new_node.prev = self.tail

            self.tail = new_node
        self.size += 1

    def find(self, data):
        this_value = self.head
        while this_value:
            if this_value.value == data:
                return this_value
            this_value = this_value.next
        raise ValueError("Item not found")

    def get(self, index: int) -> LinkedListNode:
        if index < 0 or index >= self.size:
            raise IndexError(f"Index '{index}' is out of bounds for the list.")

        current_node = self.head
        for _ in range(index):
            current_node = current_node.next
        return current_node
    def __len__(self):
        return self.size

    def __str__(self):
        result = ""
        this_value = self.head
        while this_value:
            result += str(this_value) + " "
            this_value = this_value.next
        return "[ " + result + "]"

    def remove(self, data):
        target_node = self.find(data)

        if target_node:
            if target_node.prev:
                target_node.prev.next = target_node.next
            else:
                self.head = target_node.next

            if target_node.next:
                target_node.next.prev = target_node.prev
            else:
                self.tail = target_node.prev
            self.size -= 1
        else:
            raise ValueError("Item not found")


if __name__ == "__main__":
    linkedlist = LinkedList()

    linkedlist.append([123, 2, 3, 4])
    print("Linkedlist: ", linkedlist)


    linkedlist.remove(2)
    print("Linkedlist after removal: ", linkedlist)