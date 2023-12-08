class Node:
    def __init__(self, data=None):
        self.value = data
        self.prev = None
        self.next = None

class LinkedListNode(Node):
    def __init__(self, data):
        Node.__init__(self,data)
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
        self.size+=1

    def find(self, data):
        if self.head is None:
            raise ValueError("List is empty")
        current = self.head
        while current.next is not None:
            if current.value == data:
                return current
        raise ValueError("There is no such data in list")

    def get(self, i):
        current_node = self.head
        if i<0 or i>= self.size:
            raise IndexError("index out of range")

        for _ in range(i):
            current_node = current_node.next

        return current_node

    def  __len__(self):
        return self.size

    def __str__(self):
        result = []
        current_node = self.head
        while current_node:
            result.append('\''+str(current_node.value)+'\'')
            current_node = current_node.next
        return str(result)

    def remove(self, data):
        target = self.find(data)
        if target == self.head:
            target.prev.next = None
        else:
            target.prev.next = None
            target.next.prev = None

        prev_node = target.prev
        next_node = target.next

        if prev_node:
            prev_node.next = next_node
        else:
            self.head = next_node

        if next_node:
            next_node.prev = prev_node
        else:
            self.tail = prev_node

        self.size -= 1

    def insert(self, index, data):
        if index < 0 or index > self.size:
            raise IndexError("Index out of range")

        if index == self.size:
            self.add_last(data)
            return

        current_node = self.get(index)

        new_node = LinkedListNode(data)
        prev_node = current_node.prev

        if prev_node:
            prev_node.next = new_node
            new_node.prev = prev_node

        new_node.next = current_node
        current_node.prev = new_node

        self.size += 1

class Deque(LinkedList):
    def __init__(self):
        LinkedList.__init__(self)

    def pop(self):
        if self.size==0:
            raise ValueError("Deque is empty")


        node = self.tail
        if node.prev is not None:
            prev_node = node.prev
            prev_node.next = None
            self.tail = prev_node
        else:
            self.tail = None
            self.head = None
        return  node.value

    def pop_left(self):
        if self.size == 0:
            raise ValueError("Deque is empty")

        node = self.tail
        if node.next is not None:
            next_node = node.next
            next_node.prev = None
            self.head = next_node
        else:
            self.tail = None
            self.head = None
        return node.value

    def append_left(self, data):
        self.insert(0, data)


    def remove(self, *args, **kwargs):
        raise NotImplementedError("Use pop() or popleft() for removal")

    def insert(self, *args, **kwargs):
        raise NotImplementedError("Use append() or append_left() for appending nodes")

    @staticmethod
    def text_reverse(input_file, output_file):
        d = Deque()
        with open(input_file, 'r') as readFile:
            lines = readFile.readlines()

        for line in lines:
            d.append(line)

        with open(output_file, 'w') as writeFile:
            size = d.size
            for _ in range(size):
                writeFile.write(d.pop())




deque_instance = Deque()
deque_instance.text_reverse("input.txt", "out.txt")

