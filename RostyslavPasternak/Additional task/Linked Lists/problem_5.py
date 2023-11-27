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
        if isinstance(data, list):
            data = data[::-1]
            for element in data:
                self.append(element)
        else:
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
    def insert(self,index, new_element):
        if index < 0 or index > self.size:
            raise IndexError(f"Index '{index}' is out of bounds for the list.")
        if self.size == 0:
            self.append(new_element)
        else:
            this_value = self.head
            new_node = LinkedListNode(new_element)
            if index == 0:
                new_node.next = this_value
                this_value.prev = new_node
                self.head = new_node
            else:
                this_value = self.get(index)

                previous_value = this_value.prev

                previous_value.next = new_node
                this_value.prev = new_node

                new_node.next = this_value
                new_node.prev = previous_value
            self.size += 1





if __name__ == "__main__":
    linkedlist = LinkedList()

    linkedlist.append([123, 2, 3, 4])

    print("Linkedlist: ", linkedlist)
    linkedlist.insert(0, 999)
    print("Linkedlist after insertion: ", linkedlist)



