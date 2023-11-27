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


    def __str__(self):
        result = ""
        this_value = self.head
        while this_value:
            result += str(this_value) + " "
            this_value = this_value.next
        return "[ " + result + "]"


if __name__ == "__main__":
   linkedlist = LinkedList()

   linkedlist.append(123)
   linkedlist.append(1)
   linkedlist.append(2)
   linkedlist.append(3)
   print("Linkedlist: ", linkedlist)
   try:
       find_node = linkedlist.find(2)
       get_node = linkedlist.get(1)
   except Exception as e:
       print(e)
   else:
       print("Found Nodе by value: ", find_node)
       print("Found Node by index: ", get_node)
