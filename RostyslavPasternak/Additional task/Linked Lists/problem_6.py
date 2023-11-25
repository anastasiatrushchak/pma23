from problem_5 import LinkedList


class Deque(LinkedList):
    def __init__(self):
        super().__init__()

    def pop(self):
        if self.size == 0:
            raise ValueError("Cannot pop from an empty deque")

        last_node = self.tail
        if self.size == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = last_node.prev
            self.tail.next = None

        self.size -= 1
        return last_node
    def popleft(self):
        temp = self.get(0)
        super().remove(temp.value)
        return temp
    def appendleft(self,data):
        super().insert(0, data)

    def remove(self, *args, **kwargs):
        raise NotImplementedError("Use pop() or popleft() for removal")

    def insert(self, *args, **kwargs):
        raise NotImplementedError("Use appendleft() for insertion")

if __name__ == "__main__":
    deque = Deque()

    deque.append(123)
    deque.append(1)
    deque.append(2)
    deque.append(3)
    print(deque)
    try:
        deque.pop()
        deque.popleft()
        deque.appendleft("99999")
        deque.remove()
        deque.insert()
        print(deque)
    except Exception as e:
        print(e)
    print(deque)





