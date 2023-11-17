class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class ArrayList:
    def __init__(self):
        self.size = 0
        self.capacity = 10
        self.array = [None] * self.capacity

    def resize(self):
        new_capacity = int(1.5 * self.capacity) + 1
        new_array = [None] * new_capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.capacity = new_capacity
        self.array = new_array

    def add(self, element):
        if self.size == self.capacity:
            self.resize()
        self.array[self.size] = element
        self.size += 1

    def remove(self, element):
        if element in self.array:
            index = self.array.index(element)
            for i in range(index, self.size - 1):
                self.array[i] = self.array[i + 1]
            self.size -= 1
            self.array[self.size] = None

    def insert(self, index, element):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        if self.size == self.capacity:
            self.resize()
        for i in range(self.size, index, -1):
            self.array[i] = self.array[i - 1]
        self.array[index] = element
        self.size += 1

    def clear(self):
        self.size = 0
        self.capacity = 10
        self.array = [None] * self.capacity
